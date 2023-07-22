#!/bin/bash
#!/bin/sh
    
rm -r db/database.db 
python db/database.py $1
