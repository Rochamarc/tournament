#!/bin/sh
#!/bin/bash

# Name generator initialization
#
#


if [ "$1" = "help" ]
then
    echo "Database Initilize Help"
    echo "usage: ./database_initialise.sh [user] [password]"
    echo "user\t\t\t: mysql user name" 
    echo "password\t\t: mysql user password"
    exit
else
    echo "Creating NameGenerator database"
    mysql -u "$1" --password="$2" -e "create database tournament_name";
    echo "Name Generator Database created sucessfully"

    echo "Creating NameGenerator tables"
    mysql -h localhost -u "$1" --password="$2" tournament_name < ./NameGenerator/queries/main.sql
    echo "Name Generator Tables created sucesfully"

    # populate Name Generator database
    echo "Populating NameGenerator Database"
    python ./NameGenerator/configure.py
    echo "NameGenerator Database populated sucessfully"


    # Tournament initilialization
    #
    #


    echo "Creating Tournament database"
    mysql -u "$1" --password="$2" -e "create database tournament";
    echo "Tournament Database created sucessfully"

    echo "Creating Tournament tables and constraints"
    mysql -h localhost -u "$1" --password="$2" tournament < ./db/queries/main.sql
    echo "Tournament tables and constraints created sucessfully"

    echo "Inserting Tournament initial data"
    mysql -h localhost -u "$1" --password="$2" tournament < ./db/queries/insert/main.sql
    echo "Tournament data inserted sucessfully"


    # populate tournament database
    echo "Populating Tournament Database"
    python ./configure.py
    echo "Tournament Database populated sucessfully"
fi




