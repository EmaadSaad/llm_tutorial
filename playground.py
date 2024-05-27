from openai import OpenAI


### this is all so we can securely access our api key
import os
from dotenv import load_dotenv
load_dotenv()


openai_client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

prompt = "You are a earthquake predictor"
formatted_system_prompt = {"role": "system", "content": prompt}
messages = []

messages.append(formatted_system_prompt)

response = openai_client.chat.completions.create(
    model = "gpt-4o",
    temperature = 0,
    max_tokens = 100,
    messages = messages,

)

print(response.choices[0].message.content)

