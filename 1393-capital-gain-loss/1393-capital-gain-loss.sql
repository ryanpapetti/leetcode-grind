# Write your MySQL query statement below

# there's a trick here that REQUIRES YOU TO SEE THE DAYS ARE NOT ORDERED

# the idea here is to build a cumulative sum 

# something like: CASE WHEN operation = 'Buy' THEN price * -1 ELSE price

# also we need to group by stock_name

SELECT stock_name, SUM(CASE WHEN operation = 'Buy' THEN price * -1 ELSE price END) AS capital_gain_loss 

FROM Stocks 

GROUP BY stock_name

ORDER BY operation_day