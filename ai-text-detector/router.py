from fastapi import APIRouter
import random
from models.dtos import PredictRequestDto, PredictResponseDto

router = APIRouter()

@router.post('/predict', response_model=PredictResponseDto)
def predict_endpoint(request: PredictRequestDto):
    class_ids = []
    for answer in request.answers:
        class_ids.append(random.randint(0,1))

    response = PredictResponseDto(
        class_ids=class_ids
    )

    return response