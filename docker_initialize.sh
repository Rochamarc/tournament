#!/bin/bash

function catching_errors(){
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


# Create tables and constrainsts

echo "Creating Tournament tables and constraints"
mysql -u root --password=${MYSQL_ROOT_PASSWORD} ${MYSQL_DATABASE} < ./main.sql

exitcode=$?

catching_errors $exitcode "Tournament Tables and Constraints Failed" "Tournament Tabled and Constraints Created Sucessfully"

# Create procedures and triggers

echo "Creating procedures and triggers"
mysql -u root --password=${MYSQL_ROOT_PASSWORD} ${MYSQL_DATABASE} < ./procedures_triggers.sql

exitcode=$?

catching_errors $exitcode "Tournament Procedures and Triggers Failed" "Tournament Procedures and Triggers Created Sucessfully"

# Insert main data on tournament

echo "Inserting Tournament initial data"
mysql -u root --password=${MYSQL_ROOT_PASSWORD} ${MYSQL_DATABASE} < ./insert/main.sql

exitcode=$?

catching_errors $exitcode "Tournament Data Insertion Failed" "Tournament Data Inserted Sucessfully"





