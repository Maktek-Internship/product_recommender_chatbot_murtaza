# Shopping Assistant Chatbot

A Streamlit application that acts as a shopping assistant chatbot. It gathers product information from users, searches for relevant products online using the Google Custom Search API, and provides product recommendations with purchase links.

## Features

- **Product Description Input**: Users can enter a description of the product they are looking for.
- **Product Recommendation**: The chatbot gathers product requirements and provides top product suggestions with links to buy.
- **Google Custom Search Integration**: Utilizes Google Custom Search API to search for products online.

## Requirements

- streamlit
- langchain
- langchain_groq
- requests
- python-dotenv


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/shopping-assistant-chatbot.git
      
2. Navigate to the project directory:
```bash
  cd shopping-assistant-chatbot
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
4. Set up your environment variables:
- Create a .env file in the project root and add your Google API key and Custom Search Engine ID:
  ```bash
  GOOGLE_API_KEY=your_google_api_key
  GOOGLE_CX=your_custom_search_engine_id
5. Run the application:
```bash
streamlit run app.py
```
# Usage
- Open the application in your browser as instructed by Streamlit.
- Enter the description of the product you are looking for in the input field.
- Click the "Find Products" button to receive product recommendations and purchase links.

