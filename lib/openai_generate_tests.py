from openai import OpenAI
from dotenv import load_dotenv
import os
from openai.types.chat import ChatCompletionMessageParam

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("API-KEY:",api_key)

# Initialize client
client = OpenAI(api_key=api_key)
model="gpt-3.5-turbo"
def get_completion(prompt, model=model):
    messages: list[ChatCompletionMessageParam] = [
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

# Prompt for test case generation
prompt = """
You are a senior QA engineer.
Generate functional and negative API test cases
for a user login service.
Format the output as a numbered list with descriptions.
"""

response = get_completion(prompt)
print(response)