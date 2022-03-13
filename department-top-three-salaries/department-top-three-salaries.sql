# Write your MySQL query statement below

# partition by the departmentId
# rank ordered salaries by department id and add as a column
# if the rank column is less than 3, then 
# only have the department name (do last)


WITH rank_salaries AS (SELECT id, name, salary, departmentId, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) department_rank FROM Employee)

SELECT Department.name AS "Department", rank_salaries.name AS "Employee", salary AS "Salary" FROM rank_salaries JOIN Department ON rank_salaries.departmentId=Department.id WHERE department_rank < 4
# SELECT departmentId,name,salary,department_rank FROM rank_salaries