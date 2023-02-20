SELECT g.name, s.fullname
FROM students s
LEFT JOIN groups g ON g.id = s.group_id
GROUP BY g.name , s.fullname;