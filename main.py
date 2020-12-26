import os
import asyncio
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.db.mongodb import MongoDB
from app.crud.RecipeRepository import RecipeRepository
from app.crud.MenuRepository import MenuRepository
from app.models import RequestModels
from app.models import ResponseModels

import sys
sys.path.insert(0,'/home/ubuntu/WeeklyMenuServer')


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

@app.post("/recipe/add", response_model=ResponseModels.SaveResponse)
async def create_recipe(recipe: RequestModels.RecipeRequest):
    '''
    Path to fetch the menu for a certain week
    '''
    try:
        new_recipe_id = RecipeRepository.create_recipe(MongoDB.get_collection('HelloFresh', 'Recipes'), recipe)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return ResponseModels.SaveResponse(success=True, message='', id=await new_recipe_id)


@app.get("/recipe/", response_model=ResponseModels.RecipeResponse)
async def get_recipe(recipe_id: str):
    '''
    Path to fetch a recipe specified by id
    '''
    try:
        recipe_doc = RecipeRepository.read_recipe_by_id(MongoDB.get_collection('HelloFresh', 'Recipes'), recipe_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return ResponseModels.RecipeResponse.parse_obj((await recipe_doc).dict())
    
