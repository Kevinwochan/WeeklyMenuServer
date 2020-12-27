'''
A model defining the structure of HTTP JSON requests
'''
from typing import List, Optional
from pydantic import BaseModel, Field, BaseConfig
from pydantic.dataclasses import dataclass
from bson import ObjectId, errors

class Ingredient(BaseModel):
    name: str

class Instruction(BaseModel):
    description: str

class RecipeRequest(BaseModel):
    title: str
    subtitle: str = ''
    description: str = ''
    tags: List[str] = []
    instructions: List[Instruction] = []
    ingredients: List[Ingredient] = []

