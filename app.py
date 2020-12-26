import os
from typing import List
from json import dumps
from flask import Flask, request, jsonify, Response
from pymodm import connect

from DBModels import Menus
from ResponseModels import *

'''
Iniitalise the API app
'''
app = Flask(__name__)


def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response


app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.register_error_handler(Exception, defaultHandler)


@app.before_first_request
def connect_to_db():
    connect(f'mongodb+srv://{os.getenv('MONG0_USER')}:{os.getenv('MONGO_PASSWORD')}@cluster0.rhkkj.mongodb.net/HelloFresh?retryWrites=true&w=majority')


@app.route("/menu/add", methods=['POST'])
def create_menu():
    '''
    Creates a new menu
    '''
    week = int(request.form['week'])
    year = int(request.form['year'])
    recipes = []
    if 'recipes' in request.form:
        recipes = list(request.form['recipes'].split(','))
    Menus(WeekYear=f'W{week}-{year}', recipes=recipes).save()
    return jsonify({'success': True})


@app.route("/menu/<string:week_year>", methods=['GET'])
def read_menu(week_year):
    '''
    Path to fetch the menu for a certain week
    '''
    try:
        menu_document = Menus.objects.get({"_id": week_year})
    except Exception:
        raise ValueError('Invalid week or year, format is W<WEEK>-<YEAR> e.g W1-2020')

    menu_dict = menu_document.to_son().to_dict()
    menu_json = MenuResponse(**menu_dict).json()
    return Response(response=menu_json, content_type="application/json")



@app.route("/recipe/add", methods=['POST'])
def create_recipe():
    try:
        Recipes().save()
    except Exception:
        raise ValueError('Invalid week or year')
    return jsonify({'success': True})
