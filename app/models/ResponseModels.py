'''
Object Document Model (ODM) using Pydantic
'''
from typing import List
from datetime import datetime
from pydantic import BaseConfig, BaseModel, Field
from bson import ObjectId, errors

class RecipeResponse(BaseModel):
    title: str

class SaveResponse(BaseModel):
    success: bool
    message: str
    id: str
