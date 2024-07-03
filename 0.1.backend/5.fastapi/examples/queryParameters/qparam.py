from fastapi import APIRouter

router = APIRouter(
    prefix="/qpparam",
    tags=["Query Parameters"]
)

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]