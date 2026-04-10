import random
from env.models import Observation
from env.advanced_tasks import ADVANCED_TASKS
from env.graders import grade

class ModerationEnv:
    def __init__(self, task="easy"):
        self.task = task
        self.max_steps = 3
        self.reset()

    def reset(self):
        self.current_step = 0
        self.sample = random.choice(ADVANCED_TASKS[self.task])
        self.prev_actions = []

        return Observation(
            content=self.sample["content"],
            sentiment=self.sample["sentiment"],
            user_history_flags=self.sample["flags"],
            previous_actions=[]
        )

    def step(self, action):
        self.current_step += 1
        self.prev_actions.append(str(action))

        reward = self.compute_reward(action)
        done = self.current_step >= self.max_steps or reward > 0.8

        obs = Observation(
            content=self.sample["content"],
            sentiment=self.sample["sentiment"],
            user_history_flags=self.sample["flags"],
            previous_actions=self.prev_actions
        )

        return obs, reward, done, {"error": None}

    def state(self):
        return self.sample

    def compute_reward(self, action):
        score = grade(action, self.sample)

        if action.label != self.sample["label"]:
            score -= 0.3

        return max(min(score, 1.0), 0.0)
