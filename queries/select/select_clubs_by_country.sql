SELECT clubs.id, clubs.name, clubs.country, clubs.class, clubs.total_budget, clubs.salary_budget 
FROM clubs 
WHERE clubs.country = %s;