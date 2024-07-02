from fastapi import APIRouter
from enum import Enum

router = APIRouter(
    prefix="/ppitems",
    tags=["Path Parameters"]
)

@router.get("/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@router.get("/int/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}




#Working with Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#Path parameters containing paths
@router.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}