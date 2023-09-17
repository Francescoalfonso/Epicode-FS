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

# Es_22 