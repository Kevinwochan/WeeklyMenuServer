'''
Object Document Model (ODM) using Pydantic
'''
from typing import List
from datetime import datetime
from bson import ObjectId
from pydantic import BaseConfig, BaseModel, Field
from pydantic.dataclasses import dataclass
from pydantic import Extra

class MongoConfig(BaseConfig):
    allow_population_by_field_name = True
    fields = {'id': '_id'}
    json_encoders = {
        ObjectId: lambda id: str(id)
    }

class MongoId(ObjectId):
    '''
    A wrapper to allow validation of ObjectIds
    '''
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError('ObjectId required')
        return str(v)

class RecipeDB(BaseModel):
    id: MongoId = Field(..., alias='_id')
    title: str
    subtitle: str
    description: str
    tags: List[str]
    instructions: List[str]
    ingredients: List[str]
    
