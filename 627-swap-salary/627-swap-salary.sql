# Write your MySQL query statement below
# In plain english: if the sex is m, make it f; otherwise make it m
UPDATE salary
SET
    sex = CASE sex
    WHEN 'm' THEN 'f'
    ELSE 'm'
    END;