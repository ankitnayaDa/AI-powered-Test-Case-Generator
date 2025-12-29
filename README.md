# AI-Powered Test Case Generator (Telecom QA)
## Overview

This repository contains an AI-powered test case generation tool designed for telecom and cloud-native systems testing.
It leverages Large Language Models (LLMs) to automatically generate telecom-grade test cases from feature descriptions, with a focus on 4G/5G core network use cases.

The primary use case demonstrated in this project is IPv6 support in 4G CUPS (Control and User Plane Separation) architecture.

## Problem Statement

In large-scale telecom systems:

* Test case design for complex features (e.g., CUPS, IPv6, PFCP flows) is time-consuming
* Manual test creation is error-prone
* Ensuring coverage for failover, scale, and protocol edge cases requires deep domain expertise

Traditional automation frameworks help with execution, but test design remains largely manual.

## Solution

This project demonstrates how LLM-based AI can be applied to software testing problems by:

* Using telecom-specific prompt engineering
* Generating production-grade test cases
* Returning output in structured JSON and Markdown
* Making results automation-ready and reusable

The generated test cases cover:

* Functional scenarios
* Negative and boundary conditions
* Session lifecycle validation
* Failover and recovery
* Protocol-level behavior (PFCP, GTP-U)
* IPv4 / IPv6 dual-stack behavior

## Key Features

* Telecom-aware test generation (4G CUPS, PFCP, IPv6)
* LLM-driven AI test design
* Structured JSON output for machine processing
* Markdown output for human-readable documentation
* Repeatable and automated generation via Python
* Extensible for CI/CD and automation frameworks

## Example Use Case

### Feature: IPv6 support in 4G CUPS 
**Architecture:**
* SGW-C / PGW-C (Control Plane)
* SGW-U / PGW-U (User Plane)
* PFCP signaling
* Dual-stack IPv4/IPv6 support

The tool generates test cases that validate:

* PFCP session establishment with IPv6 parameters
* IPv6 address allocation
* Traffic forwarding via user plane
* Session modification and deletion
* Control plane and user plane failover
* Interoperability with IPv4-only subscribers

## Repository Structure
```
AI-powered-Test-Case-Generator/
├── prompts/
├── output/
│   ├── ipv6_cups_ai_testcases.json
│   ├── ipv6_cups_ai_testcases.md
│   └── ipv6_cups_tests.robot
├── resources/
│   ├── telecom_keywords.resource
│   ├── telecom_variables.resource
│   └── telecom_settings.resource
├── generate_tests.py
├── json_to_robot.py
├── json_to_robot_keywords.py
├── json_to_robot_resources.py
├── run_pipeline.py
├── Makefile
└── README.md
```

## How It Works

1. A telecom-grade prompt defines:
* System context
* Protocols
* Reliability and scale requirements

2. The Python script:
* Reads the prompt template
* Injects feature description
* Calls the LLM API

3. The AI returns:
* Structured JSON test cases
* Human-readable Markdown documentation
4. Outputs are saved for:
* Review
* Automation conversion
* CI/CD integration

## Prerequisites

* Python 3.9+
* An LLM API key (OpenAI / Gemini)
* Basic knowledge of telecom core networks (recommended)

## Setup & Usage
1. Clone the repository
```
git clone https://github.com/ankitnayaDa/AI-powered-Test-Case-Generator.git
cd AI-powered-Test-Case-Generator
```
2. Create virtual environment
```
python -m venv venv
source venv/bin/activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Configure API key
Create a .env file:
```
OPENAI_API_KEY=your_api_key_here
```

5. Run test case generation
```
python run_pipeline.py
```

Generated test cases will be available in the ```output/``` directory.

## Extensibility
This project is intentionally designed to be extensible:
* JSON → Robot Framework test generation
* JSON → pytest automation
* Integration with Jenkins / GitHub Actions
* Test prioritization or flaky test detection using ML
* Support for additional telecom features (5G SA, UPF, IMS)

## Robot Framework Test Generation
In addition to generating structured test cases in JSON and Markdown, this project can be extended to automatically generate Robot Framework test scripts from the AI-generated JSON output.

This enables a fully automated flow:
```Feature description → AI-generated test cases → Robot Framework automation```

## Generation Flow
* AI generates structured JSON test cases
* A conversion script parses the JSON
* Robot Framework .robot files are generated automatically
* Generated tests are ready to run in CI/CD pipelines

## Example JSON Input
```
{
  "id": "CUPS_IPV6_TC_001",
  "description": "Validate IPv6 session establishment via SGW-U",
  "steps": [
    "Trigger PDN session creation",
    "Verify PFCP session establishment",
    "Verify IPv6 address allocation",
    "Send IPv6 traffic from UE"
  ],
  "expected_result": "IPv6 session is established and traffic flows successfully",
  "protocol": ["PFCP", "GTP-U"]
}
```
## Example Generated Robot Framework Test
```
*** Test Cases ***
CUPS_IPV6_TC_001 - Validate IPv6 session establishment
    [Documentation]    Validate IPv6 session establishment via SGW-U
    [Tags]    IPv6    CUPS    PFCP

    Trigger PDN Session Creation
    Verify PFCP Session Established
    Verify IPv6 Address Allocation
    Send IPv6 Traffic From UE

    Verify IPv6 Traffic Is Successful
```
**Note**: Keywords such as Trigger PDN Session Creation and
Verify PFCP Session Established are expected to be implemented using existing telecom test libraries or custom keywords.

## Author

Ankit Kumar Nayak
Senior QA Automation Engineer
Telecom | Cloud-Native Systems | AI-Assisted Testing