create database esercizio_4_M4;
use esercizio_4_M4;
create table if not exists aeroporto(
	città varchar(255),
    nazione varchar(255),
    num_piste tinyint unsigned,
    primary key (città)
    );
create table if not exists aereo(
	tipo_aereo varchar(255),
    num_passeggeri int,
    quantità_merci int unsigned,
    primary key (tipo_aereo)
    );
create table if not exists volo(
	id_volo char(5),
    giorno_settimana enum ('lun','mar','mer','gio','ven','sab','dom'),
    città_partenza varchar(255),
    ora_partenza time,
    città_arrivo varchar(255),
    ora_arrivo date,
    tipo_aereo varchar(255),
    primary key (id_volo),
    constraint fk_tipo_aereo foreign key (tipo_aereo) references aereo(tipo_aereo) on update cascade on delete no action,
    constraint fk_città_partenza foreign key(città_partenza) references aeroporto(città) on update cascade on delete no action,
    constraint fk_città_arrivo foreign key(città_arrivo) references aeroporto(città) on update cascade on delete no action
    );