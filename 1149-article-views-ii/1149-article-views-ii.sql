# Write your MySQL query statement below

# we need to get all viewers where the article(1) != article(2) and view_date(1)=view_date(2)

# maybe lead or lag

WITH previous_views AS (SELECT *, LAG(view_date,1) OVER (PARTITION BY viewer_id ORDER BY view_date) AS prev_date, LAG(article_id,1) OVER (PARTITION BY viewer_id ORDER BY view_date) AS prev_article FROM Views)

SELECT DISTINCT viewer_id AS id FROM previous_views WHERE article_id<>prev_article AND view_date=prev_date