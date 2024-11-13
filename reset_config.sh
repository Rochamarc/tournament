# Start composing the docker 

echo "Droping containers" && \
docker compose down && \ 
sleep 2 && \
echo "Creating containers" && \
docker compose up -d && \
echo "Waiting for the database configuration..." && \
sleep 30 && \
./exec_docker_initialize.sh && \
echo "Configuring Name Generator" && \
python NameGenerator/configure.py && \
echo "First insert into main database" && \
python championships_configuration.py
echo "Configuring Tournament" && \
python configure.py