CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      WITH sorted_salary AS (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT N)
      SELECT CASE WHEN N=COUNT(salary) THEN MIN(salary) ELSE null END
            FROM sorted_salary

  );
END