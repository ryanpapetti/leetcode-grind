# Write your MySQL query statement below
SELECT department.name AS Department, employee.name AS Employee, employee.salary as Salary 
FROM Employee 

LEFT JOIN Department ON Employee.departmentId=Department.id

WHERE (employee.departmentId, employee.salary) IN (SELECT departmentId, MAX(salary) FROM employee GROUP BY departmentId)

