from fastapi import FastAPI, HTTPException, APIRouter
from huggingface_hub import HfApi
import json
from typing import List, Optional
import os
from pydantic import BaseModel
from pathlib import Path

from pydantic_sqlalchemy import sqlalchemy_to_pydantic



from huggingface_util.models_helper import ModelsHelper
from huggingface_util.models_helper import HuggingFaceModel

PydanticHuggingFaceModel= sqlalchemy_to_pydantic(HuggingFaceModel)


app = FastAPI()

router = APIRouter(prefix="/api")
models_helper = ModelsHelper()


class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True



@router.get("/huggingface_models/", response_model=List[PydanticHuggingFaceModel])
async def get_huggingface_models():
    return [PydanticHuggingFaceModel.from_orm(model) for model in models_helper.get_models(10)]


@router.get("/models")
async def get_cached_models():
    try:
        #cached_models = os.listdir(CACHE_DIR)
        return {"cached_models": []}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)