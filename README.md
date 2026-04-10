# Content Moderation OpenEnv

## Description
This project simulates a real-world content moderation system where an AI agent analyzes user-generated content and makes moderation decisions. The agent must classify content as safe, toxic, spam, or abusive, and decide appropriate actions such as allow, warn, or remove.

The environment is designed following the OpenEnv specification and models realistic moderation workflows used in social media platforms, forums, and messaging systems.

## Architecture
The system consists of the following components:

- Environment (ModerationEnv): Simulates incoming content and evaluates agent actions
- Agent (LLM-based): Uses an LLM via OpenAI API to generate decisions
- Dataset: Contains structured moderation scenarios across difficulty levels
- Grader: Computes deterministic scores between 0.0 and 1.0
- Inference Pipeline: Executes tasks and logs results in the required format
- UI (Gradio): Interactive interface for testing and demonstration

## State / Action Design

### Observation (State)
- content: user-generated text
- sentiment: positive / neutral / negative
- user_history_flags: number of past violations
- previous_actions: list of actions taken so far

### Action
- label: safe / toxic / spam / abusive
- action: allow / warn / remove
- confidence: value between 0 and 1

## Reward Logic
The reward function provides continuous feedback:

- +0.5 for correct classification
- +0.4 for correct moderation action
- +0.1 for high confidence (> 0.7)

Penalties:
- -0.3 for incorrect classification
- Additional penalties for unsafe decisions (e.g., allowing toxic content)

The reward is bounded between 0.0 and 1.0.

## Tasks
The environment includes three levels of difficulty:

- Easy: clear and obvious cases
- Medium: ambiguous or sarcastic content
- Hard: complex cases including mixed intent, masked toxicity, and multilingual content

## Setup

Install dependencies:
pip install -r requirements.txt

## Run Inference
python inference.py

This will execute all tasks (easy, medium, hard) and print evaluation logs.

## Run UI
python app.py

Then open:
http://localhost:7860

## Docker
docker build -t moderation-env .
docker run -p 7860:7860 moderation-env

## Environment Variables
Set the following variables before running inference:

export API_BASE_URL=<your-endpoint>
export MODEL_NAME=<your-model>
export HF_TOKEN=<your-api-key>
