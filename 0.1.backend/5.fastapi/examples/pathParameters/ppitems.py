from fastapi import APIRouter

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