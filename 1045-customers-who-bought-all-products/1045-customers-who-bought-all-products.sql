# Write your MySQL query statement below
WITH customer_product_counts AS (SELECT customer_id, COUNT(DISTINCT product_key) AS product_count FROM Customer GROUP BY customer_id)

SELECT customer_id FROM customer_product_counts WHERE product_count=(SELECT COUNT(*) FROM Product)