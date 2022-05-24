# Write your MySQL query statement below
SELECT x,y,z, 

(CASE WHEN z < x+y AND x < z+y AND y <z+x  THEN "Yes" ELSE "No" END) AS triangle

FROM Triangle