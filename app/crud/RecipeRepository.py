from typing import List
from bson.objectid import ObjectId
from app.db.mongodb import MongoDB
from app.models.RequestModels import RecipeRequest
from app.models.DBModels import RecipeDB

class RecipeRepository():
    '''
    Provides access to the recipes collection
    '''
    @staticmethod
    async def create_recipe(new_recipe: RecipeRequest) -> str:
        recipe_collection = MongoDB.get_collection('HelloFresh', 'Recipes')
        recipe_doc = new_recipe.dict(exclude={'_id'})
        result = await recipe_collection.insert_one(recipe_doc)
        if not result.acknowledged:
            raise Exception('Database did not acknowledge') # TODO:  define custom exception
        return str(result.inserted_id)

    @staticmethod
    async def read_recipe_by_id(recipe_id) -> RecipeDB:
        recipe_collection = MongoDB.get_collection('HelloFresh', 'Recipes')
        recipe_document = await recipe_collection.find_one({"_id": recipe_id})
        if recipe_document is None:
            raise ValueError('Invalid Recipe ID')
        return RecipeDB.parse_obj(recipe_document)

    @staticmethod
    async def update_recipe(new_recipe: RecipeRequest) -> str:
        recipe_collection = MongoDB.get_collection('HelloFresh', 'Recipes')
        recipe_doc = new_recipe.dict(exclude={'_id'}, by_alias=True)
        print('='*100)
        print(recipe_doc)
        result = await recipe_collection.replace_one({"_id": ObjectId(new_recipe.id)}, recipe_doc)
        if not result.acknowledged:
            raise Exception('Database did not acknowledge') # TODO:  define custom exception
        elif result.upsert_id is None:
            raise Exception('Document was not updated')
        return str(result.upsert_id)


    def delete_recipe(self, recipe):
        pass
