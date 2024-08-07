from typing import List
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from huggingface_hub import HfApi
from datetime import datetime

Base = declarative_base()

DATABASE_FILE_NAME = 'huggingface_models.db'
DATABASE_TABLE_NAME = 'models'


"""
{
    "id": "google-bert/bert-large-cased-whole-word-masking",
    "created_at": "2022-03-02 23:29:04+00:00",
    "tags": [
        "transformers",
        "pytorch",
        "tf",
        "jax",
        "safetensors",
        "bert",
        "fill-mask",
        "en",
        "dataset:bookcorpus",
        "dataset:wikipedia",
        "arxiv:1810.04805",
        "license:apache-2.0",
        "autotrain_compatible",
        "endpoints_compatible",
        "region:us"
    ],
    "pipeline_tag": "fill-mask"
}
"""
class HuggingFaceModel(Base):
    __tablename__ = DATABASE_TABLE_NAME
    id = Column(String, primary_key=True, unique=True, nullable=False)
    created_at = Column(DateTime)
    tags = Column(String)
    pipeline_tag = Column(String)

    def __str__(self) -> str:
        return f"Id: {self.id}, Created at: {self.created_at}, Tags: {self.tags}, Pipeline tag: {self.pipeline_tag}"


class ModelsHelper():
    def __init__(self) -> None:
        DATABASE_URL = f'sqlite:///{DATABASE_FILE_NAME}'
        engine = create_engine(DATABASE_URL, echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def download_models_to_database(self, maxSize: int = 10):
        api = HfApi()
        # TODO: Use user's token to doanload models

        models = api.list_models()

        currentSize = 0;

        for model in models:
            
            if maxSize > 0:
                currentSize += 1
                if currentSize > maxSize:
                    break

            model_info = HuggingFaceModel(
                id=model.id,
                created_at=model.created_at if model.created_at else None,
                tags=",".join(model.tags) if model.tags else None,
                pipeline_tag=model.pipeline_tag if model.pipeline_tag else None
            )

            self.session.add(model_info)

        # Commit the changes
        self.session.commit()


    def row_to_model(self, row) -> HuggingFaceModel:
        datetime_object = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S.%f")
        model = HuggingFaceModel(
            id = row[0],
            created_at = datetime_object,
            tags = row[2],
            pipeline_tag = row[3]
        )
        return model
    
    def get_models(self, limit: int = 10) -> List[HuggingFaceModel]:
        return_list = []
        result = self.session.execute(text(f"SELECT * FROM {DATABASE_TABLE_NAME} LIMIT {limit}"))
        for row in result:
            model = self.row_to_model(row)
            return_list.append(model)
        return return_list

    def search_models(self, searchString: str) -> List[HuggingFaceModel]:
        return_list = []
        result = self.session.execute(text(f"SELECT * FROM {DATABASE_TABLE_NAME} WHERE LOWER(id) LIKE '%{searchString}%'"))
        for row in result:
            model = self.row_to_model(row)
            return_list.append(model)
        return return_list

    def get_model(self, id: str) -> HuggingFaceModel:

        sql_query = text(f"SELECT * FROM {DATABASE_TABLE_NAME} WHERE id = :id")
        params = {"id": id}
        result = self.session.execute(sql_query, params)
        
        rows = result.fetchall()

        # Check if the result set has one row or more
        if len(rows) == 0:
            print("No results found.")
            return None
        elif len(rows) == 1:
            for row in rows:
                return self.row_to_model(row)
        else:
            print("More than one result found.")
            return None

    def download_model(self, id: str) -> HuggingFaceModel:

        huggingface_model = self.get_model(id)
        if huggingface_model is None:
            print("Fail to get the model")
            return None
        
        from transformers import AutoTokenizer, AutoModelForCausalLM

        tokenizer = AutoTokenizer.from_pretrained(id)
        model = AutoModelForCausalLM.from_pretrained(id)

        return huggingface_model
        
    def close(self):
        self.session.close()


if __name__ == "__main__":
    models_helper = ModelsHelper()
    #models_helper.download_models_to_database(10)
    #models = models_helper.get_models()
    #models = models_helper.search_models("qwen")
    #model = models_helper.get_model("Qwen/Qwen-7B")
    model = models_helper.download_model("google/gemma-2-2b-it")
    print(model)
    
    models_helper.close()

