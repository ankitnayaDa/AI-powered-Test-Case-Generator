import subprocess
import sys
import os
from lib.geminiai_tests_generate import AI_generate_test_cases
from lib.json_to_robot_testcase import generate_robot_test
from lib.json_to_robot_keywords import generate_robot_keywords
from lib.json_to_robot_resources import generate_robot_resources

PYTHON = sys.executable  # Uses current venv Python

def run_step(step_name, command=None, func=None):
    print(f"\n▶ {step_name}")

    if func:  # Call the Python function
        func()
        print(f"✅ SUCCESS: {step_name}")
        return

    if command:  # Run a shell command
        print(f"   Command: {command}")
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            print(f"\n❌ FAILED: {step_name}")
            sys.exit(1)
        print(f"✅ SUCCESS: {step_name}")

def check_required_files():
    required_files = [
        "lib/geminiai_tests_generate.py",
        "lib/json_to_robot_testcase.py",
        "lib/json_to_robot_keywords.py",
        "lib/json_to_robot_resources.py",
    ]

    missing = [f for f in required_files if not os.path.exists(f)]
    if missing:
        print("❌ Missing required files:")
        for f in missing:
            print(f"   - {f}")
        sys.exit(1)

def main():
    print("\n🚀 Starting AI-Powered Test Generation Pipeline")

    check_required_files()

    run_step(
        "AI Test Case Generation (JSON + Markdown)",
        func=AI_generate_test_cases,
    )

    run_step(
        "JSON → Robot Framework Test Cases",
        func=generate_robot_test,
    )

    run_step(
        "Robot Keyword Stub Generation",
        func=generate_robot_keywords,
    )

    run_step(
        "Robot Resource File Generation",
        func=generate_robot_resources,
    )

    print("\n🎉 PIPELINE COMPLETED SUCCESSFULLY")
    print("📁 Check 'output/' and 'resources/' directories")


if __name__ == "__main__":
    main()
