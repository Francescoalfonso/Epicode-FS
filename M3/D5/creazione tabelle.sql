create table disco(
	n_serie int auto_increment,
    titolo_album varchar(255) not null,
    anno date not null,
    prezzo decimal not null,
    primary key(n_serie)
);

create table autore(
	nome varchar(255) not null,
    titolo_canzone varchar(255),
    primary key(titolo_canzone)
);

create table cantante(
	nome_cantante varchar(255) not null,
    codice_reg int auto_increment,
    primary key (codice_reg)
);

create table esecuzione(
	codice_reg int auto_increment,
    titolo_canz varchar(255) not null,
    anno date not null,
    primary key (codice_reg),
    constraint fk_titolo_canz foreign key (titolo_canz) references autore(titolo_canzone) on update cascade on delete no action
);

create table contiene(
	n_prog int auto_increment,
    n_disco_serie int,
    codice_registr int,
    primary key (n_prog),
    foreign key(n_disco_serie) references disco(n_serie) on update cascade on delete no action
);