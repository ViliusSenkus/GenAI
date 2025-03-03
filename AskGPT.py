import requests
import openai

def chat_with_gpt(prompt, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        print("ChatGPT:", result["choices"][0]["message"]["content"].strip())
    else:
        print("Failed to fetch response. Status code:", response.status_code, response.reason)

if __name__ == "__main__":
    api_key = "223215651654873548987"
    prompt = "What is the best phrase of Churchill?"
    chat_with_gpt(prompt, api_key)