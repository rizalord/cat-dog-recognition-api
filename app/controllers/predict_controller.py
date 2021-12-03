from fastapi import APIRouter, Depends, File, UploadFile, Response, status
from dependency_injector.wiring import inject, Provide
from pydantic import BaseModel

from app.services.predict_service import PredictService
from app.containers import Container

router = APIRouter()


class PredictResponse(BaseModel):
    status: bool
    animalName: str
    percentage: int
    message: str



@router.post("/", response_model=PredictResponse, status_code=200)
@inject
def predict(
    response: Response,
    predict_service: PredictService = Depends(
        Provide[Container.predict_service]),
    file: UploadFile = File(...),
):
    try:
        # check if file exist
        if file is None:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return PredictResponse(
                status=False,
                message="File not found",
            )

        # convert file to bytes
        file_bytes = file.file.read()

        animalName, percentage, message = predict_service.predict(file_bytes)
        return PredictResponse(
            status=True,
            animalName=animalName,
            percentage=percentage,
            message=message
        )
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return PredictResponse(
            status=False,
            message=str(e)
        )
