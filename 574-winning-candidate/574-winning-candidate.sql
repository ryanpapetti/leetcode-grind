# Write your MySQL query statement below
WITH candidate_counts AS (SELECT candidateId, COUNT(candidateId) as counts FROM Vote GROUP BY candidateId),

# SELECT * FROM candidate_counts

winner_votes AS (SELECT MAX(counts) FROM candidate_counts)



SELECT name
FROM Candidate, winner_votes, candidate_counts
WHERE  candidate_counts.candidateId = Candidate.Id 
AND candidate_counts.counts = (SELECT * FROM winner_votes)