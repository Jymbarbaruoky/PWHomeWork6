SELECT s.fullname, g.grade, g.date_of 
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN students s  ON s.id = g.student_id
JOIN "groups" gr ON gr.id  = s.group_id
WHERE gr.id = 3 AND d.id = 2 AND g.date_of IN (SELECT MAX(g.date_of) AS last_day
	FROM grades g
	JOIN disciplines d ON d.id = g.discipline_id
	JOIN students s  ON s.id = g.student_id
	JOIN "groups" gr ON gr.id  = s.group_id
	WHERE gr.id = 3 AND d.id = 2)
GROUP BY s.fullname;

