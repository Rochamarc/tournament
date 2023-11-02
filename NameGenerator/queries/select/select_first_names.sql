SELECT  first_names.value
        first_names.nationality
FROM first_names
WHERE first_names.nationality = %s;