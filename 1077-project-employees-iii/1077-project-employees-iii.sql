# Write your MySQL query statement below

# for each project get the maximum experience years 

# then find all employees in that project where the XP matches

WITH project_xp_max AS (SELECT project_id, MAX(Employee.experience_years) as max_xp FROM Project JOIN Employee ON Project.employee_id=Employee.employee_id GROUP BY project_id)

SELECT Project.project_id, Project.employee_id FROM Project JOIN  Employee ON Project.employee_id=Employee.employee_id JOIN project_xp_max ON project_xp_max.project_id=Project.project_id WHERE Employee.experience_years=project_xp_max.max_xp  