#RAG on ChatGPT example (changed to Open source models as no more tokens left :D)


import os
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from rich import print

load_dotenv()

client = OpenAI(
#  api_key=os.getenv("OPENAI_KEY")
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv('GITHUB_TOKEN')
)

information = "VIlnius is the best place to work and learn. It's very green city waiting for everyone especcialy for japan students." #RAG information added

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Extract the event information"},
    {"role": "system", "content": "Work with this data " + information}, #requesting RAG
    {"role": "user", "content": "What do you know about Vilnius?"}
  ]
)

print(completion.choices[0].message.content)

