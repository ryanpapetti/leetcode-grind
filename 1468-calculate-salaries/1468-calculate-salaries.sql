# Write your MySQL query statement below

# find the max salary per company (screaming group by)

# create a mini table that stores the tax rate per company
WITH tax_rates AS 
(SELECT Salaries.company_id,
 (CASE 
  WHEN MAX(salary) < 1000 THEN 0
  WHEN MAX(salary) < 10000 AND MAX(salary) > 1000 THEN 0.24
  WHEN MAX(salary) > 10000 THEN 0.49
  END) AS TAX

  FROM Salaries
  GROUP BY company_id
)
  

# return the og table but salary is ROUND(salary * 1 - the tax rate,0) 

SELECT Salaries.company_id , Salaries.employee_id , Salaries.employee_name , (ROUND(Salaries.salary * (1-tax),0)) as salary
FROM Salaries
INNER JOIN tax_rates ON Salaries.company_id = tax_rates.company_id