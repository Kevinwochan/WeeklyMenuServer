'''
Object Document Model (ODM) using PyMODM 

PyMODM defines the structure from the database
'''
from typing import List
from pydantic import Field, BaseModel

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


class Recipe(BaseModel):
    title: str = Field()


class MenuResponse(BaseModel):
    WeekYear: str = Field(alias='_id')
    recipes: List = []
