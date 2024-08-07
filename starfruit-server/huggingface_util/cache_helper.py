import os
from pathlib import Path



def CacheHelper():
    def __init__(self):
        CACHE_DIR = os.path.expanduser("~/.cache/huggingface/hub/")

        # Ensure cache directory exists
        os.makedirs(CACHE_DIR, exist_ok=True)



    def parse_model_id(directory_name: str) -> str:
        # Convert directory name to model ID
        if directory_name.startswith("models--"):
            # Split the directory name by '--' and take the organization and model name
            parts = directory_name.split('--')
            if len(parts) == 3:
                organization, model_name = parts[1], parts[2]
                # Construct the model ID as "organization/model_name"
                model_id = f"{organization}/{model_name}"
                return model_id
        return None
    

    def get_local_huggingface_models(self):
        # List all directories in the cache directory
        model_dirs = [d.name for d in self.CACHE_DIR.iterdir() if d.is_dir()]
        model_ids = [parse_model_id(d) for d in model_dirs if parse_model_id(d) is not None]
        return model_ids

    def get_models(self):

    # Initialize an empty list to store the formatted directory names
        formatted_dirs = []

        # Iterate over the items in the cache directory
        for item in os.listdir(self.CACHE_DIR):
            # Check if the item is a directory and not hidden or "version.txt"
            if os.path.isdir(os.path.join(self.CACHE_DIR, item)) and not item.startswith('.') and item != "version.txt":
                # Convert the directory name format from "models--Model--Version" to "Model/Version"
                formatted_dir = item.replace("models--", "").replace("--", "/")
                formatted_dirs.append(formatted_dir)