import sys
import os
from fastapi import FastAPI
from app.controllers.predict_controller import router as predict_route
from app.containers import Container
from app.config.cors import CorsSetup

def create_app() -> FastAPI:
    # Inject dependencies
    container = Container()

    app = FastAPI()
    app = CorsSetup(app)
    app.include_router(predict_route, prefix="/api/predict")
    return app

app = create_app()
