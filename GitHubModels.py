# Models from https://github.com/marketplace/models/

from rich import print
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
# api_key= os.getenv('OPENAI_KEY')
# github_token = os.getenv('GITHUB_TOKEN')

# print(api_key)
# print(github_token)

url = "https://models.inference.ai.azure.com",

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv('GITHUB_TOKEN'),
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": "write me haiku about moon",
        }
    ],
    model="gpt-4o",
    temperature=1,
    max_tokens=4096,
    top_p=1
)
print(response.choices[0].message.content)
print('\n pirmos užklausos pabaiga \n')


# 
# Structured output
# 

from pydantic import BaseModel

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "vakar buvo didelis ginčas tarp bobo ir miko."},
    ],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed

print(event)