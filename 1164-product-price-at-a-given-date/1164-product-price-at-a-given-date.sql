# Write your MySQL query statement below
WITH date_cutoffs AS (SELECT * FROM Products WHERE DATEDIFF('2019-08-16',change_date) >= 0),

added_ranks AS (SELECT *,(RANK() OVER (partition by product_id ORDER BY change_date DESC) ) AS date_rank FROM date_cutoffs),


filtered_ranks AS (SELECT * FROM added_ranks WHERE date_rank = 1),

unique_products AS (SELECT DISTINCT product_id FROM Products)


# need to find out how to include the product if it is not in the 
SELECT unique_products.product_id, IFNULL(filtered_ranks.new_price,10) AS price FROM filtered_ranks RIGHT OUTER JOIN unique_products ON unique_products.product_id=filtered_ranks.product_id