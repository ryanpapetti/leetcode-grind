# Write your MySQL query statement below
SELECT employee1.name AS Employee
FROM Employee employee1, Employee employee2
WHERE employee1.salary > employee2.salary 
AND employee1.managerId=employee2.id