select max(voto), min(voto),avg(voto)matricola_studente,studente.nome_studente
	from studente
    inner join esame on studente.matricola_studente=esame.matricola_studente
	inner join corso on esame.codice_corso=corso.codice_corso
    inner join docente on corso.matricola_docente=docente.matricola_docente
	group by studente.matricola_studente, studente.nome_studente