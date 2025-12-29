import os
import json
import time
from google import genai
from google.genai import errors
from dotenv import load_dotenv

def AI_generate_test_cases():
    # --- CONFIGURATION ---
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    MODEL_NAME = "gemini-2.5-flash-lite"

    # 1. Prepare the Prompt
    with open("prompts/telecom_ipv6_cups_tests.txt") as f:
        prompt = f.read()

    # Update the prompt to ask for a specific JSON structure at the end
    prompt += "\n\nAlso, provide a JSON representation of these test cases at the very end of your response, wrapped in ```json code blocks."
    print("Generating content (handling potential rate limits)...")

    # 2. Call API with Retry Logic
    response_text = None
    for attempt in range(3):
        try:
            print(client.models.count_tokens(model=MODEL_NAME, contents=[prompt]))
            response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
            response_text = response.text
            print(response.usage_metadata)
            Save_test_Cases(response_text)
            break
        except errors.ClientError as e:
            print(e)
            if "429" in str(e):
                print(f"Rate limit hit. Sleeping 30s... (Attempt {attempt+1}/3)")
                time.sleep(30)
            else:
                raise e

def Save_test_Cases(response_text):
        OUTPUT_DIR = "output"
        os.makedirs(OUTPUT_DIR, exist_ok=True)
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