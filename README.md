# Base Django with Nginx and Postgres

This project is a base one with django running on docker with Nginx and Postgres as database.


## How to run

- Run on terminal ```make run```

### To run in develop and use linting on the fly

- First create a file ```.env``` that is based of ```.env.template```
- Create a virtualenv using the pipenv, to install it:
    - ```pip install --user pipenv```
    - ```pipenv install``` to install all packages needed
    - ```pipenv shell``` to activate the virtual environment
- To let vscode handle the linting for django and python you must select the right python interpreter, press ```ctrl + shift + p``` search for ```Python:Select Interpreter``` and select the one with ```PipEnv``` on it, should have the name of the project in it.

If changed any version or librarie to ```Pipefile``` or ```Pipefile.lock``` the ```requirements.txt``` must be updated, just run:
- ```pipenv run pip freeze > ./backend/requirements.txt```


## Versioning

- ```git checkout main && git pull```
- ```git merge --no-ff develop```
- ```git tag -a 0.0.0.0```
- ```git checkout develop && git merge --no-ff 0.0.0.0```
- ```git push origin develop main 0.0.0.0```

## Known Problems

- ~~database don't persist between startups~~
- can't create an admin by command createsuperuser

## Things todo

- Different settings for local and production
- Different docker-compose for local and production
- Configure django-restframework
- Configure django-allauth and add google login

# Rules to pull request and help developing

- Always commit on branch develop develop
- Pull request will only be reviewed on branch develop
- Commits must follow the community standarts