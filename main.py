from fastapi import FastAPI
# from enum import Enum
# from typing import Optional
# from pydantic import BaseModel

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# # 型バリデーション
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item
#
# # Enum
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
# # Queryパラメータ
# # @app.get("/items/")
# # async def read_item(skip: int = 0, limit: int = 10):
# #     return fake_items_db[skip : skip + limit]
# #
# # class Item(BaseModel):
# #     name: str
# #     description: Optional[str] = None
# #     price: float
# #     tax: Optional[float] = None
#
# #body
# # @app.post("/items/")
# # async def create_item(item: Item):
# #     item_dict = item.dict()
# #     if item.tax:
# #         price_with_tax = item.price + item.tax
# #         item_dict.update({"price_with_tax": price_with_tax})
# #     return item_dict
