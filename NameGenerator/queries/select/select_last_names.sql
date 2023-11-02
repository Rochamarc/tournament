SELECT  last_names.value
        last_names.nationality
FROM last_names
WHERE last_names.nationality = %s;