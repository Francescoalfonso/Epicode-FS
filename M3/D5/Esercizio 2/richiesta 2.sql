select docente.nome_docente,corso.nome_corso,esame.settore_scentifico
	from docente
	inner join corso on docente.matricola_docente=corso.matricola_docente
	inner join esame on corso.codice_corso=esame.codice_corso
;