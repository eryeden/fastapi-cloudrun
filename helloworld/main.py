from fastapi import FastAPI
from enum import Enum
from typing import Union
from pydantic import BaseModel
import os


app = FastAPI()


# root
@app.get("/")
async def root():
    name = os.environ.get("NAME", "World")
    return {"message": "Hello World", "name": name}
