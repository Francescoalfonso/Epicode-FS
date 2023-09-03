insert into autore(nome,titolo_canzone)
	values	('curt','about a girl'),
			('curt','rape me'),
            ('axel','november rain'),
            ('axel','paradise city');

insert into cantante(nome_cantante)
	values	('curt'),
			('nirvana'),
            ('pink'),
            ('qeen'),
            ('axel'),
            ('guns');
  
 insert into disco(titolo_album,anno,prezzo)
	values	('the wall','1979-01-01',19.99),
			('in utero','1994-01-01',17.59),
            ('use your illusion','1991-01-01',12.99);
            
insert into contiene(n_disco_serie,codice_registr)
	values	(1,1),
			(1,2),
            (1,3),
            (2,1),
            (2,2),
            (2,3);


insert into esecuzione(titolo_canz,anno)
	values	('rape me','1991-01-01'),
			('about a girl','1991-02-01'),
            ('november rain','1979-01-01');