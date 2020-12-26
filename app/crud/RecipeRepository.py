from typing import List
from bson.objectid import ObjectId
from app.models.RequestModels import RecipeRequest
from app.models.DBModels import RecipeDB


class RecipeRepository():
    '''
    Provides access to the recipes collection
    '''
    @staticmethod
    async def create_recipe(recipe_collection, new_recipe: RecipeRequest) -> str:
        recipe_doc = new_recipe.dict(exclude={'_id'})
        print(recipe_doc)
        result = await recipe_collection.insert_one(recipe_doc)
        if not result.acknowledged:
            raise Exception('Database did not acknowledge') # TODO:  define custom exception
        return str(result.inserted_id)

    @staticmethod
    async def read_recipe_by_id(recipe_collection, recipe_id) -> RecipeDB:
        recipe_document = await recipe_collection.find_one({"_id": ObjectId(recipe_id)}, limit=30)
        if recipe_document is None:
            raise ValueError('Invalid Recipe ID')
        print('='*30)
        print(recipe_document)      
        print('='*30)  
        return RecipeDB(**recipe_document)

    def update_recipe(self):
        pass

    def delete_recipe(self, recipe):
        pass
