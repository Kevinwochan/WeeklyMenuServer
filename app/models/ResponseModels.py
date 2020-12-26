'''
Object Document Model (ODM) using Pydantic
'''
from typing import List
from datetime import datetime
from pydantic import BaseConfig, BaseModel, Field
from bson import ObjectId, errors

class ResponseRecipe(BaseModel):
    title: str

class ResponseSave(BaseModel):
    success: bool
    message: str
    id: str

class Error(BaseModel):
    message: str