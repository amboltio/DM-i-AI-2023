from typing import List
from pydantic import BaseModel

class PredictRequestDto(BaseModel):
    answers: List[str]

class PredictResponseDto(BaseModel):
    class_ids: List[int]