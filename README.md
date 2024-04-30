
# Referal System

It is a referal management system made by django rest framework.

## Installation

Run referal system by follwing commands

```bash
  docker-compose build
  docker-compose up
```

## Documentation

After running the project, swagger UI will be available in the
'/swagger/' end point

[Swagger UI ](http://localhost:8000/swagger/)


## Running The Testcases

To run the testcases, run the following command

```bash
  docker-compose run app python manage.py test users --keepdb
```
