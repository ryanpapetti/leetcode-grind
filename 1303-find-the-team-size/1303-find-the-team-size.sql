# Write your MySQL query statement below

WITH team_sizes AS (SELECT team_id, COUNT(team_id) AS team_size FROM Employee GROUP BY team_id) 

SELECT employee_id, team_size FROM Employee, team_sizes WHERE Employee.team_id = team_sizes.team_id