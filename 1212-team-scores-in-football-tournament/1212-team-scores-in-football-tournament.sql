# Write your MySQL query statement below
# 3 * count (win) + count(tie)

# so find the games that belong to a particular club
WITH home_points AS (SELECT Teams.team_id AS host_team, Teams.team_name, 

IFNULL(SUM(CASE WHEN Matches.host_goals > Matches.guest_goals THEN 3 WHEN Matches.host_goals=Matches.guest_goals THEN 1 ELSE 0 END ),0) 

AS home_num_points

FROM Teams
LEFT OUTER JOIN Matches ON Teams.team_id=Matches.host_team
GROUP BY Teams.team_id),
                     
                    


guest_points AS (SELECT Teams.team_id AS guest_team, Teams.team_name,

IFNULL(SUM(CASE WHEN Matches.host_goals < Matches.guest_goals THEN 3 WHEN Matches.host_goals=Matches.guest_goals  THEN 1 ELSE 0 END ),0)

AS guest_num_points

FROM Teams
LEFT OUTER JOIN Matches ON Teams.team_id=Matches.guest_team
GROUP BY Teams.team_id),


all_points AS (SELECT guest_points.guest_team as team_id, (home_points.home_num_points + guest_points.guest_num_points) AS total_points FROM guest_points LEFT OUTER JOIN home_points ON guest_points.guest_team=home_points.host_team )


SELECT Teams.team_id, Teams.team_name, IFNULL(all_points.total_points,0) AS num_points FROM Teams LEFT OUTER JOIN all_points ON all_points.team_id = Teams.team_id  ORDER BY num_points DESC, team_id

