# Es_19
# Abbiamo un testo, ad esempio:
# racconto = """Lisetta va a passeggio in campagna; è felice di
# raccogliere i fiori che crescono sulle rive, ai bordi della strada.
# Ha già un bel mazzetto di ranuncoli e margherite."""
# Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che
# contiene ogni tipo di carattere e quante volte appare.
# Esempio, se il testo è
# testo = """Ciao a tutti!"""
# l'output sarà:
# {"C": 1, "i": 2, "a": 2, "o": 1, " ": 2, "t": 3, "u": 1, "!": 1}

racconto="""Lisetta va a passeggio in campagna; è felice di raccogliere i fiori che crescono sulle rive, ai bordi della strada. Ha già un bel mazzetto di ranuncoli e margherite."""
def dizionario_lettere(testo):
    chiavi=set()
    for i in testo:
        chiavi.add(i)
    chiavi=list(chiavi)
    valori=[]
    for i in chiavi:
        valori.append(testo.count(i))
    dizionario=dict(zip(chiavi,valori))
    return dizionario

print(dizionario_lettere(racconto))

# Es_20
# Abbiamo un testo, ad esempio:
# racconto = """Lisetta va a passeggio in campagna; è felice di
# raccogliere i fiori che crescono sulle rive, ai bordi della strada.
# Ha già un bel mazzetto di ranuncoli e margherite."""
# Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che
# contiene ogni tipo di carattere e quante volte appare, esclusi punteggiatura e spazi.
# Esempio, se il testo è
# testo = """Ciao a tutti!"""
# l'output sarà:
# {"C": 1, "i": 2, "a": 2, "o": 1, "t": 3, "u": 1}

racconto="""Lisetta va a passeggio in campagna; è felice di raccogliere i fiori che crescono sulle rive, ai bordi della strada. Ha già un bel mazzetto di ranuncoli e margherite."""
def dizionario_lettere(testo):
    chiavi=set()
    punteggiatura=(',',';','.',' ',':','!','?')
    for i in testo:
        if i not in punteggiatura:
            chiavi.add(i)
    chiavi=list(chiavi)
    valori=[]
    for i in chiavi:
        valori.append(testo.count(i))
    dizionario=dict(zip(chiavi,valori))
    return dizionario

print(dizionario_lettere(racconto))

# Es_21
# Abbiamo un testo, ad esempio:
# racconto = """Lisetta va a passeggio in campagna; è felice di
# raccogliere i fiori che crescono sulle rive, ai bordi della strada.
# Ha già un bel mazzetto di ranuncoli e margherite."""
# Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che
# contiene ogni tipo di carattere e quante volte appare, senza fare differenza tra maiuscole e
# minuscole.

racconto="""Lisetta va a passeggio in campagna; è felice di raccogliere i fiori che crescono sulle rive, ai bordi della strada. Ha già un bel mazzetto di ranuncoli e margherite."""
def dizionario_lettere(testo):
    chiavi=set()
    testo_minuscolo=testo.lower()
    for i in testo_minuscolo:
        chiavi.add(i)
    chiavi=list(chiavi)
    valori=[]
    for i in chiavi:
        valori.append(testo_minuscolo.count(i))
    dizionario=dict(zip(chiavi,valori))
    return dizionario

print(dizionario_lettere(racconto))

# Esercizio 22
# Esaminiamo il dataset:
# quanti dati ci sono in totale?(quante coppie chiave,valore ci sono)
# quali sono i metadati? (quali sono le chiavi)
# stampiamo il primo elemento (Sarebbe la prima riga del dataset)
# stampiamo l'ultimo elemento
# riusciamo a stampare un elemento a caso?
# quali sono gli anni di inserimento presenti?
# quante attività ci sono nel quadrato di longitudine 9-10 e latitudine 45-46?
# quante attività ci sono nella provincia di Vicenza?
# quante enoteche ci sono, e come si chiamano?
# quante attività ci sono in Lazio e Abruzzo assieme?

import json
import random

f = open('''Mappa-dei-pub-circoli-locali-in-Italia.json''', "r", encoding="latin1")
mappe=json.load(f)
print('quanti dizionari ci sono in totale? ',len(mappe)) 

key_valori=0
for dizionari in  mappe:
    key_valori+=len(dizionari)
print('quante coppie chiave-valore ci sono?', key_valori)

chiavi=set()
for dizionari in mappe:
    for chiave in dizionari.keys():
        chiavi.add(chiave)
print('le chiavi sono: ', chiavi)

primo_elemento=mappe[0]
print('il primo elemento è: ',primo_elemento)

ultimo_elemento=mappe[-1]
print("l'ultimp elemento è: ", ultimo_elemento)

elemento_random=random.choice(mappe)
print("stampiamo un elemento random: ",elemento_random)

anni_inserimento=set()
for elemento in mappe:
    anno=elemento["canno_inserimento"]
    anni_inserimento.add(anno)
print('gli anni di inserimento sono: ', anni_inserimento)

attività_quadrato=[dizionari['cnome'] for dizionari in mappe if 9<float(dizionari["clongitudine"])<10 and 45<float(dizionari["clatitudine"])<46]
print(len(attività_quadrato))

attività_Vicenza=[dizionari['cnome']for dizionari in mappe if dizionari['cprovincia'].lower()=='vicenza']
print(len(attività_Vicenza))

enoteche=[dizionari['cnome']for dizionari in mappe if dizionari['cnome'].lower().find('enoteca') !=-1]
print('le enoteche presenti sono:',len(enoteche),'\n', 'e si chiamano:', enoteche)

attività_lazio_Abbruzzo=[dizionari['cnome'] for dizionari in mappe if dizionari['cregione'].lower()=='lazio'or dizionari['cregione'].lower()=='abruzzo']
print('le attività che si trovanp in abruzzo e nel lazio sono:',len(attività_lazio_Abbruzzo))