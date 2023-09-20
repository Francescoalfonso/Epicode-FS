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