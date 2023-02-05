#!/bin/sh

echo "Criando diretorios necessarios!"
mkdir files
mkdir files/names
echo "Criando e configurando base de dados!"
python3 database.py
