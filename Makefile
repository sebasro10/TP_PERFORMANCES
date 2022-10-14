# Commands docker-compose
docker-compose-build:
	docker-compose build

docker-compose-up:
	docker-compose up -d

docker-compose-down:
	docker-compose down

# Run locust for testing performance
tests-graphql:
	locust -f tests_performance/locustfile_graphql.py -H http://localhost:5001

tests-graphql2:
	locust -f tests_performance/locustfile_graphql2.py -H http://localhost:5001

tests-grpc:
	locust -f tests_performance/locustfile_grpc.py

tests-rest:
	locust -f tests_performance/locustfile_rest.py -H http://localhost:5003

tests-rest2:
	locust -f tests_performance/locustfile_rest2.py -H http://localhost:5003
