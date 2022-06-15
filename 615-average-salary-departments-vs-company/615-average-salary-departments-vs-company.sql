# Write your MySQL query statement below
WITH company_average_month AS (SELECT DATE_FORMAT(pay_date,"%Y-%m") AS pay_month, AVG(amount) AS avg_salary FROM Salary GROUP BY DATE_FORMAT(pay_date,"%Y-%m"))

SELECT DATE_FORMAT(Salary.pay_date,"%Y-%m") AS pay_month, 
Employee.department_id, 
CASE 
WHEN ROUND(AVG(Salary.amount),2) > ROUND(company_average_month.avg_salary,2) THEN "higher" 
WHEN ROUND(AVG(Salary.amount),2) = ROUND(company_average_month.avg_salary,2) THEN "same" 
ELSE "lower" END AS comparison
FROM Salary 
INNER JOIN Employee on Salary.employee_id = Employee.employee_id 
INNER JOIN company_average_month ON company_average_month.pay_month=DATE_FORMAT(Salary.pay_date,"%Y-%m") 
GROUP BY DATE_FORMAT(pay_date,"%Y-%m"), department_id 




# SELECT DATE_FORMAT(Salary.pay_date,"%Y-%m") AS pay_month, 
# Employee.department_id, 

# AVG(Salary.amount), company_average_month.avg_salary
# FROM Salary 
# INNER JOIN Employee on Salary.employee_id = Employee.employee_id 
# INNER JOIN company_average_month ON company_average_month.pay_month=DATE_FORMAT(Salary.pay_date,"%Y-%m") 
# GROUP BY DATE_FORMAT(pay_date,"%Y-%m"), department_id ORDER BY DATE_FORMAT(pay_date,"%Y-%m") 