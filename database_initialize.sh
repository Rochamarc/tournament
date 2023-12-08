echo "Inserting tables and constraints"
mysql -h localhost -u tournament_user -p tournament < ./db/queries/main.sql
echo "Insert initial data"
mysql -h localhost -u tournament_user -p tournament < ./db/queries/insert/main.sql