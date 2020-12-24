'''
Object Document Model (ODM) using PyMODM 
'''
from typing import List
from pymodm import EmbeddedMongoModel, MongoModel, fields

class Ingredient(MongoModel):
    '''
    Represents an ingredient
    '''
    name = fields.CharField()
    units = fields.CharField()
    allergens = fields.ListField()
    thumbnail = fields.ImageField()


class Instruction(EmbeddedMongoModel):
    '''
    Represents an instruction of a recipe
    '''
    description = fields.CharField()
    thumbnail = fields.ImageField()

class Recipes(MongoModel):
    '''
    Represents a recipe
    '''
    title = fields.CharField()
    description = fields.CharField()
    thumbnail = fields.ImageField()
    preparation_time = fields.IntegerField()  # Minutes
    cooking_difficulty = fields.CharField(choices=['Easy', 'Medium', 'Hard'])
    instructions = fields.ListField()
    nutritional_values = fields.ListField()  # Per Serving
    included_ingredients = fields.ListField()
    excluded_ingredients = fields.ListField()
    tags = fields.ListField()
    utensils = fields.ListField()
    reviews = fields.ListField()
    week = fields.IntegerField()

class Menus(MongoModel):
    '''
    Represents the weekly menu
    '''
    WeekYear = fields.CharField(primary_key=True)
    recipes = fields.ListField(field=fields.ReferenceField(Recipes))
