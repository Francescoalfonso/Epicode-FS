SELECT d.NomeDipartimento, d.SettoreScientifico, COUNT(cm.CodiceMaster) AS NumConcorsi
FROM DIPARTIMENTO d
JOIN CONCORSOMASTER cm ON cm.CodiceDipartimento=d.CodiceDipartimento
WHERE d.CodiceDipartimento NOT IN (
SELECT cm.CodiceDipartimento
FROM CONCORSOMASTER cm 
WHERE cm.NumPostiDisponibili <= 7)
GROUP BY d.NomeDipartimento, d.SettoreScientifico
ORDER BY d.NomeDipartimento, d.SettoreScientifico;
