import numpy as np
from loguru import logger
from fastapi import APIRouter
from models.dtos import PredictRequestDto, PredictResponseDto
from utils import validate_segmentation, encode_request, decode_request

router = APIRouter()

@router.post('/predict', response_model=PredictResponseDto)
def predict_endpoint(request: PredictRequestDto):

    # Decode request str to numpy array
    img: np.ndarray = decode_request(request)

    # Obtain segmentation prediction
    predicted_segmentation = predict(img)

    # Validate segmentation format
    validate_segmentation(img, predicted_segmentation)

    # Encode the segmentation array to a str
    encoded_segmentation = encode_request(predicted_segmentation)

    # Return the encoded segmentation to the validation/evalution service
    response = PredictResponseDto(
        img=encoded_segmentation
    )
    return response


### CALL YOUR CUSTOM MODEL VIA THIS FUNCTION ###
def predict(img: np.ndarray) -> np.ndarray:
    logger.info(f'Recieved image: {img.shape}')
    threshold = 50
    segmentation = get_threshold_segmentation(img,threshold)
    return segmentation

### DUMMY MODEL ###
def get_threshold_segmentation(img:np.ndarray, threshold:int) -> np.ndarray:
    return (img < threshold).astype(np.uint8)*255

    