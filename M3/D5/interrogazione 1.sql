select nome_cantante
from cantante join esecuzione 
on cantante.codice_reg=esecuzione.codice_reg
join autore on esecuzione.titolo_canz=autore.titolo_canzone
where nome=nome_cantante and nome like 'c%';
