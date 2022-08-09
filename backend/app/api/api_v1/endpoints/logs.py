import json

from fastapi import APIRouter, Body

router = APIRouter()


def convert_records_to_json(records):
    return [json.loads(i) for i in records.split("\n") if i]


@router.post("/")
def update_item(records: str = Body(...)):
    print(convert_records_to_json(records))
    return records
