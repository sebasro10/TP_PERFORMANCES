# TP PERFORMANCES

**Author**: Sebastian Romero <sebastian.romero@imt-atlantique.net>

Project directories:

* `/movie_graphql`: movie service with GraphQL protocol
* `/movie_grpc`: movie service with Grpc protocol
* `/movie_rest`: movie service with Rest protocol
* `/tests_performance`: files for testing performance

## Requirements

Install `locust` (https://docs.locust.io/en/1.5.2/installation.html):
```bash
pip3 install locust
```

Install `grpc` (https://grpc.io/docs/languages/python/quickstart/):
```bash
pip install grpcio
pip install grpcio-tools
```

## Run microservices

Build or rebuild services
```bash
make docker-compose-build
```

Create and start containers
```bash
make docker-compose-up
```

Stop and remove containers, networks
```bash
make docker-compose-down
```

## Run locust for testing performance

Depending on the protocol you want to test, you can execute one of the commands below.

> After run a command:
> * Go to the url http://localhost:8089
> * If you want, you can modify the parameters
> * Click on `start swarming`

### Comparison between GraphQL, Grpc and Rest

These commands allow testing the same methods for each protocol:

```bash
make tests-graphql
```

```bash
make tests-grpc
```

```bash
make tests-rest
```

### Comparison between GraphQL and Rest

In this case we compare GraphQL and Rest, but with the following case:

* Only the title of the film is required in the response.

GraphQL allows you to request only this information, but with Rest, you need to request all the information.

```bash
make tests-graphql2
```

```bash
make tests-rest2
```
