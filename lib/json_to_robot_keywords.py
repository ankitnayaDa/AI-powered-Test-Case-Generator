import json
import os
import re

INPUT_JSON = "output/ipv6_cups_testcases.json"
OUTPUT_RESOURCE = "resources/telecom_keywords.resource"

def normalize_keyword(step: str) -> str:
    step = re.sub(r"[^a-zA-Z0-9 ]", "", step)
    return step.title()


def extract_unique_keywords(test_cases):
    keywords = set()
    for tc in test_cases:
        for step in tc.get("steps", []):
            keywords.add(normalize_keyword(step))
    return sorted(keywords)


def generate_robot_keywords():
    if not os.path.exists(INPUT_JSON):
        raise FileNotFoundError(f"Input JSON not found: {INPUT_JSON}")

    with open(INPUT_JSON, "r") as f:
        data = json.load(f)

    test_cases = data.get("test_cases", [])
    if not test_cases:
        raise ValueError("No test cases found in JSON")

    keywords = extract_unique_keywords(test_cases)

    os.makedirs("resources", exist_ok=True)

    lines = []
    lines.append("*** Keywords ***")
    lines.append("")

    for kw in keywords:
        lines.append(kw)
        lines.append("    [Documentation]    Auto-generated keyword stub")
        lines.append(f"    Log    TODO: Implement {kw}")
        lines.append("")

    with open(OUTPUT_RESOURCE, "w") as f:
        f.write("\n".join(lines))

    print(f"✅ Robot Framework keyword stubs generated: {OUTPUT_RESOURCE}")