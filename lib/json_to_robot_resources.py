import json
import os
import re

INPUT_JSON = "output/ipv6_cups_testcases.json"
RESOURCE_DIR = "resources"


def normalize_keyword(step: str) -> str:
    step = re.sub(r"[^a-zA-Z0-9 ]", "", step)
    return step.title()


def load_test_cases():
    if not os.path.exists(INPUT_JSON):
        raise FileNotFoundError(f"Input JSON not found: {INPUT_JSON}")

    with open(INPUT_JSON, "r") as f:
        data = json.load(f)

    return data.get("test_cases", [])


def generate_keywords_resource(test_cases):
    keywords = set()
    for tc in test_cases:
        for step in tc.get("steps", []):
            keywords.add(normalize_keyword(step))

    lines = ["*** Keywords ***", ""]

    for kw in sorted(keywords):
        lines.extend([
            kw,
            "    [Documentation]    Auto-generated keyword stub",
            f"    Log    TODO: Implement {kw}",
            ""
        ])

    return "\n".join(lines)


def generate_variables_resource():
    lines = [
        "*** Variables ***",
        "",
        "${SGW_C}        sgw-c.example.com",
        "${SGW_U}        sgw-u.example.com",
        "${PGW_C}        pgw-c.example.com",
        "${PGW_U}        pgw-u.example.com",
        "${UE_IPV6}     2001:db8::1",
        ""
    ]
    return "\n".join(lines)


def generate_settings_resource():
    lines = [
        "*** Settings ***",
        "Library    BuiltIn",
        "Library    Collections",
        "",
        "# Protocol and telecom-specific libraries can be added here",
        "# Example:",
        "# Library    PFCPClientLibrary",
        ""
    ]
    return "\n".join(lines)


def generate_robot_resources():
    test_cases = load_test_cases()
    if not test_cases:
        raise ValueError("No test cases found in JSON")

    os.makedirs(RESOURCE_DIR, exist_ok=True)

    with open(f"{RESOURCE_DIR}/telecom_keywords.resource", "w") as f:
        f.write(generate_keywords_resource(test_cases))

    with open(f"{RESOURCE_DIR}/telecom_variables.resource", "w") as f:
        f.write(generate_variables_resource())

    with open(f"{RESOURCE_DIR}/telecom_settings.resource", "w") as f:
        f.write(generate_settings_resource())

    print("✅ Robot Framework resource files generated:")
    print(" - telecom_keywords.resource")
    print(" - telecom_variables.resource")
    print(" - telecom_settings.resource")