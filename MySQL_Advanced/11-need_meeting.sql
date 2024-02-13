-- SQL script that creates need_meeting that lists all students < %80
-- and no last_meeting for more than 1 month
CREATE VIEW need_meeting AS
SELECT name 
FROM students 
WHERE score < 80 
AND (last_meeting IS NULL OR last_meeting <= CURDATE() - INTERVAL 1 MONTH);