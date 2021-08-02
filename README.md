# basedbin

Simple REST pastebin-like service to put text files or images.

## Installing with Docker 

### Docker Compose

* Clone repo to your machine
* Edit `docker-compose.yml` file and set database credentials*
* Run `docker-compose up` command
* Go to `localhost:8080` (or any other port you set for `nginx` service)

\* As `DB_HOST` variable in `app` service you need to set database service name (by default: `db`)

### Standalone container

* Run `mongo` database in any way you want
* Clone repo to your machine
* Run container
```shell
$ docker run -d \
    -e DB_HOST=DB_HOST \
    -e DB_PORT=DB_PORT \
    -e DB_USER=DB_USER \
    -e DB_PASSWORD=DB_PASSWORD \
    --restart on-failure \
    --name basedbin \
    ghcr.io/samedamci/basedbin:latest
```

## Documentation

Go to `/docs` API endpoint for documentation.

## Other stuff

+ [basedbinpy](https://github.com/samedamci/basedbinpy) - simple Python client library 