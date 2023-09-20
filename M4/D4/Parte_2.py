# Es_19 Trovare i codici fiscali i quali contengono '95', metterli in una lista e stamparla
lista_cf=["ABCDEF95G01A123B","GHIJKL91M02A321C","MNOPQR89S03A456D","STUVWX95Z04A654E","XYZABC01D05A789F","DEFGHI95J06A987G"]
lista=[]
for i in lista_cf:
    if '95' in i:
        lista.append(i)
print(lista)

# Es_20 data la lista di cf precedente stampare a video per ogni cf i caratteri relativi al nome e quelli relativi al cognome
lista_cf=["ABCDEF95G01A123B","GHIJKL91M02A321C","MNOPQR89S03A456D","STUVWX95Z04A654E","XYZABC01D05A789F","DEFGHI95J06A987G"]
for i in lista_cf:
    print('dato il cf',i,'i caratteri relativi al nome sono',i[:3],'i caratteri relativi al cognome sono',i[3:6])

# Es_21 Date tre liste di dimensioni uguali stampare tutti e soli gli studenti che frequentano una prima edizione
studenti=['Alex','Bob','Cindy','Dan','emma','Faith','Grace']
corsi=['Cybersecurity','Data Analyst','Backend','Frontend','Data Analyst','Backend','Frontend','Cybersecurity']
edizioni=[1,2,3,2,2,1,3,3]
for studente,corso,edizione in zip(studenti,corsi,edizioni):
    if edizione==1:
        print(studente,corso,edizione) # se dovessi stampare solo gli studenti allora basta togliere corso ed edizione dalla print

# Es_22 Creare un dizionario che assegni ad ogni proprietario la sua auto
registro={'Ada':'Punto','Ben':'Multipla','Charlie':'Golf','Debbie':107}
print('il registro completo è composto dai seguenti propietari ed auto: ',registro)
print("l'auto guidata da Debbie è una: ",registro['Debbie'])

# Es_23 In riferimento al precedente esecizio aggiungere Emily che guida una A1, Fred che guida una octavia ed eliminare i dati relativi a Ben. Poi sta,pare il registro
registro={'Ada':'Punto','Ben':'Multipla','Charlie':'Golf','Debbie':107}
# registro['Emily','Fred']='A1','Octavia' # riga prova chiedere se va bene
registro['Emily']='A1'
registro['Fred']='Octavia'
del registro['Ben']
print(registro)

# Es_24 Dati due dizionari che assegnano le auto ai proprietari aggiornare il primo con i dati del secondo
dizionario_auto={'Ada':'Punto','Ben':'Multipla','Charlie':'Golf','Debbie':'107','Emily':'A1'}
nuovi_proprietari={'Ben':'Polo','Fred':'Octavia','Grace':'Yaris','Hugh':'Clio'}
dizionario_auto.update(nuovi_proprietari)
print('il registro proprietari/auto aggiornato è il seguente: ',dizionario_auto)
# Ben passa dall'avere una multipla ad una polo, in pratica è come se avessimo un ser

# Es_25 Dato il dataset dei proprietari di auto viene richiesto di mostrare i dati relativi a 3 clienti
dizionario_auto={'Ada': 'Punto', 'Ben': 'Multipla', 'Charlie': 'Golf', 'Debbie': '107', 'Emily': 'A1', 'Fred': 'Octavia', 'Grace': 'Yaris', 'Hugh': 'Clio'}
print(dizionario_auto['Hugh'])
print(dizionario_auto['Ada'])
print(dizionario_auto['Emily'])
print(dizionario_auto['Debbie'])

# Es_26 
dizionario_auto={'Ada': 'Punto', 'Ben': 'Multipla', 'Charlie': 'Golf', 'Debbie': '107', 'Emily': 'A1', 'Fred': 'Octavia', 'Grace': 'Yaris', 'Hugh': 'Clio'}
defeault='mancante'
print(dizionario_auto.get('Hugh',defeault))
print(dizionario_auto.get('Ada',defeault))
print(dizionario_auto.get('Debbie',defeault))
print(dizionario_auto.get('Jade',defeault))

# Es_27 stampare tutte le chiavi del dizionario
dizionario_auto={'Ada': 'Punto', 'Ben': 'Multipla', 'Charlie': 'Golf', 'Debbie': '107', 'Emily': 'A1', 'Fred': 'Octavia', 'Grace': 'Yaris', 'Hugh': 'Clio'}
print(dizionario_auto.keys())

# Es_28 Stampiamo tutti i valori del dizionario
diz={'a':121,'zy':3774,'qop':147726,'ab':325,'k':12,'clap':9}
print(diz.values())

# Es_29 utilizzando il metodo .item() stampare le coppie chiave-valore
diz={'a':121,'zy':3774,'qop':147726,'ab':325,'k':12,'clap':9}
print(diz.items())

# Es_30 utilizzando il metodo .values() calcolare max, min e somma
diz={'a':121,'zy':3774,'qop':147726,'ab':325,'k':12,'clap':9}
print(max(diz.values()))
print(sum(diz.values()))
print(min(diz.values()))

# Es_31 mediante ciclo for stampare cosa guida ogni persona
dizionario_auto={'Ada': 'Punto', 'Ben': 'Multipla', 'Charlie': 'Golf', 'Debbie': '107', 'Emily': 'A1', 'Fred': 'Octavia', 'Grace': 'Yaris', 'Hugh': 'Clio'}
for proprietario, auto in dizionario_auto.items():
    print(proprietario,'guida una', auto)

# Es_32 stampare tutte le auto che non sono 'multipla'
dizionario_auto={'Ada': 'Punto', 'Ben': 'Multipla', 'Charlie': 'Golf', 'Debbie': '107', 'Emily': 'A1', 'Fred': 'Octavia', 'Grace': 'Yaris', 'Hugh': 'Clio'}
for  auto in dizionario_auto.values():
    if auto!='Multipla':
        print(auto)

# Es_33 Innestare i vari dizionari
dizionario={}
dizionario['Ada']={'funko pop':10,'action figures':5,'manga':35}
dizionario['ben']={'funko pop':2,'action figures':6,'manga':40}
dizionario['Charlie']={'action figures':31,'graphic novels':18}
dizionario['Debbie']={'funko pop':1,'graphic novels':9,'manga':25,'action figures':2}
print(dizionario)

# Es_34 Innestare i vari dizionari
dizionario={}
dizionario['Ada']={'funko pop':10,'action figures':5,'manga':35}
dizionario['ben']={'funko pop':2,'action figures':6,'manga':40,'graphic novels':{'DC':2,'Marvel':0}}
dizionario['Charlie']={'action figures':31,'graphic novels':{'DC':10,'Marvel':8}}
dizionario['Debbie']={'funko pop':1,'graphic novels':{'DC':5,'Marvel':4},'manga':25,'action figures':2}
print(dizionario)

# Es_35 
dizionario={}
dizionario['Ada']={'funko pop':10,'action figures':5,'manga':35}
dizionario['Ben']={'funko pop':2,'action figures':6,'manga':40,'graphic novels':{'DC':2,'Marvel':0}}
dizionario['Charlie']={'action figures':31,'graphic novels':{'DC':10,'Marvel':8}}
dizionario['Debbie']={'funko pop':1,'graphic novels':{'DC':5,'Marvel':4},'manga':25,'action figures':2}
somma_maga=0
for collezionista in dizionario.values():
    somma_maga+=collezionista.get('manga',0)
print(somma_maga)
GN_DC=0
GN_M=0
for collezionista in dizionario.values():
    if 'graphic novels' in collezionista:
        GN=collezionista['graphic novels']
        if 'DC'in GN:
            GN_DC+=GN['DC']
print(GN_DC)
for collezionista in dizionario.values():
    if 'graphic novels' in collezionista:
        GN=collezionista['graphic novels']
        if 'Marvel'in GN:
            GN_M+=GN['Marvel']
totale_GN=GN_DC+GN_M
print(GN_M+GN_DC)
print('quanti funko pop ha Ada?',dizionario['Ada']['funko pop'])
print('quanti manga ha Ben?',dizionario['Ben']['manga'])
print('quante graphic novels della Marvel ha Debbie?',dizionario['Debbie']['graphic novels']['Marvel'])
print('quanti funko pop hanno in tutto Ada e ben?',dizionario['Ada']['funko pop']+dizionario['Ben']['funko pop'])
print('quanti funko pop ha Ada?',dizionario['Ada']['funko pop'])
print('quanti manga hanno in totale i collezionisti?',somma_maga)
print('quante graphic novels hanno in totale i collezionisti?',GN_DC)
print('quante graphic novels hanno in totale i collezionisti?',totale_GN)