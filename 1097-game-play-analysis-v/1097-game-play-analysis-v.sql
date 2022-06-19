# Write your MySQL query statement below

# things I need:

# number of players with installation date as X
# each player and their installation date
# lead() of each player and find where the lead is the day after the user's installation date
# get all users satisfying ^^^^^^ and add the user installation date
# divide relevant users / installs 



WITH user_installation_dates AS (SELECT player_id, MIN(event_date) AS install_date FROM Activity GROUP BY player_id),

install_date_counts AS (SELECT install_date, COUNT(DISTINCT player_id) AS installs FROM user_installation_dates GROUP BY install_date),

user_next_logins AS (SELECT player_id, event_date, LEAD(event_date,1) OVER (PARTITION BY player_id ORDER BY event_date) AS next_login FROM Activity),

retented_players AS (SELECT user_next_logins.player_id, event_date FROM user_next_logins JOIN user_installation_dates ON user_installation_dates.player_id=user_next_logins.player_id  WHERE next_login=DATE_ADD(event_date, INTERVAL 1 DAY) AND event_date=install_date),

retented_players_by_install AS (SELECT event_date, COUNT(DISTINCT player_id) AS relevant_players FROM retented_players GROUP BY event_date HAVING relevant_players > 0)



SELECT install_date AS install_dt, installs, 
(CASE WHEN relevant_players IS NULL THEN 0.00 
 ELSE ROUND((relevant_players/installs),2) END) 
 AS Day1_retention 

FROM install_date_counts LEFT JOIN retented_players_by_install ON install_date_counts.install_date=retented_players_by_install.event_date
