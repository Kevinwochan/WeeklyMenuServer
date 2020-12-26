'''
Object Document Model (ODM) using Pydantic
'''
from typing import List
from datetime import datetime
from pydantic import BaseModel
from bson import ObjectId, errors

class RecipeRequest(BaseModel):
    title: str