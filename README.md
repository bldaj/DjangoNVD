# DjangoNVD

## Running server
### Requirements
For running server you have to install [docker](https://www.docker.com/).

### Launch
To start server all you need is type:

```bash
$ docker-compose up -d
```

## Running tasks
### Launch
To run tasks outside docker just type:

```bash
$ celery -A NVD worker -B -l INFO
```