FROM mysql:5.7

COPY ./database/tournament/main.sql/ /docker-entrypoint-initd.d/
COPY ./database/tournament/procedures_triggers.sql/ /docker-entrypoint-initd.d/