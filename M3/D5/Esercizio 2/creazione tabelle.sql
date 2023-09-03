create table studente(
	matricola_studente varchar(255),
    nome_studente varchar(255) not null,
    città_studente varchar(255) not null,
    primary key(matricola_studente)
);

create table docente(
	matricola_docente varchar(255),
    nome_docente varchar(255),
    primary key(matricola_docente, nome_docente)
);

create unique index indice_docente on docente(matricola_docente, nome_docente);

create table corso(
	codice_corso int,
    nome_corso varchar(255),
    matricola_docente varchar(255),
    primary key (codice_corso),
    constraint fk_matricola_docente_corso_docente foreign key (matricola_docente) references docente(matricola_docente) on update cascade on delete no action
);

create table esame(
	codice_corso int,
    matricola_studente varchar(255),
    data_esame date not null,
    voto float not null,
    settore_scentifico enum('matematica','fisica','disegno'),
    primary key(codice_corso, matricola_studente),
    constraint fk_codice_corso_esame_corso foreign key(codice_corso) references corso(codice_corso) on update cascade on delete no action,
    constraint fk_matricola_studente_esame_studente foreign key(matricola_studente) references studente(matricola_studente) on update cascade on delete no action
);

create unique index indice_docente on esame(codice_corso,matricola_studente);