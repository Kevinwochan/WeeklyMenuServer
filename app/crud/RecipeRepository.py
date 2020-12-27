from typing import List
from bson.objectid import ObjectId
from app.db.mongodb import MongoDB
from app.models.RequestModels import RecipeRequest
from app.models.DBModels import RecipeDB


class RecipeRepository():
    recipe_collection = MongoDB.get_collection('HelloFresh', 'Recipes')
    '''
    Provides access to the recipes collection
    '''
    @classmethod
    async def create_recipe(cls, new_recipe: RecipeRequest) -> str:
        recipe_doc = new_recipe.dict(exclude={'_id'})
        result = await cls.recipe_collection.insert_one(recipe_doc)
        if not result.acknowledged:
            # TODO:  define custom exception
            raise Exception('Database did not acknowledge')
        return str(result.inserted_id)

    @classmethod
    async def read_recipe_by_id(cls, recipe_id) -> RecipeDB:
        recipe_document = await cls.recipe_collection.find_one({"_id": recipe_id})
        if recipe_document is None:
            raise ValueError('Invalid Recipe ID')
        return RecipeDB.parse_obj(recipe_document)

    @classmethod
    async def update_recipe(cls, recipe_id: str, new_recipe: RecipeRequest) -> str:
        recipe_doc = new_recipe.dict(exclude={'_id', 'id'}, by_alias=True) 
        result = await cls.recipe_collection.replace_one({"_id": ObjectId(recipe_id)}, recipe_doc)
        if not result.acknowledged:
            # TODO:  define custom exception
            raise Exception('Database did not acknowledge')
        elif result.modified_count != 1:
            raise Exception('Document was not updated')
        return recipe_id

    @classmethod
    async def delete_recipe(cls, recipe_id: str):
        result = await cls.recipe_collection.delete_one({"_id": ObjectId(recipe_id)})
        if not result.acknowledged:
            # TODO:  define custom exception
            raise Exception('Database did not acknowledge')
        elif result.deleted_count != 1:
            raise Exception('Document was not deleted')
        return
