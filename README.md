## Dockerized Django+React starter project

### Requirements
* [Docker Engine](https://docs.docker.com/engine/installation)
* [Docker Compose](https://docs.docker.com/compose/install)

### Stack
* Postgres
* Django + Django Rest Framework
* Webpack + React + Stylus
* Mocha + Chai for js testing
* Pytest for python testing

### Setup

```
git remote add seed https://github.com/elielagmay/docker-django-react-seed.git
git pull seed master
```

Edit the environement variables in `env/dev` then build and start the docker containers:

```
./bin/develop
```

### Run Django commands

```
./bin/django [command]
./bin/django createsuperuser
./bin/django makemigrations [app_name]
```

### Todo
* Dockerized deployment
* Dockerized testing
