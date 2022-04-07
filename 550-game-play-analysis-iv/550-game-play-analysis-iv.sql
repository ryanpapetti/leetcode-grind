# Write your MySQL query statement below
# find the first day they logged in
# if the next day is in the dataset, add one to count


WITH first_logins AS (SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id),

     total_players AS (SELECT COUNT(DISTINCT player_id) as players FROM Activity),
     
     numerator AS (SELECT COUNT(*) as consecutive_logins
                    FROM Activity 
                    JOIN first_logins ON first_logins.player_id = Activity.player_id 
                    WHERE event_date = DATE_ADD(first_login, INTERVAL 1 DAY))
                    
                    

SELECT ROUND(numerator.consecutive_logins/total_players.players,2) AS fraction FROM numerator, total_players



