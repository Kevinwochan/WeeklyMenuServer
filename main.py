import os
import asyncio
from typing import List
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.db.mongodb import MongoDB
from app.crud.RecipeRepository import RecipeRepository
from app.crud.MenuRepository import MenuRepository
from app.Models import WeeklyMenu
'''
Iniitalise the API app
'''
app = FastAPI()


@app.on_event("startup")
def startup():
    '''
    Prepare database access
    '''
    MongoDB.connect()


@app.on_event("shutdown")
def shutdown():
    '''
    Clean up application state before shutdown
    '''
    MongoDB.disconnect()


'''
Routes
'''


@app.get("/")
async def root():
    return ''


@app.get("/menu/", response_model=WeeklyMenu)
async def read_menu(year: int, week: int):
    '''
    Path to fetch the menu for a certain week
    '''
    weekly_menu = await MenuRepository.read_menu_by_year_week(MongoDB.get_collection('HelloFresh', 'Menus'), year, week)
    recipe_queries = []
    for recipe_id in weekly_menu['recipes']:
        query = RecipeRepository.read_recipe_by_id(MongoDB.get_collection, recipe_id)
        recipe_queries.append(query)
    recipe_documents = await asyncio.gather(*recipe_queries)
    print('===')
    print(recipe_documents)        
    return JSONResponse(content=jsonable_encoder(WeeklyMenu(recipes=[])))
