from fastapi import FastAPI, HTTPException, APIRouter, Query
from typing import List
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from huggingface_util.models_helper import ModelsHelper
from huggingface_util.models_helper import HuggingFaceModel
from huggingface_util.cache_helper import CacheHelper

PydanticHuggingFaceModel= sqlalchemy_to_pydantic(HuggingFaceModel)

# Initialize the FastAPI app
app = FastAPI()
router = APIRouter(prefix="/api")

# Initialize the HuggingFace helper
models_helper = ModelsHelper()
cache_helper = CacheHelper()

@router.get("/huggingface_models/", response_model=List[PydanticHuggingFaceModel])
async def get_huggingface_models():
    models = models_helper.get_models(10)
    return [PydanticHuggingFaceModel.from_orm(model) for model in models]

@router.get("/huggingface_models/model", response_model=PydanticHuggingFaceModel)
async def get_huggingface_model(id: str = Query(..., description="The ID of the item, including slashes encoded as %2F")):
    model = models_helper.get_model(id)
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return PydanticHuggingFaceModel.from_orm(model)

@router.get("/huggingface_models/search", response_model=List[PydanticHuggingFaceModel])
async def get_huggingface_model(id: str = Query(..., description="The ID of the item, including slashes encoded as %2F")):
    models = models_helper.search_models(id)
    return [PydanticHuggingFaceModel.from_orm(model) for model in models]


@router.get("/models", response_model=List[str])
async def get_cached_models() :
    try:
        return cache_helper.get_models()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models/model", response_model=PydanticHuggingFaceModel)
async def get_huggingface_model(id: str = Query(..., description="The ID of the item, including slashes encoded as %2F")):
    model = models_helper.get_model(id)
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return PydanticHuggingFaceModel.from_orm(model)


app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)