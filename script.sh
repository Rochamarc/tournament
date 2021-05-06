#!/bin/sh

echo "Criando diretorios necessarios!"
mkdir files
mkdir files/saves
mkdir files/names
echo "Criando e configurando base de dados!"
python3 database.py
python3 stadium.py
