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

### Setup and customize

```
git remote add seed https://github.com/elielagmay/docker-django-react-seed.git
git pull seed master
cp server/web/settings/local.py.example server/web/settings/local.py
```

1. Edit the environement variables in `env/dev`
2. Add additional Django settings in `server/web/settings/local.py`
3. Update the Django User model in `server/api/account/models.py`

Finally, build and start the docker containers:

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
