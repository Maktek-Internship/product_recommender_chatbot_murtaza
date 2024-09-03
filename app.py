import streamlit as st
import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import requests
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(temperature=0, model="llama3-70b-8192")


#prompt template for gathering product information
product_info_template = """
You are a shopping assistant. The user is looking for {product_description}.
Ask follow-up questions to understand the exact product requirements.
Then search for products online, and suggest the best match with a purchase link.
"""

product_info_prompt = PromptTemplate(input_variables=["product_description"], template=product_info_template)

#llm chain
chain = LLMChain(llm=llm, prompt=product_info_prompt)

def search_product_online(query):
    # Google Custom Search API endpoint
    endpoint = "https://www.googleapis.com/customsearch/v1"
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('GOOGLE_CX')

    # Parameters for the request
    params = {
        'q': query,
        'key': api_key,
        'cx' : cx
    }

    # api request
    response = requests.get(endpoint, params=params)

    # Checking if the response is successful
    if response.status_code == 200:
        results = response.json()
        return results.get('items', [])
    else:
        return None

def generate_product_recommendation(product_description):
    conversation = chain.run(product_description=product_description)
    products = search_product_online(product_description)
    
    if not products:
        return "Sorry, no products were found."
    
    # Prepare the response with product links
    recommendation = f"{conversation}\n\nHere are some product suggestions:\n"
    for product in products[:3]:  # Limit to top 3 products
        title = product.get('title', 'No Title')
        link = product.get('link', 'No Link')
        snippet = product.get('snippet', 'No Description')
        recommendation += f"{title}\n{snippet}\nBuy here: {link}\n\n"
    
    return recommendation

#Streamlit UI

st.title("Shopping Assistant Chatbot")

# User input 
product_description = st.text_input("What product are you looking for?")

if st.button("Find Products"):
    if product_description:
        with st.spinner("Searching for the best products..."):
            try:
                recommendation = generate_product_recommendation(product_description)
                st.write(recommendation)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.write("Please enter a product description.")
