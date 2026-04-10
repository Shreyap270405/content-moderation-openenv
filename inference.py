import os
import json
from openai import OpenAI
from env.moderation_env import ModerationEnv
from env.models import Action

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

def get_action(obs):
    prompt = f"""
    Classify content:
    {obs.content}

    Return JSON:
    {{
      "label": "...",
      "action": "...",
      "confidence": 0.0
    }}
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    try:
        parsed = json.loads(response.choices[0].message.content)
        return Action(**parsed)
    except:
        return Action(label="safe", action="allow", confidence=0.5)

def run_task(task):
    env = ModerationEnv(task)
    obs = env.reset()

    print(f"[START] task={task} env=content-moderation model={MODEL_NAME}")

    rewards = []
    success = False

    for step in range(10):
        action = get_action(obs)
        obs, reward, done, info = env.step(action)

        rewards.append(f"{reward:.2f}")

        print(f"[STEP] step={step+1} action={action} reward={reward:.2f} done={str(done).lower()} error={info.get('error')}")

        if done:
            success = reward > 0.7
            break

    score = float(rewards[-1]) if rewards else 0.0

    print(f"[END] success={str(success).lower()} steps={step+1} score={score:.2f} rewards={','.join(rewards)}")

if __name__ == "__main__":
    for t in ["easy", "medium", "hard"]:
        run_task(t)
