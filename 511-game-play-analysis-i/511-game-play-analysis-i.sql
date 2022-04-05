# Write your MySQL query statement below

# group by playerid where the date is the 

SELECT player_id, MIN(event_date) AS first_login FROM Activity  GROUP BY player_id; 
