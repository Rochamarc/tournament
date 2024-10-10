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


echo "Creating NameGenerator Tables"
mysql -u root --password=${MYSQL_ROOT_PASSWORD} ${MYSQL_DATABASE} < ./main.sql

exitcode=$?

catching_errors $exitcode "NameGenerator Tables Creation Failed" "NameGenerator Tables Created Sucessfully"



