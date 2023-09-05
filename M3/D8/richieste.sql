/*query1 mostrare quanti progetti completati ha ogni progettista e dove sono installati */

select progettista.matricola_progettista, anagrafica_impianto.città_impianto, count(progettista.matricola_progettista)
from progettista
join stato_lavori on progettista.matricola_progettista=stato_lavori.matricola_progettista
join anagrafica_impianto on stato_lavori.id_impianto=anagrafica_impianto.id_impianto
where progetto='completo'
group by progettista.matricola_progettista, anagrafica_impianto.città_impianto;

/*query1 mostrare quante installazioni completate ha ogni progettista e dove sono installati
 e che l'allaccio sia precedente alla data odierne*/

select progettista.matricola_progettista, anagrafica_impianto.città_impianto, count(progettista.matricola_progettista)
from progettista
join stato_lavori on progettista.matricola_progettista=stato_lavori.matricola_progettista
join anagrafica_impianto on stato_lavori.id_impianto=anagrafica_impianto.id_impianto
where installazione='completa' and  allaccio<=now()
group by progettista.matricola_progettista, anagrafica_impianto.città_impianto;

/* query 3 mostrare per inverter e pannelli la marca ed il modello relativi ai singoli impianti e ordinarli per cliente */

select anagrafica_impianto.cod_fiscale,magazzino_inverter.marca_inverter,magazzino_inverter.modello_inverter, magazzino_pannelli.marca_pannelli, magazzino_pannelli.modello_pannelli
from anagrafica_impianto
join magazzino_inverter on anagrafica_impianto.cod_inverter=magazzino_inverter.cod_inverter
join magazzino_pannelli on anagrafica_impianto.cod_pannelli=magazzino_pannelli.cod_pannelli
order by anagrafica_impianto.cod_fiscale;

/* query 4 mostrare il POD degli impiati pari a 3 kW in cui la richiesta di connessione è stata fatta dopo il 2021/01/01 
*/
select pratiche_enel.pod
from anagrafica_impianto
join pratiche_enel on anagrafica_impianto.pod=pratiche_enel.pod
where taglia_impianto='3 kW' and domanda_connessione>='2021-01-01'
group by pratiche_enel.pod;

/* query 5 mostrare nome e cognome del cliente e taglia degli impianti allacciati nel 2023*/
 select cliente.nome_cliente,cliente.cognome_cliente,anagrafica_impianto.taglia_impianto
 from cliente
 join anagrafica_impianto on cliente.cod_fiscale=anagrafica_impianto.cod_fiscale
 join stato_lavori on anagrafica_impianto.id_impianto=stato_lavori.id_impianto
 where year(allaccio)=2023
group by cliente.nome_cliente,cliente.cognome_cliente,anagrafica_impianto.taglia_impianto;

/* query 6 mostrare il codice pod, nome e cognome dei clienti che hanno la residenza che coincide
con l'ubicazione dell'impianto*/

select anagrafica_impianto.pod,cliente.nome_cliente,cliente.cognome_cliente,cliente.cod_fiscale
from cliente
join anagrafica_impianto on cliente.cod_fiscale=anagrafica_impianto.cod_fiscale
where indirizzo_cliente=idirizzo_impianto and  provincia_cliente=provincia_impianto
order by cliente.cod_fiscale desc;

/* query 7 mostrare matricola progettista, pod e codice fiscale del cliente, 
per gli impianti per cui sono trascorsi meno di 40 giorni tra la domanda di connessione e l'allaccio */

select stato_lavori.matricola_progettista,anagrafica_impianto.pod,anagrafica_impianto.cod_fiscale
from pratiche_enel
join anagrafica_impianto on pratiche_enel.pod=pratiche_enel.pod
join stato_lavori on anagrafica_impianto.id_impianto=stato_lavori.id_impianto
where datediff(allaccio,inizio_iter)<130;

/* query 8 ordinare per provincia i progetti completati */

select pod, provincia_impianto
from anagrafica_impianto
join stato_lavori on anagrafica_impianto.id_impianto=stato_lavori.id_impianto
where installazione='completa'
order by provincia_impianto;

/* query 9 mostrare il nome del cliente il quale ha pannelli sunpower */
select nome_cliente
from magazzino_pannelli
join anagrafica_impianto on magazzino_pannelli.cod_pannelli=anagrafica_impianto.cod_pannelli
join cliente on anagrafica_impianto.cod_fiscale=cliente.cod_fiscale
where marca_pannelli='sunpower'
;
