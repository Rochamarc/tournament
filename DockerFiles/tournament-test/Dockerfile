FROM mysql:5.7

WORKDIR /database

COPY ./docker_initialize.sh .
COPY ./database/tournament_test/main.sql .
COPY ./database/tournament/procedures_triggers.sql . 
COPY ./database/tournament/queries/insert/main.sql ./insert/