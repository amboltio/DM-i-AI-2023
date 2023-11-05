from pydantic import BaseModel
from typing import List


class LunarLanderPredictRequestDto(BaseModel):
    observation: List[float]
    reward: float
    is_terminal: bool
    total_reward: float
    game_ticks: int


class LunarLanderPredictResponseDto(BaseModel):
    action: int
