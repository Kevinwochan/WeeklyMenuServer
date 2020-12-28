# NOTE: This project is largely incomplete
I fell into a rabbit hole of trying to get an async API working with FastAPI and Motor (an async mongo client). Mongo's "_id" field and ObjectId type did not playing nice.

# Installation
Run `pipenv install` or `pip install -r requirements.txt` depending on your preference

# Usage
## Pipenv
After installing run `pipenv run flask run`
This by default is launched in development mode due to the FLASK_ENV environment variable

## Other
After installing run `flask run`

# API Architecture
## app
- This folder is supposed to contain most of the code.
- By having the code all in this only config files and documentation would be at the top level

### models
- There are two sets of models: DBModels.pu and ResponseModels.py
- DBModels define the mapping from Mongo Documents to python data structures
- ResponseModels define the JSON response structure


## data
- This folder holds useful JSON data that may be useful for testing

## scripts
- This folder holds useful scripts to runs portions of this repo
- 
---
| script          | description                                                                                                                                      | progress    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| deploy.sh       | this script was planned to pull a dockerfile and launch the API in a docker container                                                            | incomplete  |
| develop.sh      | this script was planned to launch all the necessary programs for hot-loading                                                                      | in progress |
---

## Considerations
### Repository Design Pattern
The Repository design pattern abstracts away the database implementation and defines an database independent interface 

### Async vs Synchronous
When working with APIs built synchronously a large portion of the response time can be taken up by the API server waiting for the query response from the database server.

During this waiting period for the database to return the query result, an asynchronous API would be able to continue the program until the query result is needed. This saves small amounts of time when performing a single query but when an endpoint request requires multiple queries to be made at the exact same time, these queries can be parallelized using async.

# Database Architecture
## Weekly Menu Model
The weekly menu could be stored as inside a Recipe Document but would require the entire recipe collection to be scanned.
A separate Menu collection is useful for allowing efficient queries for the desired recipes and allows recipes to be re-used by multiple weeks.

## Ingredients Model
Ingredients were specified as a new embedded document so that editing a single ingredient will edit the ingredient in all recipes.
This is important if a change in manufacturing process of the ingredient results in a possible allergen being added to the ingredient. TYhe allergens must then be updated accross all recipes to reflect the potential hazard.
