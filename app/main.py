import os
import asyncio
from bson import ObjectId
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.db.mongodb import MongoDB
from app.crud.RecipeRepository import RecipeRepository
from app.models.RequestModels import RecipeRequest
from app.models.ResponseModels import SaveResponse, RecipeResponse


'''
Iniitalise the API app
'''
app = FastAPI()



@app.on_event("shutdown")
def shutdown():
    '''
    Clean up application state before shutdown
    '''
    MongoDB.disconnect()


'''
Routes
'''

@app.post("/recipe/add", response_model=SaveResponse)
async def create_recipe(recipe: RecipeRequest):
    '''
    Path to fetch the menu for a certain week
    '''
    try:
        new_recipe_id = await RecipeRepository.create_recipe(recipe)
    except Exception as e:
        return SaveResponse(success=False, message=str(e), id=None)
    return SaveResponse(success=True, message='', id=new_recipe_id)


@app.get("/recipe/{recipe_id}", response_model=RecipeResponse)
async def get_recipe(recipe_id: str):
    '''
    Provides a client with the recipe specified by a recipe id
    '''
    try:
        recipe_id = ObjectId(recipe_id)
    except:
         raise HTTPException(status_code=400, detail='recipe id was not a valid object id')
    try:
        recipe_doc = await RecipeRepository.read_recipe_by_id(recipe_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return RecipeResponse.parse_obj(recipe_doc.dict())
    
@app.put("/recipe/edit/{recipe_id}", response_model=SaveResponse)
async def update_recipe(recipe_id: str, new_recipe: RecipeRequest):
    '''
    Updates an existing recipe specified by a recipe id
    '''
    try:
        recipe_id = await RecipeRepository.update_recipe(recipe_id, new_recipe)
        return SaveResponse(success=True, message='', id=recipe_id)
    except Exception as e:
        return SaveResponse(success=False, message=str(e), id='')

@app.delete("/recipe/delete/{recipe_id}", response_model=SaveResponse)
async def delete_recipe(recipe_id: str):
    '''
    Deletes an existing recipe specified by a recipe id
    '''
    try:
        recipe_id = await RecipeRepository.delete_recipe(recipe_id)
        return SaveResponse(success=True, message='', id='')
    except Exception as e:
        return SaveResponse(success=False, message=str(e), id='')