from typing import List
from bson.objectid import ObjectId
from app.Models import RecipeDB, ManyRecipes


class RecipeRepository():
    '''
    Provides access to the recipes collection
    '''
    @staticmethod
    def create_recipe(new_recipe):
        pass

    @staticmethod
    async def read_recipe_by_id(recipe_collection, recipe_id) -> RecipeDB:
        recipe_document = recipe_collection.find_one({"_id": ObjectId(recipe_id)}, limit=30)
        return RecipeDB(**recipe_document)

    def update_recipe(self):
        pass

    def delete_recipe(self, recipe):
        pass
