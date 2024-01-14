select 	champions.season,
		divisions.name,
		competitions.name,
		clubs.name 
from champions
inner join divisions ON champions.division_id = divisions.id
inner join competitions on divisions.competition_id = competitions.id 
inner join clubs on champions.club_id = clubs.id 
order by (divisions.name);