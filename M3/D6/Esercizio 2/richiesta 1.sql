SELECT s.NomeStudente, d.SettoreScientifico
FROM STUDENTE s
JOIN PARTECIPACONCORSOMASTER pcm ON s.Matricola = pcm.MatricolaStudente
JOIN CONCORSOMASTER cm ON pcm.CodiceMaster = cm.CodiceMaster
JOIN DIPARTIMENTO d ON d.CodiceDipartimento = pcm.CodiceDipartimento
ORDER BY s.NomeStudente;