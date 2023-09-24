# Es_1 creare una nuova lista i cui elementi siano gli stessi di numeri incrementati di 10, mediante comprehension.
numeri=[4,10,50,100,128,71,46]
X_10=[numero+10 for numero in numeri]
print(X_10)

# Es_2 creare una nuova lista i cui elementi siano gli stessi di numeri raddoppiati, mediante comprehension.
numeri=[4,10,50,100,128,71,46]
X_2=[numero*2 for numero in numeri]
print(X_2)

# Es_3 creare una nuova lista i cui elementi siano le iniziali dei nomi, mediante comprehension.
nomi=["Alex","Bob","Cindy","Dan","Emma","Faith","Grace","Henry"]
iniziali=[i[0] for i in nomi]
print(list(iniziali))

# Es_4 Creare una nuova lista i cui elementi siano le iniziali dei nomi seguite da punto, mediante comprehension.
nomi = ["Alex","Bob","Cindy","Dan","Emma","Faith","Grace","Henry"]
iniziali=[i[0]+'.' for i in nomi]
print(list(iniziali))

# Es_5 Creare una lista che contenga (per ogni CF) solo i caratteri relativi al nome, mediante comprehension
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F","DEFGHI95J06A987G"]
rel_nomi=[i[3:6] for i in lista_cf]
print(list(rel_nomi))

# ES_6 Creare due liste, una che contenga (per ogni CF) solo i caratteri relativi al nome, e una che contenga (per ogni CF) solo i caratteri relativi al cognome; entrambe mediante comprehension
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F","DEFGHI95J06A987G"]
rel_nomi=[i[3:6] for i in lista_cf]
rel_cognomi=[i[0:3] for i in lista_cf]
print(list(rel_nomi))
print(list(rel_cognomi))

# ES_7 Creare una lista che contenga solo i codici fiscali dei nati nel '95, tramite comprehension
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F","DEFGHI95J06A987G"]
nati_nel_95=[i for i in lista_cf if '95' in i]
print(nati_nel_95)

# ES_8 Creare una lista che contenga gli ultimi cinque caratteri dei soli codici fiscali di persone nate nel '95, tramite comprehension
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F","DEFGHI95J06A987G"]
nati_nel_95=[i[-5:] for i in lista_cf if '95' in i]
print(nati_nel_95)

# Es_9 Cambiare il simbolo dell'euro (€) in quello del dollaro ($) per ogni stringa nella lista, usando la comprehension.
prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]
dollaro=[i.replace('€','$') for i in prezzi]
print(dollaro)

# Es_10 Vogliamo dividere gli studenti in due squadre per un campionato di Uno nel
#       seguente modo: la prima metà per un squadra, e la seconda metà per l'altra.
#       Creiamo due liste per ogni squadra, e alla fine visualizziamole.'''

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]
l=int(len(studenti)/2)
squadra_1=[i for i in studenti[0:l]]
squadra_2=[i for i in studenti[l:]]
print('squadra 1: ',squadra_1)
print('squadra 2:',squadra_2)

# Es_11 vogliamo dividere gli studenti in due squadre per un campionato di Uno nel
#       seguente modo: selezioneremo i nomi in posizione pari per un squadra, e i nomi
#       in posizione dispari per l'altra.

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]
squadra_1=[i for i in studenti if studenti.index(i)%2==0]
squadra_2=[i for i in studenti if studenti.index(i)%2!=0]
print('squadra 1: ',squadra_1)
print('squadra 2:',squadra_2)

#  Es_12 Abbiamo una lista con i guadagni degli ultimi 12 mesi (supponiamo da Gennaio a Dicembre):
#        dobbiamo confrontare, stampando tutto a video, il guadagno di ogni mese con la media
#        dei guadagni precedenti
#        Esempio di un possibile output:
#        Mese 1: 100 €
#        Mese 2: 90 € (media prec: 100 €)
#        Mese 3: 70 € (media prec: 95 €)]

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
lista_media=[]
somma=0
j=0
for guadagno in guadagni:
    somma+=guadagni[j]
    media=somma/(j+1)
    lista_media.append(media)
    if j==0:
        print('Mese',j+1,':', guadagni[j],'€')
    else:
        print('Mese',j+1,':', guadagni[j],'€ (mese precedente',media,')')
    j+=1

# Es_13 Dobbiamo confrontare, stampando tutto a video, il guadagno di ogni mese con
#       la media dei guadagni precedenti, e specificare nell'output se è maggiore o
#       minore

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
lista_media=[]
somma=0
j=0
for guadagno in guadagni:
    somma+=guadagni[j]
    media=somma/(j+1)
    lista_media.append(media)
    if j==0:
        print('Mese',j+1,':', guadagni[j],'€')
    else:
        print('Mese',j+1,':', guadagni[j],'€ (mese precedente',media,')')
        if guadagni[j]<media:
            print('ho guadagnato meno')
        else:
            print('ho guadagnato di più')
    j+=1

# Es_14 Scrivere una funzione che, data una lista di numeri, fornisca in output il maggiore di tutti, senza utilizzare la funzione max()
lista=[45,368,217,4,232]
def massimo(x):
    max=int(x[0])
    i=0
    for valore in x:
        a=int(x[i])
        if max<=a:
            max=a
        i+=1
    print(max)
massimo(lista)

# Es_15 Scrivere una funzione che, data una lista di numeri, fornisca in output il minimo e
#       il massimo (possiamo usare o meno le funzioni min() e max())max=0
lista=[45,368,2167,4,232]
def max_min(x):
    print("il massimo è:",max(x),"\n il minimo è:",min(x))
max_min(lista)

# Es_16 Scrivere una funzione che, data una lista di numeri, fornisca in output i due
# numeri più grandi

lista=[45,368,217,4,232]
def due_max(x):
    appoggio=x
    maggiori_2=list()
    maggiori_2.append(max(appoggio))
    appoggio.remove(max(x))
    maggiori_2.append(max(appoggio))
    return maggiori_2
print(due_max(lista))

# Es_17
#   Scrivere una funzione che in input acquisisce una lista di numeri e un numero K;
#   in output, dovrà restituire la media di tutti i numeri nella lista maggiori o uguali a
#   K; se non ce ne dovesse essere nessuno, dovrà stampare a schermo un
#   messaggio adeguato
lista=[]
def media_maggiori_k(x):
    vuota=[]
    i=0
    while i<5:
        valore=input('digitaare un intero ')
        lista.append(int(valore))
        i+=1
    print(x)
    k=int(input('inserire il valore do k:'))
    maggiori_k=[i for i in x if i>=k]
    if maggiori_k<=vuota:
        media='non abbiamo valori superiori a k'
    else:
     media=sum(maggiori_k)/len(maggiori_k)
    return media
print(media_maggiori_k(lista))

# Es_18  Scrivere una funzione che, data una lista di numeri, come output stamperà lo stesso numero di asterischi su righe diverse, ottenendo una semplice visualizzazione grafica
lista=[]
def grafico(x):
    while True:
        valore=input('digitare un numero, per terminare digitare "fatto" ')
        if valore=='fatto':
            break
        lista.append(int(valore))
    print(lista)
    for n in lista:
        asterisco=''
        i=0
        while i<n:
            asterisco=asterisco+'*'
            i+=1
        print(asterisco)
grafico(lista)