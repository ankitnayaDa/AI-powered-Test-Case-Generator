import os
import json
import time
from google import genai
from google.genai import errors
from dotenv import load_dotenv

# --- CONFIGURATION ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print("API-KEY:",api_key)
client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-2.5-flash-lite"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Prepare the Prompt
with open("prompts/telecom_ipv6_cups_tests.txt") as f:
    template = f.read()

feature_desc = """
The system introduces IPv6 support in 4G CUPS architecture,
allowing UEs to obtain IPv6 addresses and establish data
sessions over IPv6 via SGW-U and PGW-U while control plane
functions remain on SGW-C and PGW-C using PFCP signaling.
The feature supports dual-stack IPv4/IPv6 subscribers and
ensures session continuity during control or user plane
failures
"""

# Update the prompt to ask for a specific JSON structure at the end
prompt = template.replace("{{FEATURE_DESCRIPTION}}", feature_desc)
prompt += "\n\nAlso, provide a JSON representation of these test cases at the very end of your response, wrapped in ```json code blocks."

print("Generating content (handling potential rate limits)...")

# 2. Call API with Retry Logic
response_text = None
for attempt in range(3):
    try:
        print(client.models.count_tokens(model="gemini-2.0-flash", contents=[prompt]))
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
        response_text = response.text
        print(response.usage_metadata)
        break
    except errors.ClientError as e:
        print(e)
        if "429" in str(e):
            print(f"Rate limit hit. Sleeping 30s... (Attempt {attempt+1}/3)")
            time.sleep(30)
        else:
            raise e

if response_text:
    # 3. Save the full Markdown version
    md_path = os.path.join(OUTPUT_DIR, "ipv6_cups_testcases.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(response_text)
    print(f"Saved Markdown to: {md_path}")

    # 4. Extract and Save JSON version
    if "```json" in response_text:
        # Extract content between ```json and ```
        json_str = response_text.split("```json")[1].split("```")[0].strip()
        try:
            json_data = json.loads(json_str)
            json_path = os.path.join(OUTPUT_DIR, "ipv6_cups_testcases.json")
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=4)
            print(f"Saved JSON to: {json_path}")
        except json.JSONDecodeError:
            print("Could not parse JSON block from AI response.")