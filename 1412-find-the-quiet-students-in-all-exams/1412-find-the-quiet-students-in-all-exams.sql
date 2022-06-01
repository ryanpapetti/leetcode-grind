# Write your MySQL query statement below
WITH exam_score_ranks AS (SELECT Exam.*, RANK() OVER (PARTITION BY exam_id ORDER BY score) AS asc_rank, RANK() OVER (PARTITION BY exam_id ORDER BY score DESC) AS desc_rank FROM Exam),

student_exam_counts AS (SELECT student_id, COUNT(exam_id) AS exam_count, SUM(CASE WHEN asc_rank>1 AND desc_rank>1 THEN 1 ELSE 0 END ) AS quiet_exam_count FROM exam_score_ranks GROUP BY student_id)


# SELECT * FROM exam_score_ranks WHERE exam_score_ranks.asc_rank>1 AND exam_score_ranks.desc_rank>1



# SELECT * FROM student_exam_counts

SELECT student_exam_counts.student_id, Student.student_name 
FROM student_exam_counts 
JOIN Student ON student_exam_counts.student_id=Student.student_id WHERE student_exam_counts.exam_count=student_exam_counts.quiet_exam_count 