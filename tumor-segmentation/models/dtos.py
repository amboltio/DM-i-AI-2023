from pydantic import BaseModel

class PredictRequestDto(BaseModel):
    img: str


class PredictResponseDto(BaseModel):
    img: str
