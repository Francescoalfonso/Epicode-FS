insert into progettista 
	values	(001,'marco','rossi'),
			(002,'luca','nervi'),
            (003,'paolo','bitta'),
            (004,'valentino','rossi')
;

insert into cliente
	values	('abc123','Maria','rossi','via nazionale','verona','verona'),
			('cba321','chiara','verdi','corso mazzini','rende','cosenza'),
            ('def258','luca','romeo','via roma','rossano','cosenza')
;

insert into magazzino_inverter 
	values	(001,'zcs','tlmv3',2),
			(002,'zcs','hydhp',4),
            (003,'hi','hpk',50)
;

insert into magazzino_pannelli
	values	(001,'sunpower','450W',200),
			(002,'jinkosolar','550W',150),
            (003,'hoisama','390W',500)
;

insert into pratiche_enel
	values	('it001e123456','2022-02-01','2023-02-08','2023-02-28','2023-03-07'),
			('it001e123467','2022-12-01','2022-12-08','2022-12-28','2023-01-07'),
            ('it001e123478','2022-04-02','2023-04-07','2023-04-26','2023-05-07'),
            ('it001e123489','2021-02-01','2023-02-08','2023-02-28','2023-03-07'),
            ('it001e123490','2021-02-11','2023-02-18','2023-02-20','2023-03-12')
;

insert into anagrafica_impianto
	values	(001,'it001e123456','def258','via roma','rossano','cosenza','3 kW',003,002),
			(002,'it001e123489','abc123','via gramsci','bardolino','verona','6 kW',001,003),
            (003,'it001e123478','cba321','via marina','reggio calabria','reggio calabria','3 kW',002,001),
            (004,'it001e123467','abc123','via sicilia','calciano','matera','15 kW',003,002)
;

insert into stato_lavori
	values	(001,002,'incompleto','incompleta','2028-12-31'),
			(002,001,'completo','incompleta','2028-12-31'),
			(003,003,'completo','completa','2023-06-20'),
			(004,004,'completo','completa','2028-12-31')
;
