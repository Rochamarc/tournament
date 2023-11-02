SELECT  first_names.value,
        last_names.value
FROM first_names, last_names
    WHERE first_names.nationality = %s
    AND last_names.nationality = %s 
ORDER BY RAND() LIMIT 1;