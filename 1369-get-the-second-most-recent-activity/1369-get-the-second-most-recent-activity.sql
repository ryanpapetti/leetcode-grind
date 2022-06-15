# Write your MySQL query statement below
WITH activity_ranks AS (SELECT username, activity, startDate, endDate, RANK() OVER (PARTITION BY username ORDER BY endDate DESC) as rank_activity FROM UserActivity),

activity_counts AS (SELECT username, activity, startDate, endDate, COUNT(*) AS activity_count FROM UserActivity GROUP BY username HAVING COUNT(*)=1)


SELECT username, activity, startDate, endDate FROM activity_ranks WHERE rank_activity=2
UNION
SELECT username, activity, startDate, endDate FROM activity_counts
