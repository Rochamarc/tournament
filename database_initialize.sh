#!/bin/bash

#   if [ $exitcode -ne 0 ]; then 
#       echo "Error on Name Generator databse creation"
#       exit
#   else 
#       echo "Name Generator Database Created Sucessfully"
#   fi 

function catching_errors(){
    # $1 exitcode, $2 error_message $3sucess_message
    exitcode="${1}"
    error_message="${2}"
    sucess_message="${3}"


    if [ ${exitcode} -ne 0 ]; then
        # this is the error, and exiting the code
        echo $error_message
        exit
    else
        # sucess just show the message and pass to next step
        echo $sucess_message
    fi
}


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
    # NameGenerator initialization
    #
    #

    echo "Creating NameGenerator database"
    mysql -u "$1" --password="$2" -e "create database tournament_name";
    
    # return of the code
    exitcode=$?

    # testing if the code is sucessfull
    catching_errors $exitcode "Name Generator DB failed" "Name Generator DB Created Sucessfully"

    # Creating tables
    #

    echo "Creating NameGenerator tables"
    mysql -h localhost -u "$1" --password="$2" tournament_name < ./NameGenerator/queries/main.sql
    
    exitcode=$?

    catching_errors $exitcode "Name Generator Tables failed" "Name Generator Tables Created sucesfully" 

    # populate Name Generator database
    #

    echo "Populating NameGenerator Database"
    python ./NameGenerator/configure.py 

    exitcode=$?

    catching_errors $exitcode "Name Generator DB Population Failed" "NameGenerator DB Populated Sucessfully"


    # Tournament initilialization
    #
    #


    # Create database
    #

    echo "Creating Tournament database"
    mysql -u "$1" --password="$2" -e "create database tournament";

    exitcode=$?

    catching_errors $exitcode "Tournament DB failed" "Tournament DB Created Sucessfully"

    # Create tables and constrainsts
    #

    echo "Creating Tournament tables and constraints"
    mysql -h localhost -u "$1" --password="$2" tournament < ./db/queries/main.sql
    
    exitcode=$?

    catching_errors $exitcode "Tournament Tables and Constraints Failed" "Tournament Tabled and Constraints Created Sucessfully"

    # Create procedures and triggers
    #

    echo "Creating procedures and triggers"
    mysql -h localhost -u "$1" --password="$2" tournament < ./db/queries/procedures_triggers.sql
    
    exitcode=$?

    catching_errors $exitcode "Tournament Procedures and Triggers Failed" "Tournament Procedures and Triggers Created Sucessfully"
 
    # Insert main data on tournament
    #

    echo "Inserting Tournament initial data"
    mysql -h localhost -u "$1" --password="$2" tournament < ./db/queries/insert/main.sql

    exitcode=$?

    catching_errors $exitcode "Tournament Data Insertion Failed" "Tournament Data Inserted Sucessfully"


    # populate tournament database
    #

    echo "Populating Tournament Database"
    python ./configure.py

    exitcode=$?

    catching_errors $exitcode "Tournament Database Population Failed" "Tournament Database Populated Sucessfully"
fi




