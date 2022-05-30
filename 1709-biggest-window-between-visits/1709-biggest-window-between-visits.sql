# Write your MySQL query statement below
# the first deal is finding out how to find the difference between any two consecutive visits
# one idea I have is to do something like this
# SELECT UV2.visit_date - UV1.visit_date WHERE uv2 rank = uv1 rank + 1

# if uv2 rank is equal to the last rank then simply  do difference with last date instead


WITH ordered_visits AS (SELECT *, RANK() OVER (PARTITION BY user_id ORDER BY visit_date DESC) AS visit_rank FROM UserVisits),

 difference_in_visits AS 
 (SELECT UV2.*, 
  (CASE WHEN UV2.visit_rank = 1 THEN 
   ABS(DATEDIFF(UV2.visit_date,'2021-1-1')) ELSE ABS(DATEDIFF(UV2.visit_date,UV1.visit_date)) END )
  AS visit_diff 
  FROM ordered_visits UV1, ordered_visits UV2 
  WHERE UV1.user_id = UV2.user_id AND ((UV2.visit_rank = UV1.visit_rank + 1) OR (UV2.visit_rank = UV1.visit_rank)) )

SELECT user_id, MAX(visit_diff) AS biggest_window FROM difference_in_visits GROUP BY user_id

