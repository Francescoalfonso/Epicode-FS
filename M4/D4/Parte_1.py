# Es_1 Stampare ogni elemento di una stringa su una riga differente
elementi="NPKOHC"
for i in elementi:
    print(i)

# Es_2 Stampare ogni elemento di una stringa su una riga differente, preceduta da 'elemento-'
elementi="NPKOHC"
for i in elementi:
    print('elemento - ',i)

# Es_3 Stampare ogni elemento di una stringa su una riga differente, preceduta da 'elemento-numero'
elementi="NPKOHC"
for  contatore,i in enumerate(elementi,1):
    print('elemento - ',contatore,i)

# Es_4 modificare la parola 'marmalade' sostituendo le 'e' con 'a'  e viceversa. salvare il risultato e stampare
# Mediante ciclo for
parola="marmalade"
mod=[]
for i in parola:
    if i=='e':
        i='a'
        mod.append(i)
    else:
        mod.append(i)
print(mod)
# Mediante ciclo while
arola="marmalade"
mod=[]
i=0
while i<len(parola):
    if parola[i]=='e':
        mod.append('a')
        i+=1
    else:
        mod.append(parola[i])
        i+=1
print(mod)
# Mediante replace
parola="marmalade"
modificata=parola.replace("e","a")
print(modificata)

# Es_5 Calcolare e stampare tutte le prime 10 potenze di 2 utilizzando il ciclo for
base=2
for contatore in range(10):
    valore=base**contatore
    print(valore)

# Es_6 Calcolare le prime N potenze di 3 e stamparle in una lista
# metodo for
N=int(input('inserire il limite di potenze da calcolare '))
base=3
lista=[]
for i in range(N):
    valore=base**i
    lista.append(valore)
print(lista)
# Metodo while
N=int(input('inserire il limite di potenze da calcolare '))
base=3
lista=[]
i=0
while i<N:
    valore=base**i
    lista.append(valore)
    i+=1
print(lista)
# Es_7 Calcolare le prime N potenze di k e stamparle in una lista, k ed N sono inserite da utente
# metodo for
N=int(input('inserire il limite di potenze da calcolare '))
k=int(input('inserire il valore di k che farà da base al nostro esponente '))
lista=[]
for i in range(N):
    valore=k**i
    lista.append(valore)
print(lista)
# Metodo while
N=int(input('inserire il limite di potenze da calcolare '))
k=int(input('inserire il valore di k che farà da base al nostro esponente '))
lista=[]
i=0
while i<N:
    valore=k**i
    lista.append(valore)
    i+=1
print(lista)

# Es_8 Calcolare e stampare tutte le potenze di 2 minori di 25000
limite=25000
base=2
i=0
potenza=base**i
while potenza<=limite:
    potenza=base**i
    print(potenza)
    i+=1

# Es_9 Calcolare e stampare tutte le potenze di 2 minori di N ricevuto da input 
limite=int(input("inserire il limite secondo il quale arrestare l'elevazione a potenza "))
base=2
i=0
potenza=base**i
while potenza<=limite:
    potenza=base**i
    print(potenza)
    i+=1

# Es_10 Calcolare e stampare le prime 100 potenze di 2, ogni 3
# Metodo 1
limite=100
base=2
lista=[]
for i in range(limite):
    if i%3==0:
        potenza=base**i
        lista.append(potenza)
print(lista)
# Metodo 2
limite=100
base=2
lista=[]
for i in range(0,100,3):
        potenza=base**i
        lista.append(potenza)
print(lista)

# Es_11 Data una lista di numeri utilizzando il costrutto for trovare il max 
lista=[4,9,5,1,7,10,2,3]
max=0
for i in lista:
    if i>=max:
        max=i
print(max)

# Es_12 Mediante ciclo for stampare l'età media degli studenti
età_studenti=[20,30,40,50,60]
somma=0
for i in età_studenti:
    somma+=i
media=somma/len(età_studenti)
print(media)

# Es_13 Mediante ciclo for stampare la media dei guadagni
età_studenti=[100,90,70,40,50,80,90,120,80,20,50,50]
somma=0
for i in età_studenti:
    somma+=i
media=somma/len(età_studenti)
print(media)

# Es_14 é ugaule al 12 e 13 
età_studenti=[100,90,70,40,50,80,90,120]
somma=0
for i in età_studenti:
    somma+=i
media=somma/len(età_studenti)
print(media)

# Es_15 Data una lista di studenti stampare singolarmente i nomi preceduti da un -
studenti=['Alex','Bob','Cindy','Dan','emma','Faith','Grace']
for i in studenti:
    print(' - ', i)

# Es_16 Date tre liste di dimensioni uguali stapare su ogni riga nome studente, corso ed edizioni corrispondenti
studenti=['Alex','Bob','Cindy','Dan','emma','Faith','Grace']
corsi=['Cybersecurity','Data Analyst','Backend','Frontend','Data Analyst','Backend','Frontend','Cybersecurity']
edizioni=[1,2,3,2,2,1,3,3]
for studente,corso,edizione in zip(studenti,corsi,edizioni):
    print(studente,' segue ',corso,', edizione ',edizione)

# Es_17 Data una lista di parole per ogni parola stampare quante volte appare la lettera 'e'
parole=['Albergo','Sedia','Borgo','Petalo','Belvedere','Semestre','Sosta','Orpello','Abete']
for i in parole:
    conteggio=0
    for j in i:
        if j=='e':
            conteggio+=1
    print('nella parola',i,'la lettera "e" è contenuta',conteggio)

# Es_18 Data una lista di parole per ogni parola stampare quante volte appare la lettera 'e' facendo attenzione che appare sia maiuscola che minuscola
parole=['Albergo','Sedia','Borgo','Petalo','Eremo','Belvedere','Semestre','Esteta','Sosta','Orpello','Abete','Orologio','Cesta','Ermellino']
for i in parole:
    conteggio=0
    for j in i:
        if j=='e' or j=='E':
            conteggio+=1
    print('nella parola',i,'la lettera "e" è contenuta',conteggio)