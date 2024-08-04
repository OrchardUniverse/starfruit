#!/usr/bin/env python

from huggingface_hub import HfApi
import json


def save_models_dict_to_file():

    hf_api = HfApi()

    models = hf_api.list_models()
    #models = hf_api.list_models(limit=10)

    models_list = [model.__dict__ for model in models]

    # Save the models to a JSON file
    with open('huggingface_models_all.json', 'w') as json_file:
        json.dump(models_list, json_file, indent=4, default=str)

    print("Model data saved to huggingface_models.json")

def save_models_to_file():

    hf_api = HfApi()

    models = hf_api.list_models()
    # models = hf_api.list_models(limit=10)

    models_list = [{
        "id": model.id,
        "created_at": model.created_at,
        "library_name": model.library_name,
        "tags": model.tags,
        "pipeline_tag": model.pipeline_tag,
        "modelId": model.modelId
    }for model in models]

    # Save the models to a JSON file
    with open('huggingface_models_all.json', 'w') as json_file:
        json.dump(models_list, json_file, indent=4, default=str)

    print("Model data saved to huggingface_models.json")

if __name__ == "__main__":
  save_models_to_file()
