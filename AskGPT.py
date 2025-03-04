import requests
import openai
import os
from dotenv import load_dotenv
from rich import print

# retrieving openai api key
load_dotenv()
api_key= os.getenv('OPENAI_KEY')

# request method
def chat_with_gpt(prompt, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "store": True,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        print("ChatGPT:", result["choices"][0]["message"]["content"].strip())
    else:
        print("Failed to fetch response. Status code:", response.status_code, response.reason)


# execution
if __name__ == "__main__":
    api_key = "223215651654873548987"
    prompt = "What is the best phrase of Churchill?"
    chat_with_gpt("write a haiku about ai", api_key)