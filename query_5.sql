SELECT t.fullname, d.name
FROM disciplines d 
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 5
GROUP BY t.fullname, d.name;