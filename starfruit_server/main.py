from fastapi import FastAPI, HTTPException
from modelscope.hub.snapshot_download import snapshot_download
import os
import json

app = FastAPI()

# Define the path to the local models directory
local_models_dir = os.path.expanduser('~/.cache/modelscope/hub')

# Function to get detailed info about each local model
def get_local_model_info(model_name):
    model_path = os.path.join(local_models_dir, model_name)
    
    # Check if the model directory exists
    if not os.path.isdir(model_path):
        raise HTTPException(status_code=404, detail="Model not found")
    
    model_info = {
        'model_name': model_name,
        'path': model_path,
    }
    
    # Example of reading a config file or metadata file if exists
    config_path = os.path.join(model_path, 'config.json')
    model_info_path = os.path.join(model_path, 'model_info.json')

    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            model_info['config'] = json.load(f)

    if os.path.exists(model_info_path):
        with open(model_info_path, 'r') as f:
            model_info['details'] = json.load(f)
    
    # Add more file reads as necessary
    # Example: Reading weights or other metadata files
    
    return model_info

# Endpoint to list all local models
@app.get("/models/")
def list_models():
    local_models = os.listdir(local_models_dir)
    local_models_info = [get_local_model_info(model) for model in local_models]
    return local_models_info

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
