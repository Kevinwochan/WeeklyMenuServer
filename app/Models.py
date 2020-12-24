'''
Object Document Model (ODM) using Pydantic
'''
from typing import List
from datetime import datetime
from pydantic import BaseConfig, BaseModel, Field
from bson import ObjectId, errors

'''
class Ingredient():
    name = StringField()
    units = StringField()
    allergens = ListField(field=StringField)
    thumbnail = ImageField()


class Instruction(EmbeddedDocument):
    description = StringField()
    thumbnail = ImageField()

class Recipes(Document):
    title = StringField()
    description = StringField()
    thumbnail = ImageField()
    preparation_time = IntField()  # Minutes
    cooking_difficulty = StringField(choices=['Easy', 'Medium', 'Hard'])
    instructions = EmbeddedDocumentListField(Instruction)
    nutritional_values = ListField(field=DictField)  # Per Serving
    included_ingredients = ListField(field=DictField)
    excluded_ingredients = ListField(field=DictField)
    tags = ListField(field=StringField)
    utensils = ListField(field=StringField)
    reviews = ListField()
    week = IntField()
'''
'''
Wrapper classes to allow parsing Object IDs
'''


class MongoModel(BaseModel):

    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
            ObjectId: lambda oid: str(oid),
        }

    @classmethod
    def from_mongo(cls, data: dict):
        """We must convert _id into "id". """
        if not data:
            return data
        id = data.pop('_id', None)
        return cls(**dict(data, id=id))

    def to_mongo(self, **kwargs):
        exclude_unset = kwargs.pop('exclude_unset', True)
        by_alias = kwargs.pop('by_alias', True)

        parsed = self.dict(
            exclude_unset=exclude_unset,
            by_alias=by_alias,
            **kwargs,
        )

        # Mongo uses `_id` as default key. We should stick to that as well.
        if '_id' not in parsed and 'id' in parsed:
            parsed['_id'] = parsed.pop('id')

        return parsed


class RecipeDB(MongoModel):
    title: str
    week: int


class ManyRecipes(MongoModel):
    '''
    A model for returning multiple recipes
    '''
    recipes: List[RecipeDB]


class WeeklyMenu(MongoModel):
    week: int
    year: int
    recipes: List[RecipeDB]
