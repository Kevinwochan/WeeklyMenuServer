from typing import List
from crud.RecipeRepository import RecipeRepository


class MenuRepository():
    '''
    Provides access to the recipes collection
    '''
    @staticmethod
    def create_recipe(new_recipe):
        pass

    @staticmethod
    async def read_menu_by_year_week(menu_collection, year: int, week: int):
        menu = await menu_collection.find_one({"week": week, "year": year}, limit=30)
        return menu

    def update_recipe(self):
        pass

    def delete_recipe(self, recipe):
        pass
