from typing import Union
from fastapi import FastAPI

from models.item_model import Item


app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello word"
    }
    
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id,
        "q": q
    }
    

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return{
        "item_id": item_id,
        "item_name": item.name 
    }