FROM mysql:5.7

WORKDIR /database

COPY ./docker_initialize.sh .
COPY ./database/tournament_analysis/main.sql .
COPY ./database/tournament/procedures_triggers.sql . 