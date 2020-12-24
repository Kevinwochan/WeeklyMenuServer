from typing import List
from app.crud.RecipeRepository import RecipeRepository
from app.Models import WeeklyMenu, RecipeDB


class MenuRepository():
    '''
    Provides access to the recipes collection
    '''
    @staticmethod
    def create_recipe(new_recipe):
        pass

    @staticmethod
    async def read_menu_by_year_week(menu_collection, year: int, week: int) -> WeeklyMenu:
        menu = await menu_collection.find_one({"week": week, "year": year}, limit=30)
        print('='*20)
        print(menu)
        print(type(menu))

        return WeeklyMenu.from_mongo(menu)

    def update_recipe(self):
        pass

    def delete_recipe(self, recipe):
        pass
