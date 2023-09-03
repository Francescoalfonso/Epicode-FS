select studente.nome_studente,studente.matricola_studente,corso.nome_corso,esame.data_esame,esame.voto
	from studente
    inner join esame on studente.matricola_studente=esame.matricola_studente
    inner join corso on esame.codice_corso=corso.codice_corso
    inner join docente on corso.matricola_docente=docente.matricola_docente
    where esame.voto>28
;