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

function show_help(){
    # show the help informations 
    #

    s_help="${1}"

    if [ $s_help ]; then 
        if [ ${s_help} = "user" ]; then
            # helper for the user
            #

            echo "Type the user name for the mysql user"
            exit 
        elif [ ${s_help} = "password" ]; then
            # helper for the password
            #

            echo "Type the passowrd value for the mysql user"
            exit
        fi
    else 
        echo -e "Database Initilize Help\n"
        echo -e "usage:\t\t\t ./database_initialise.sh [user] [password]\n"
        echo -e "user:\t\t\t mysql user name" 
        echo -e "password:\t\t mysql user password"
        exit
    fi     
}


# mysql -h 0.0.0.0 -P 5500 -u MainRoot --password="RootPassword" -e "CREATE DATABASE TournamentName"


HOST=0.0.0.0
PORT=5500
DATABASE=Tournament

if [ "$1" = "help" ]
then
    show_help "$2"

else
    # Tournament initilialization
    #
    #

    # Create tables and constrainsts
    #

    echo "Creating Tournament tables and constraints"
    mysql -h $HOST -P $PORT -u "$1" --password="$2" $DATABASE < ./database/tournament/main.sql
    
    exitcode=$?

    catching_errors $exitcode "Tournament Tables and Constraints Failed" "Tournament Tabled and Constraints Created Sucessfully"

    # Create procedures and triggers
    #

    echo "Creating procedures and triggers"
    mysql -h $HOST -P $PORT -u "$1" --password="$2" $DATABASE < ./database/tournament/procedures_triggers.sql
    
    exitcode=$?

    catching_errors $exitcode "Tournament Procedures and Triggers Failed" "Tournament Procedures and Triggers Created Sucessfully"
 
    # Insert main data on tournament
    #

    echo "Inserting Tournament initial data"
    mysql -h $HOST -P $PORT -u "$1" --password="$2" $DATABASE < ./database/tournament/queries/insert/main.sql

    exitcode=$?

    catching_errors $exitcode "Tournament Data Insertion Failed" "Tournament Data Inserted Sucessfully"


    # populate tournament database
    #

    echo "Populating Tournament Database"
    python ./configure.py

    exitcode=$?

    catching_errors $exitcode "Tournament Database Population Failed" "Tournament Database Populated Sucessfully"


    # NameGenerator initialization
    #
    #

    echo "Creating NameGenerator tables"
    mysql -h $HOST -P $PORT -u "$1" --password="$2" $DATABASE < ./NameGenerator/queries/main.sql
    
    exitcode=$?

    catching_errors $exitcode "Name Generator Tables failed" "Name Generator Tables Created sucesfully" 

    # populate Name Generator database
    #

    echo "Populating NameGenerator Database"
    python ./NameGenerator/configure.py 

    exitcode=$?

    catching_errors $exitcode "Name Generator DB Population Failed" "NameGenerator DB Populated Sucessfully"
fi




