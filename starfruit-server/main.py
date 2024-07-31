from fastapi import FastAPI, HTTPException
from modelscope.hub.snapshot_download import snapshot_download
import os
import json
from pathlib import Path
from typing import List
from huggingface_hub import HfApi, list_models, HfFolder
import yaml
from pathlib import Path
from transformers.file_utils import CONFIG_NAME, WEIGHTS_NAME

app = FastAPI()

# Define the path to the local models directory
local_models_dir = os.path.expanduser('~/.cache/modelscope/hub')
HUGGINGFACE_CACHE_DIR = Path(os.path.expanduser("~/.cache/huggingface/hub/"))


token = "hf_xxx"

# Or configure a HfApi client
hf_api = HfApi(
    endpoint="https://huggingface.co", # Can be a Private Hub endpoint.
    token=token, # Token is not persisted on the machine.
)


"""
Example data:

[
  ".locks",
  "models--Qwen--Qwen2-0.5B"
]
"""
def get_huggingface_model_list() -> List[str]:
    if not HUGGINGFACE_CACHE_DIR.exists():
        raise HTTPException(status_code=404, detail="Hugging Face cache directory not found.")
    
    # List all directories in the Hugging Face cache directory
    model_dirs = [d.name for d in HUGGINGFACE_CACHE_DIR.iterdir() if d.is_dir()]
    return model_dirs

# Function to get detailed info about each local model
"""
Example data:

[
  "qwen"
]
"""
def get_local_model_info(model_name):
    model_path = os.path.join(local_models_dir, model_name)
    
    # Check if the model directory exists
    if not os.path.isdir(model_path):
        raise HTTPException(status_code=404, detail="Model not found")
    
    model_list = os.listdir(model_path)

    return model_list

# Endpoint to list all local models
@app.get("/models/")
def list_models():
    local_models = os.listdir(local_models_dir)
    local_models_info = [get_local_model_info(model) for model in local_models]
    return local_models_info
    
    #model_list = get_model_list()
    #return model_list

    

# Endpoint to get info about a specific model
@app.get("/models/{model_name}")
def get_model_info(model_name: str):
    model_info = get_local_model_info(model_name)
    return model_info

# Endpoint to download a model
@app.post("/models/download/{model_name}")
def download_model(model_name: str):
    try:
        model_path = snapshot_download(model_name)
        return {"model_name": model_name, "path": model_path}
    except Exception as e:
        return {"error": str(e)}

@app.get("/hg_models")
def list_remote_models():
    config_file = Path.home() / ".config" / "huggingface_models.yaml"
    if config_file.exists():
        return {"exists": True, "path": str(config_file)}
    else:
        return {"exists": False, "path": str(config_file)}

    models = hf_api.list_models()
    return models

@app.get("/remote/datasets")
def list_remote_datasets():
    datasets = hf_api.list_datasets()
    return datasets

@app.get("/local/models")
def list_local_models():
    cache_dir = HfFolder().cache_dir
    models = []
    for root, dirs, files in os.walk(cache_dir):
        if CONFIG_NAME in files or WEIGHTS_NAME in files:
            models.append(root)
    return models

@app.get("/local/datasets")
def list_local_datasets():
    datasets_dir = os.path.join(HfFolder().cache_dir, "datasets")
    datasets = [name for name in os.listdir(datasets_dir) if os.path.isdir(os.path.join(datasets_dir, name))]
    return datasets

@app.post("/huggingface_models/sync")
def save_models_to_file():
    models = hf_api.list_models()
    models_data = [model.modelId for model in models]

    config_dir = Path.home() / ".config"
    config_dir.mkdir(exist_ok=True)

    models_file = config_dir / "huggingface_models.yaml"

    with models_file.open("w") as file:
        yaml.dump(models_data, file)

    return {"message": f"Saved {len(models_data)} models to {models_file}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
