# Write your MySQL query statement below

WITH direct_report_counts AS (SELECT managerId, COUNT(managerId) AS dr_count FROM Employee GROUP BY managerId HAVING dr_count > 4)

SELECT name FROM Employee JOIN direct_report_counts ON Employee.id=direct_report_counts.managerId