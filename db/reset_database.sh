#!/bin/bash
#!/bin/sh
    
echo "Reseting database"
rm -r db/database.db 
echo "Recreating Base Database"
python db/database.py $1
echo "Recretating International Database"
python setting_international_clubs.py 
