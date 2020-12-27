'''
Object Document Model (ODM) using Pydantic
'''
from typing import List
'''
A model defining the structure of HTTP JSON responses
'''

from pydantic import BaseConfig, BaseModel, Field
from pydantic.dataclasses import dataclass
from bson import ObjectId, errors

class RecipeResponse(BaseModel):
    title: str
    subtitle: str
    description: str
    tags: List[str]
    instructions: List[str]
    ingredients: List[str]

class SaveResponse(BaseModel):
    success: bool
    message: str
    id: str
