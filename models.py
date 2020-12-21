from mongoengine import *


class Ingredient():
    name = StringField()
    units = StringField()
    allergens = ListField(field=StringField)
    thumbnail = ImageField()


class Instruction(EmbeddedDocument):
    description = StringField()
    thumbnail = ImageField()

class Recipe(Document):
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


class WeeklyMenu(Document):
    week = IntField()
    year = IntField()
    recipes = ListField(field=ReferenceField(Recipe))
