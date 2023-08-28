select città from aeroporto where num_piste is null;

select tipo_aereo from volo where città_partenza='torino';

select città_partenza from volo where città_arrivo='bologna';

select città_partenza, città_arrivo from volo where id_volo='az272';

select	tipo_aereo, giorno_settimana, ora_partenza from volo where città_partenza like ('b%o%') and città_arrivo like ('%e%a');
 
