# Write your MySQL query statement below

WITH eligible_books AS 
(SELECT * FROM Books 
 WHERE available_from < DATE_ADD(DATE("2019-06-23"), INTERVAL -1 MONTH))


SELECT eligible_books.book_id, name FROM eligible_books 
LEFT JOIN Orders ON eligible_books.book_id=Orders.book_id 
GROUP BY book_id 
HAVING
SUM(CASE WHEN (dispatch_date > DATE_ADD(DATE("2019-06-23"), INTERVAL -1 YEAR)) THEN quantity ELSE 0 END) < 10