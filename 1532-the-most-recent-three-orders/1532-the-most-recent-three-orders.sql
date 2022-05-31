# Write your MySQL query statement below
# to get most recent 3, just rank and get all where rank > 3 also dont use dense rank


WITH order_ranks AS

(SELECT Orders.*, RANK() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS order_rank FROM Orders )


SELECT Customers.name AS customer_name, Customers.customer_id, order_ranks.order_id, order_ranks.order_date FROM order_ranks JOIN Customers ON Customers.customer_id = order_ranks.customer_id WHERE order_ranks.order_rank <= 3 ORDER BY customer_name, customer_id, order_date DESC
