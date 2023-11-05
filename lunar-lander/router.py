import numpy as np
from fastapi import APIRouter
from models.dtos import LunarLanderPredictRequestDto, LunarLanderPredictResponseDto


router = APIRouter()


@router.post('/predict', response_model=LunarLanderPredictResponseDto)
def predict(request: LunarLanderPredictRequestDto):
    # x, y, vx, vy, theta, vtheta, l1, l2 = oberservation = request.observation
    # reward = request.reward
    # total_reward = request.total_reward
    # game_ticks = request.game_ticks
    # lander_chrashed = request.is_terminal

    if request.is_terminal:
        print("Current game is over, a new game will start with next request!")

    # Your moves go here!
    action = int(np.random.randint(4))

    return LunarLanderPredictResponseDto(
        action=action
    )
