SELECT t.fullname, s.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN students s  ON s.id = g.student_id
JOIN teachers t ON t.id = d.teacher_id
WHERE s.id = 1 AND t.id = 5;