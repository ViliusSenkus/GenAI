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
        print("Failed to fetch response. Status code:", response.status_code)

if __name__ == "__main__":
    fetch_todos()
    api_key = "YOUR_OPENAI_API_KEY"  # Čia įrašyk savo OpenAI API raktą
    prompt = "Labas, kaip sekasi?"
    chat_with_gpt(prompt, api_key)