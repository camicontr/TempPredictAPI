#Python
from typing import List
from datetime import datetime

#Pydantic
from pydantic import BaseModel, Field, validator

#FastAPI
from fastapi import Body

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
    time_steps: int = Field(
        ...,
        gt=0,
        description="Number of temperature values to predict"
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
                "date_init": "2021-12-30 15:00:00",
                "temp_back": [28.9, 28.7, 28.1, 27.7, 27.6, 27.7, 27.7,
                              27.5, 27.1, 26.8, 26.9, 26.6, 26.6, 26.6,
                              26.6, 26.3, 26.1, 27.3, 27.4, 27.4, 28.6,
                              28.6, 28.2, 28.8, 27.9, 27.5, 27.3, 27.2,
                              27.1, 27.4],
                "time_steps": 1,
            }
        }


@app.get('/info')
async def model_info():
    # Return model information, version, how to call
    return {
        "name": "RNN temperature prediction",
        "version": "v1.0.0"
    }


@app.get('/health')
async def service_health():
    # Return service health
    return {
        "ok"
    }


@app.post('/predict')
async def model_predict(
    input: Input = Body(
        ...
        )
):
    # Predict with input
    response = get_model_response(input)
    return response
