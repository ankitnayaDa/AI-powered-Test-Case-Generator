import json
import os
import re

INPUT_JSON = "output/ipv6_cups_testcases.json"
OUTPUT_ROBOT = "tests/ipv6_cups_tests.robot"
TEST_DIR = "tests"

def normalize_keyword(step: str) -> str:
    """
    Convert step text into Robot Framework keyword style
    """
    step = re.sub(r"[^a-zA-Z0-9 ]", "", step)
    return step.title()


def robot_test(test_case: dict) -> str:
    lines = []
    test_name = f"{test_case['id']} - {test_case['description']}"
    lines.append(test_name)

    # Documentation
    lines.append(f"    [Documentation]    {test_case['description']}")

    # Tags
    tags = test_case.get("protocol", [])
    if tags:
        tag_line = "    [Tags]    " + "    ".join(tags)
        lines.append(tag_line)

    lines.append("")

    # Steps
    for step in test_case.get("steps", []):
        keyword = normalize_keyword(step)
        lines.append(f"    {keyword}")

    # Validation
    lines.append("")
    lines.append("    Verify Test Case Expected Result")

    lines.append("")
    return "\n".join(lines)


def generate_robot_test():
    os.makedirs(TEST_DIR, exist_ok=True)
    if not os.path.exists(INPUT_JSON):
        raise FileNotFoundError(f"Input JSON not found: {INPUT_JSON}")

    with open(INPUT_JSON, "r") as f:
        data = json.load(f)

    test_cases = data.get("test_cases", [])
    if not test_cases:
        raise ValueError("No test cases found in JSON")

    robot_lines = []
    robot_lines.append("*** Settings ***")
    robot_lines.append("Library    BuiltIn")
    robot_lines.append("")
    robot_lines.append("*** Test Cases ***")
    robot_lines.append("")

    for tc in test_cases:
        robot_lines.append(robot_test(tc))

    with open(OUTPUT_ROBOT, "w") as f:
        f.write("\n".join(robot_lines))

    print(f"✅ Robot Framework test file generated: {OUTPUT_ROBOT}")