# Extract the content from the main database
mysqldump -h 0.0.0.0 -P 5500 -u MainUser -p --no-tablespaces Tournament > dump_file.sql

# Copy the content to the database
mysql -h 0.0.0.0 -P 5502 -u MainUser -p TournamentTest < dump_file.sql