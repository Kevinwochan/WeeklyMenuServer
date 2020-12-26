'''
Object Document Model (ODM) using Pydantic
'''
from typing import List
from datetime import datetime
from pydantic import BaseConfig, BaseModel, Field

class RecipeDB(BaseModel):
    title: str