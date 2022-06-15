# Write your MySQL query statement below
WITH activity_ranks AS (SELECT username, activity, startDate, endDate, RANK() OVER (PARTITION BY username ORDER BY endDate DESC) AS rank_activity, COUNT(*) OVER (PARTITION BY username) AS count_activity  FROM UserActivity)


SELECT username, activity, startDate, endDate FROM activity_ranks WHERE rank_activity=2 OR count_activity=1
