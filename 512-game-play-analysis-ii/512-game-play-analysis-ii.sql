# Write your MySQL query statement below

WITH temp AS (SELECT player_id, MIN(event_date) AS first_date FROM Activity GROUP BY player_id)

SELECT Activity.player_id, Activity.device_id FROM Activity INNER JOIN temp ON temp.player_id = Activity.player_id AND temp.first_date = Activity.event_date