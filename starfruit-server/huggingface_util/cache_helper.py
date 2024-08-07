import os
from pathlib import Path
from typing import List

class CacheHelper():
    
    def __init__(self):
        self.CACHE_DIR = os.path.expanduser("~/.cache/huggingface/hub/")

        # Ensure cache directory exists
        os.makedirs(self.CACHE_DIR, exist_ok=True)
    

    def get_models(self) -> List[str]:

        # Initialize an empty list to store the formatted directory names
        formatted_dirs = []

        # Iterate over the items in the cache directory
        for item in os.listdir(self.CACHE_DIR):
            # Check if the item is a directory and not hidden or "version.txt"
            if os.path.isdir(os.path.join(self.CACHE_DIR, item)) and not item.startswith('.') and item != "version.txt":
                # Convert the directory name format from "models--Model--Version" to "Model/Version"
                formatted_dir = item.replace("models--", "").replace("--", "/")
                formatted_dirs.append(formatted_dir)
        
        return formatted_dirs


if __name__ == "__main__":
    cache_helper = CacheHelper()
    print(cache_helper.get_models())