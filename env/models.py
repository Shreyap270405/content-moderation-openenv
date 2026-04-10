from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    content: str
    sentiment: str
    user_history_flags: int
    previous_actions: List[str]

class Action(BaseModel):
    label: str
    action: str
    confidence: float
