# Write your MySQL query statement below
WITH student_ranks AS (SELECT *, RANK() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id) AS student_rank FROM Enrollments)


SELECT student_id, course_id, grade FROM student_ranks WHERE student_rank=1
