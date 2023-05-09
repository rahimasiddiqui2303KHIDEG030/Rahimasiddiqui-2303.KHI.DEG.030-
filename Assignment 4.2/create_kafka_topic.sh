#!/bin/bash

docker-compose exec broker kafka-topics --create --topic Class-activity-event-0 --bootstrap-server broker:9092 

docker-compose exec broker kafka-topics --create --topic Class-activity-event-1 --bootstrap-server broker:9092 --partitions 2

docker-compose exec broker kafka-topics --create --topic Class-activity-event-2 --bootstrap-server broker:9092 --partitions 3

docker-compose exec broker kafka-topics --create --topic Class-activity-event-3 --bootstrap-server broker:9092 --partitions 5

docker compose exec broker kafka-topics --list --bootstrap-server broker:9092

docker compose exec broker kafka-topics --describe --bootstrap-server broker:9092

docker compose exec broker kafka-topics --topic Class-activity-event-3 --describe --bootstrap-server broker:9092


