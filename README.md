# AI-powered Test Case Generator

This repository contains a GenAI (Gemini) example to generate structured test cases from a prompt template for IPv6 CUPS (Control and User Plane Separation).

**Included script:**
- `geminiai_tests_generate.py`: Uses Google GenAI (Gemini) to generate testcases from the prompt and saves both a Markdown and JSON output to the `output/` folder. Expects `GEMINI_API_KEY` in the environment.

**Prompt template:**
- `prompts/telecom_ipv6_cups_tests.txt` — production-style prompt that requests only valid JSON with a specific schema for IPv6 support in 4G CUPS.

**Outputs:**
- `output/ipv6_cups_testcases.md` — full Markdown response captured from the model.
- `output/ipv6_cups_testcases.json` — parsed JSON extracted from the model response (if present).

Quick notes
- The script is an example and assumes you have the appropriate Python packages installed and `GEMINI_API_KEY` available via a `.env` file or environment variable.
- `geminiai_tests_generate.py` includes simple retry logic and extracts the JSON code block from the LLM response.

Additional files added
- `requirements.txt` — lists dependencies used by the example (`python-dotenv`, `google-genai`).
- `.env.template` — copy this to `.env` and fill in `GEMINI_API_KEY` before running the script.
- `run_tests.py` — a tiny CLI to run the Gemini example: `python run_tests.py gemini`.

Run the CLI

```powershell
python run_tests.py gemini
```

Copy `.env.template` to `.env` first and populate the keys:

```powershell
copy .env.template .env
# then edit .env with your API keys
```

Getting started
1. Create and activate a virtual environment (recommended):

	```powershell
	python -m venv .venv
	.\\.venv\\Scripts\\Activate.ps1
	pip install -r requirements.txt  # if you create one; otherwise install needed libs
	```

2. Add API keys to a `.env` file or export them in your environment:

	- `GEMINI_API_KEY` — for `geminiai_tests_generate.py`

3. Run the Gemini example:

	```powershell
	python geminiai_tests_generate.py
	```

Where to look for results
- See the `output/` folder for generated testcases (Markdown and JSON).
- The prompt template is in `prompts/telecom_ipv6_cups_tests.txt` — edit it to change the output structure or feature description.