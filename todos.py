from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional


app = FastAPI()
items = []
@app.post("/create-items")
def create_items(item: str):
  items.append(item)
  return items

@app.get("/check items")
def check_items(item: str):
  if item in items:
    return item
  return {"error": "item does not exist add it first"}


@app.put("/update{item_id}")
def update_items(item_id: int):
    item = items[item_id]
    return item
