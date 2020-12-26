'''
Object Document Model (ODM) using Pydantic
'''
from typing import List
from pydantic import BaseModel, Field, BaseConfig
from pydantic.dataclasses import dataclass
from bson import ObjectId, errors

class MongoConfig(BaseConfig):
    allow_population_by_field_name = True
    json_encoders = {
        id: lambda id: str(id)
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

@dataclass(config=MongoConfig)
class RecipeRequest(BaseModel):
    id : MongoId = Field(alias='_id')
    title: str