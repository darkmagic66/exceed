from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price:float

@app.get("/")
def rpp():
    return {"Hello": "Exceed"}

@app.post("/")
def root_post():
    name = "jim"
    return {"Hello": name}




@app.get("/items/{item_id}")
def get_item(item_id: int,q:Optional[str]=None):
    num = item_id+1
    return{"item_id":num,"q":q}

@app.post("/items/{item_id}")
def get_item(item_id: int,item: Item):
    return{"price":item.price,"name":item.name}

