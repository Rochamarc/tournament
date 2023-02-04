#!/bin/bash
#!/bin/sh
    
echo "Reseting database"
rm -r database.db 
echo "Recreating Base Database"
python3 database.py $1
echo "Recretating International Database"
python3 setting_international_clubs.py 
