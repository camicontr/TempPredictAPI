#Python
from typing import List
from datetime import datetime

#Pydantic
from pydantic import BaseModel, Field, validator

#FastAPI
from fastapi import Body
from fastapi import status

#Auxiliary
from ms import app
from ms.auxiliar import get_model_response


# Input for data validation
class Input(BaseModel):
    date_init: datetime = Field(
        ...,
        description="Starting date of the temperature list"
        )
    temp_back: List[float] = Field(
        ...,
        description="Last 30 previous temperature values"
        )
    
    @validator("date_init", pre=True)
    def parse_date(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d %H:%M:%S"
        )

    class Config:
        schema_extra = {
            "example": {
                "date_init": "2021-12-30 20:00:00",
                "temp_back": [28.9, 28.7, 28.1, 27.7, 27.6, 27.7, 27.7,
                              27.5, 27.1, 26.8, 26.9, 26.6, 26.6, 26.6,
                              26.6, 26.3, 26.1, 27.3, 27.4, 27.4, 28.6,
                              28.6, 28.2, 28.8, 27.9, 27.5, 27.3, 27.2,
                              27.1, 27.4]
            }
        }


class Prediction(BaseModel):
    date_pred: datetime = Field(
        ...,
        description="date of the temperature predict"
        )
    temp_pred: float = Field(...)


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"],
    summary="Home from app"
    )
async def home():
    """
    Home

    This is the home from app

    No parameters 

    Returns dictionary with model information, version
    """
    return {
        "name": "RNN temperature prediction",
        "version": "v1.0.0"
    }


@app.post(
    path='/predict',
    response_model=Prediction,
    status_code=status.HTTP_200_OK,
    tags=["Predict"],
    summary="Prediction"
    )
async def model_predict(
    input: Input = Body(
        ...
        )
):
    """
    Predict

    This is the path operation for temperature predict using the last 30 temperature values

    - Body parameter
        - **input** -> This is the class input with date init and last 30 temperature values 

    Returns temperature prediction with your date information
    """
    response = get_model_response(input)
    return response
