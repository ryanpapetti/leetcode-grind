# Write your MySQL query statement below

# so I need to join to get the product names and ids + order dates

# to get the min order date I really should just use WHERE RANK() = 1 by order_date

WITH order_ranks AS (

SELECT Products.product_name, Orders.product_id, Orders.order_id, Orders.order_date, (RANK() OVER (PARTITION BY Orders.product_id ORDER BY Orders.order_date DESC)) AS order_rank 

FROM Orders

JOIN Products ON Products.product_id=Orders.product_id   

ORDER BY product_name, product_id, order_id ) 

SELECT product_name,product_id,order_id,order_date FROM order_ranks WHERE order_rank=1