SELECT s.Matricola, s.NomeStudente
FROM studente s
JOIN partecipaconcorsomaster pcm on pcm.MatricolaStudente=s.Matricola
JOIN concorsomaster cm on cm.CodiceMaster=pcm.CodiceMaster
WHERE s.VotoLaurea>100
GROUP BY s.Matricola, s.NomeStudente
HAVING COUNT(cm.CodiceMaster)>=2 AND COUNT(DISTINCT cm.DataPubblicazione) < COUNT(cm.CodiceMaster)