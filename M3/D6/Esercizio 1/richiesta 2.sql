select max(voto) as voto_max, min(voto),avg(voto), studente.matricola_studente,studente.nome_studente
	from studente
    inner join esame on studente.matricola_studente=esame.matricola_studente
	inner join corso on esame.codice_corso=corso.codice_corso
    inner join docente on corso.matricola_docente=docente.matricola_docente
    group by studente.matricola_studente,studente.nome_studente
    having avg(voto)>25 and count(esame.data_esame)>=10
    order by voto_max asc
;