# Write your MySQL query statement below

# this requires two tables at least. One to get the grouped event type averages 

WITH event_averages AS (SELECT event_type, AVG(occurences) AS event_avg FROM Events GROUP BY event_type),

# now I need to get all the businesses that have two event_types where the occurence > event_avg

joined_table AS (SELECT Events.business_id, Events.event_type FROM Events JOIN event_averages ON Events.event_type= event_averages.event_type WHERE Events.occurences > event_averages.event_avg)

SELECT business_id FROM joined_table GROUP BY business_id HAVING COUNT(DISTINCT event_type)>1

# SELECT * FROM joined_table