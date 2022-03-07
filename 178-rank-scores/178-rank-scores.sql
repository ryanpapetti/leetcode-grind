# Write your MySQL query statement below
# ranked in descending order
# Not grouped (non distinct scores)


WITH sorted_scores(score) AS (SELECT DISTINCT score AS score FROM scores ORDER BY score DESC),
     score_ranks AS (SELECT score, ROW_NUMBER() OVER (ORDER BY score DESC) AS score_rank FROM sorted_scores ORDER BY score DESC)
     


SELECT scores.score, score_rank AS "rank" FROM scores LEFT JOIN score_ranks ON scores.score = score_ranks.score ORDER BY score_rank 


