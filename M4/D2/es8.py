stringa=input('inseire stringa da valutare: ')
if len(stringa)<=8 and len(stringa)>=5:
    print('la stringa comprende tra i 5 e gli 8 caratteri')
else:
    if len(stringa)<5:
        print('la stringa ha meno di 5 caratteri')
    else:
        print('la stringa ha più di 8 caratteri')