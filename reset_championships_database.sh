#!/bin/sh
#!/bin/bash

echo "Reseting championships database"
mysql -h localhost -u "$1" --password="$2" tournament < ./db/queries/reset_championships.sql