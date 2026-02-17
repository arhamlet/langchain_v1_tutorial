#  Introduction to LangChain v1
This repository serves as a foundational tutorial for learning LangChain v1. It is designed to guide you through the basic functionalities and core concepts required to build LLM-powered applications.

## Overview
LangChain is a framework designed to simplify the creation of applications using large language models (LLMs). This project focuses on the transition into Version 1 (v1), highlighting the standard ways to compose, manage, and deploy AI workflows.

## Learning Objectives
The contents of this repository cover the primary pillars of the LangChain ecosystem:

Model I/O: How to format prompts and interface with different LLM providers.

Data Connection: The basics of bringing external data into your model context.

Chains: Using the LangChain Expression Language (LCEL) to pipe components together.

Memory: Strategies for maintaining state and context in conversational interfaces.

Agents: An introduction to letting the LLM decide which tools to use for a given task.

## Getting Started
### Installation
To follow along with these tutorials, you will need to install the core LangChain package:

Bash
pip install langchain
### Configuration
Most tutorials within this repo require an API key from a provider (e.g., OpenAI, Anthropic, or HuggingFace). Ensure your environment variables are set:

Bash
# Example for OpenAI
export OPENAI_API_KEY='your_api_key_here'
## How to Use This Tutorial
Each module is designed to be explored sequentially. Start with basic model interaction and progress toward building complex, multi-step chains. The focus is on practical code implementation rather than theoretical deep dives.