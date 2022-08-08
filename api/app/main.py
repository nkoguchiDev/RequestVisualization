import json

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
    component: str


@app.post("/")
def update_item(logs: str = Body(...)):
    logs = logs.split("\n")
    logs = [json.loads(i) for i in logs if i]
    print(logs)
    return logs
