# Es_1 Stamapare ogni carattere della stringa uno su ogni riga utilizzando il while
nome_scuola="Epicode"
i=0
while i<len(nome_scuola):
    print(nome_scuola[i])
    i+=1

# Es_2 Stampare a video tutti i numeri da 0 a 20
i=0
while i<=20:
    print(i)
    i+=1
# Es_3 Calcolare e stampare tutte le prime 10 potenze di 2
esponente=0
base=2
while esponente<=10:
    potenza=base**esponente
    esponente=esponente+1
    print(potenza)

# Es_4 Calcolare e stampare tutte le prime N potenze di 2 mediante un ciclo while chiedendo all'utente il valore di N
esponente=0
base=2
N=int(input('inserire il limite degli esponenziali da calcolare: '))
while esponente<=N:
    potenza=base**esponente
    esponente=esponente+1
    print(potenza)

# Es_5 Verificare che entrambe le liste abbiano la stessa lunghezza e stampare a video una frase che ci dica se è così o meno
studenti=["Alex","Bob","Cindy","Dan","Emma","Faith","Grace","Henry"]
corsi=["Cybersecurity","Data Analyst","Backend","Frontend","Data Analyst","Backend","Frontend"]
if len(studenti)==len(corsi):
    print('entrambe le liste hanno la stessa lunghezza che è pari a:',len(studenti))
else:
    print('Le liste hanno lunghezze differenti ','Studenti ha una lunghezza di: ',len(studenti),' Corsi ha una lunghezza di: ',len(corsi))

# Es_6 Con riferimento all'eserccizio precedente aggiungere i dati mancanti alla lista corsi, sapendo che l'elemento in pos. 0 segue il corso in pos. 0
# Una volta aggiunti i dati mancanti confrontare la  lunghezza tra le liste  e se sono lunghe uguali stampare la lista corsi
studenti=["Alex","Bob","Cindy","Dan","Emma","Faith","Grace","Henry"]
corsi=["Cybersecurity","Data Analyst","Backend","Frontend","Data Analyst","Backend","Frontend"]
corsi.append("Cybersecurity")
if len(studenti)==len(corsi):
    print('entrambe le liste hanno la stessa lunghezza che è pari a:',len(studenti))
    print(corsi)
else:
    print('Le liste hanno lunghezze differenti ','Studenti ha una lunghezza di: ',len(studenti),' Corsi ha una lunghezza di: ',len(corsi))

# Es_7 Scriviamo un programma che chiede in input una stringa e visualizza i primi 3 caratteri seguiti da tre puntini e poi stampare le ultime 3
stringa=input('Inserire una stringa ')
if len(stringa)<6:
    print('La stringa contiene meno di 6 caratteri')
else:
    if len(stringa)==6:
        print('i punti sospensivi sono superflui ma li stampo comunque: ',stringa[:3],'...',stringa[-3:])
    if len(stringa)>6:
        print('i punti sospensivi indicano che manca parte del testo: ',stringa[:3],'...',stringa[-3:])

# Es_8 Memorizza e stampa tutti i fattori di un dato numero dato in input
valore=int(input('inserire un intero '))
fattori=[]
d=2
while valore>1:
    if valore%d==0:
        fattori.append(d)
        valore//=d
    else:
        d+=1
print(fattori)