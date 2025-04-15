from fastapi import FastAPI
import sys
from pathlib import Path

sys.path.append(Path(__file__).parent)

from routes.predict_route import router
from middle_ware.cors import setup_cors
from middle_ware.http import LogMiddleWare

app = FastAPI()

app.add_middleware(LogMiddleWare)
setup_cors(app)
app.include_router(router)
