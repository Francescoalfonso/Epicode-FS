create table progettista(
	matricola_progettista int,
    nome_dipendente varchar(100),
    cognome_dipendente varchar(100),
    primary key (matricola_progettista)
);

create table cliente(
	cod_fiscale varchar(100),
    nome_cliente varchar(100),
    cognome_cliente varchar(100),
    indirizzo_cliente varchar(100),
    città_cliente varchar(100),
    provincia_cliente varchar(100),
    primary key (cod_fiscale)
);

create table magazzino_inverter(
	cod_inverter varchar(100),
    marca_inverter varchar(100),
    modello_inverter varchar(100),
    disponibilità_inverter int,
    primary key (cod_inverter)
);

create table magazzino_pannelli(
	cod_pannelli varchar(100),
    marca_pannelli varchar(100),
    modello_pannelli varchar(100),
    disponibilità_pannelli int,
    primary key (cod_pannelli)
);

create table pratiche_enel(
	pod varchar(100),
    domanda_connessione date,
    inizio_iter date,
    fine_iter date,
    regolamento_esercizio date,
    primary key (pod)
);
    
create table anagrafica_impianto(
	id_impianto int,
    pod varchar(100),
    cod_fiscale varchar(100),
    idirizzo_impianto varchar(100),
    città_impianto varchar(100),
    provincia_impianto varchar(100),
	taglia_impianto enum('3 kW', '4 kW', '6 kW', '10 kW', '15 kW'),
    cod_inverter varchar(100),
    cod_pannelli varchar(100),
    primary key(id_impianto),
	constraint fk_cod_inverter foreign key (cod_inverter) references magazzino_inverter(cod_inverter) on update cascade on delete no action,
	constraint fk_cod_pannelli foreign key (cod_pannelli) references magazzino_pannelli(cod_pannelli) on update cascade on delete no action,
	constraint fk_cod_fiscale_cliente foreign key(cod_fiscale) references cliente(cod_fiscale) on update cascade on delete no action,
	constraint fk_pod foreign key(pod) references pratiche_enel(pod) on update cascade on delete no action
);

create table stato_lavori(
	id_impianto int,
    matricola_progettista int,
    progetto enum('completo','incompleto'),
    installazione enum('completa','incompleta'),
    allaccio date,
    primary key(id_impianto, matricola_progettista),
    constraint fk_id_impianto foreign key (id_impianto) references anagrafica_impianto(id_impianto) on update cascade on delete no action,
    constraint fk_matricola_progettista foreign key (matricola_progettista) references progettista(matricola_progettista) on update cascade on delete no action
);