# Write your MySQL query statement below

SELECT table2.id
FROM Weather table1 INNER JOIN Weather table2 ON DATEDIFF(table2.recordDate,table1.recordDate)=1
WHERE table2.temperature > table1.temperature 
