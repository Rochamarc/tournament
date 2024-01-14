SELECT 	c.id,
		c.name,
		cc.name 
FROM clubs c
INNER JOIN club_classes cc 
	ON c.club_class_id = cc.id;