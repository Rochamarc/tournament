#!/bin/sh

echo "Criando diretorios necessarios!"
mkdir files
mkdir files/saves
mkdir files/names
mkdir files/brasileirao/serie\ a/2021
mkdir files/brasileirao/serie\ b/2021
mkdir files/brasileirao/serie\ c/2021
echo "Criando e configurando base de dados!"
python3 database.py
