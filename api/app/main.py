from tokenize import String
from typing import List

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    remote: str
    time: str
    method: str
    path: str
    code: int
    size: int
    req_time: float
    agent: str
    XFF: str
    req_id: str


@app.post("/")
def update_item(item: str = Body(...)):
    print(item)
    return item
