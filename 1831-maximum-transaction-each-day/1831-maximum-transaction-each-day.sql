# Write your MySQL query statement below

# If in one day there are multiple such transactions, return all of them. --> implies RANK() will be useful

# because the transactions are grouped by their actual timestamp, I need to convert it into a year month day format DATE_FORMAT(day, %Y-%m-%d)

WITH formatted_days AS (SELECT transaction_id, DATE_FORMAT(day, '%Y-%m-%d') AS new_day, amount FROM Transactions ),

ranked_transactions AS (SELECT transaction_id, RANK() OVER (PARTITION BY new_day ORDER BY amount DESC) as trans_rank FROM formatted_days)

SELECT transaction_id FROM ranked_transactions WHERE trans_rank=1 ORDER BY transaction_id