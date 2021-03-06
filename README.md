# WeeklyMenuServer
**NOTE:** For database credetials please contact me, credentials in version control are not valid

Don't worry about credentials. I spent my spare time leading up to Christmas trying to complete this technical test. Only for my interviewers to not look at this.

I appreciate you doing your research by looking at this repo. Please contact me. I want to work with people who enjoy and put effort into their work.

## Summary

| Task                   | Progress         |
| ---------------------- | ---------------- |
| Recipe Model           | Completed        |
| Review Model           | Incomplete       |
| Weekly Menu Model      | Incomplete       |
| Ingredients Menu Model | Incomplete       |
| User Authentication    | Incomplete       |
| Unit Testing           | Incomplete       |
| E2E Testing            | Only for recipes |
| Docker                 | Completed        |

## Development
### Installation
Run `pipenv install --dev` depending on your preference

### Usage
To start the API server run the script `pipenv run sh scripts/develop.sh`

Documentation of the API should now be available at `http://127.0.0.1:8000/docs`

A valid recipe can be viewed at `http://127.0.0.1/recipe/5fe749674d685d341ce08e63`

## Deployment
## API Documentation
After running the server, go to  for interactive documentation on the API's expected parameters and returns

## Problem Statement
A menu planning API which allows management of the weekly menu and associated recipies. 

### Context
- A [weekly menu](https://www.hellofresh.com.au/plans/) contains a set of [recipies](https://www.hellofresh.com.au/recipes/). Each week different set of recipies are selected. See example [menu for this week](https://www.hellofresh.com.au/plans/).
- A [recipe](https://www.hellofresh.com.au/recipes/beef-veggie-ragu-spaghetti-5fa9c324cb8f8c0b3a183d01) contains ingredients, step-by-step instructions, nutirtional information, classification, and other metadata. See examples recipes here [1](https://www.hellofresh.com.au/recipes/southeast-asian-chicken-coconut-soup-5fa9c26209c8db59115d3f4f), [2](https://www.hellofresh.com.au/recipes/saucy-coconut-chicken-noodles-5f9b3c7198ecf4455b27d94d), [3](https://www.hellofresh.com.au/recipes/dukkah-roasted-sweet-potato-5f9b43847aacaa50f037d858).
- A customer can review weekly menu as well as recipe by assigning ratings and/or adding comments.

#### Tasks

1. Create data models using your selected ORM for weekly menu, recipe, ingredients, review, etc. Make sure these data models are appripriately connected using `FK`, `1:M`, `M:M ` relationships.
2. Create REST APIs to create, list, read, update, delete data model objects. Bonus if you can secure API using API tokens (recommended) or JWT tokens. You can use Google Authentication to obtain JWT token.
3. Create unit and E2E tests. For E2E API tests you can use [Postman](https://www.postman.com/) but ensure Postman collection are commited to your repository. For unit tests use a framework acccording to your stack.
4. Make sure your tests can be run from a single command - create test runner `makefile` or `bash` script to run your tests.


### Recommended Technology Stack
Choose the one you are most familiar. 

- Python 3, Flask as web framework, PeeWee as ORM, Docker as Container, PostgreSQL as a database, Pytest for unit test, Postman for API test
- Python 3, Flask as web framework, Flask-PyMongo as ORM, Docker as Container, MongoDB as a database, Pytest for unit test, Postman for API test
- Go, chi or beego as web framework, sqlx or beego as ORM, Docker as Container, PostgreSQL as a database, go testing package, Postman for API test

