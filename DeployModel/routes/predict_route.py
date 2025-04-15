from fastapi import FastAPI, HTTPException,  UploadFile, APIRouter, File
from pathlib import Path
import sys
import json

ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))

from models.AttritionPredictor import AttritionPredictor
from config.ModelConfig import ModelConfig
from utils.logger import Logger

logger = Logger(log_file='process_data.log')

router = APIRouter()

estimator = AttritionPredictor(
    model_name=ModelConfig.MODEL_NAME,
    model_weight=ModelConfig.MODEL_WEIGHT,
    device=ModelConfig.DEVICE
)

@router.post('/predict')
async def get_prediction(file: UploadFile = File(...)):
    data = await file.read()
    json_data = json.loads(data.decode('utf-8'))
    
    logger.log.info(f"Received request with data: {json_data}. Total {len(json_data)} records.")
    response = estimator.model_inference(json_data)

    logger.log.info(f"Processed done with {len(response)} respones.")

    return response
