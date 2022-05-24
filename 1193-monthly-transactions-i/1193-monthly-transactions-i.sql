# Write your MySQL query statement below

# ooh a double group by!

# note the trans_date needs to be TRUNCATED to the month

# we need a COUNT(*) per group as well as a COUNT(state = 'approved')

# we also need a SUM(amount) per group AND a SUM(state is approved)


SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country, 
COUNT(*) AS trans_count,
SUM(CASE WHEN state='declined' THEN 0 ELSE 1 END) AS approved_count, 
SUM(amount) AS trans_total_amount, SUM(CASE WHEN state='declined' THEN 0 ELSE amount END) AS approved_total_amount

FROM Transactions

GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country
