# Write your MySQL query statement below



SELECT DISTINCT num AS ConsecutiveNums FROM Logs logs1
WHERE EXISTS(
    SELECT 1 FROM Logs logs2
    WHERE logs1.num=logs2.num
    AND logs2.id = logs1.id - 1
)
AND EXISTS(
    SELECT 1 FROM Logs logs2
    WHERE logs1.num=logs2.num
    AND logs2.id = logs1.id + 1
)


