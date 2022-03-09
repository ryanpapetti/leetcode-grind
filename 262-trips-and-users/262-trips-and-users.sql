# Write your MySQL query statement below
# a status is cancelled if it is NOT completed
# don't count the cancellation if the driver or the client are banned
# cancellation_rate = cancelled/total (unbanned)
# round ^^^ to 2 decimal places
# group by day

with unbanned_users AS (SELECT users_id FROM Users WHERE banned='No'),
     unbanned_trips AS (SELECT id, request_at, Trips.status FROM Trips WHERE (SELECT 1 FROM unbanned_users WHERE Trips.client_id = unbanned_users.users_id LIMIT 1)=1 AND (SELECT 1 FROM unbanned_users WHERE Trips.driver_id = unbanned_users.users_id LIMIT 1)=1 ),
     valid_trips AS (SELECT * FROM unbanned_trips WHERE (DATEDIFF(request_at,"2013-10-01") <= DATEDIFF("2013-10-03","2013-10-01")))
     # cancelled_trips AS (SELECT * FROM valid_trips WHERE valid_trips.status <> "completed")
     

# SELECT request_at AS Day, ROUND(AVG(),2) OVER (PARTITION BY request_at) AS "Cancellation Rate" FROM unbanned_trips GROUP BY Day WHERE DATEDIFF(Day,"2013-10-01") <= DATEDIFF("2013-10-01","2013-10-03")

SELECT request_at as Day, ROUND(COUNT(case valid_trips.status when 'completed' then null else 1 end)  / COUNT(*),2)  AS "Cancellation Rate" FROM valid_trips GROUP BY request_at

