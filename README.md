# Base Django with Nginx and Postgres

This project is a base one with django running on docker with Nginx and Postgres as database.


### How to run

- Run on terminal ```make run```


## Versioning

- ```git checkout main && git pull```
- ```git merge --no-ff develop```
- ```git tag -a 0.0.0.0```
- ```git checkout develop && git merge --no-ff 0.0.0.0```
- ```git push origin develop main 0.0.0.0```


## Known Problems

- database don't persist between startups