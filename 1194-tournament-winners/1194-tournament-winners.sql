# Write your MySQL query statement below

# we need:
# each player and their total points
# we need to then rank these players partitioning by each group (i.e get the group rank)
# return all players whose rank is one


# getting total player points - if they are player 1, then do first_score if they are player two then do second_score otherwise 0

WITH first_player_scores AS (SELECT player_id, IFNULL(SUM(first_score),0) AS first_scores FROM Matches RIGHT JOIN Players ON first_player=player_id GROUP BY player_id ),

second_player_scores AS (SELECT player_id, IFNULL(SUM(second_score),0) AS second_scores FROM Matches RIGHT JOIN Players ON second_player=player_id  GROUP BY player_id),


total_player_scores AS (SELECT first_player_scores.player_id, first_scores+second_scores AS total_score FROM first_player_scores INNER JOIN second_player_scores ON first_player_scores.player_id = second_player_scores.player_id  ),

players_group_rank AS (SELECT Players.player_id, group_id, RANK() OVER (PARTITION BY group_id ORDER BY total_score DESC, total_player_scores.player_id) AS group_rank, total_score FROM total_player_scores JOIN Players ON  Players.player_id = total_player_scores.player_id)

SELECT group_id, player_id FROM players_group_rank WHERE group_rank=1

# SELECT * FROM combined_player_scores

