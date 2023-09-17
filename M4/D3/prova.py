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