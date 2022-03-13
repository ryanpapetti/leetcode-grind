# Write your MySQL query statement below

# the select wrapping returns null for us :) 

# get me the salary unless the count of salary is 1 in which case get me the null

SELECT(SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
     LIMIT 1,1)
      
as SecondHighestSalary