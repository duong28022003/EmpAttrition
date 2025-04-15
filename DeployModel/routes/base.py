from fastapi import FastAPI, HTTPException,  UploadFile, APIRouter, File
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))

from .predict_route import router as predict_router

router = APIRouter()
router.include_router(predict_router, prefix='/Attrition_Predict')