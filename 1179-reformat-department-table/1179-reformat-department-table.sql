# Write your MySQL query statement below
# SQL is not as nice as python with if statements and indexing etc.
# One strategy is that we could use a CASE for each month
# If there is revenue, add it there, otherwise put null
SELECT id,

MAX(CASE WHEN month='Jan' then revenue else null end) Jan_Revenue, #this is ultra tedious but I suppose it works
MAX(CASE WHEN month='Feb' then revenue else null end) Feb_Revenue,
MAX(CASE WHEN month='Mar' then revenue else null end) Mar_Revenue,
MAX(CASE WHEN month='Apr' then revenue else null end) Apr_Revenue,
MAX(CASE WHEN month='May' then revenue else null end) May_Revenue,
MAX(CASE WHEN month='Jun' then revenue else null end) Jun_Revenue,
MAX(CASE WHEN month='Jul' then revenue else null end) Jul_Revenue,
MAX(CASE WHEN month='Aug' then revenue else null end) Aug_Revenue,
MAX(CASE WHEN month='Sep' then revenue else null end) Sep_Revenue,
MAX(CASE WHEN month='Oct' then revenue else null end) Oct_Revenue,
MAX(CASE WHEN month='Nov' then revenue else null end) Nov_Revenue,
MAX(CASE WHEN month='Dec' then revenue else null end) Dec_Revenue

FROM Department

GROUP BY id