# Write your MySQL query statement below
WITH spam_actions AS (SELECT DISTINCT post_id, action_date FROM Actions WHERE extra='spam' AND action ='report'),

was_removed AS (SELECT DISTINCT spam_actions.post_id, action_date, CASE WHEN remove_date IS NUlL THEN 0 ELSE 1 END AS removed_flag FROM spam_actions LEFT JOIN Removals ON Removals.post_id=spam_actions.post_id),

daily_averages AS (SELECT (SUM(removed_flag) / COUNT(post_id)) AS daily_avg FROM was_removed GROUP BY action_date)

SELECT 100 * ROUND(AVG(daily_avg),4) AS average_daily_percent FROM daily_averages

