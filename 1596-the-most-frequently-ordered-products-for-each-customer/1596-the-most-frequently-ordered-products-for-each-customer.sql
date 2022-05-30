# Write your MySQL query statement below

# there are a couple problem hints
# first, only get customers with at least one order implies an inner join
# two, there is a ranking of some sort, partitioned by the product id and ranked by the count 
# its likely that I need to add a CTE or another tabel to make this faster



WITH order_ranks AS (SELECT customer_id, product_id, RANK() OVER (partition by customer_id Order by COUNT(product_id) DESC) AS order_rank FROM Orders GROUP BY customer_id, product_id ORDER BY customer_id, product_id )

SELECT customer_id, Products.product_id, Products.product_name FROM order_ranks JOIN Products ON order_ranks.product_id = Products.product_id WHERE order_ranks.order_rank=1

# SELECT * FROM order_ranks