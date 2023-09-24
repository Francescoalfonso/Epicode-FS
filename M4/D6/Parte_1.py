import numpy as np
import random
import pandas as pd

# Es_1 (La prima quadra corrisponde alla riga, la seconda alla colonna )
mat=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]]
mat=np.array(mat)
print(mat[0][2])

# Es_2 determinare la dimensione del nuovo array e come accedere al singolo elemento
linear_data=np.array([x for x in range(27)])
reshaped_data=linear_data.reshape((3,3,3))
print(reshaped_data[1][1][1])
print(len(reshaped_data))

# Es_3.1-3.2
store=['UL','UR','LL','LR']
clienti=[0,0,0,0]
store=np.array(store)
clienti=np.array(clienti)
iterazioni=100
for i in range(iterazioni):
    cliente=random.randint(0,1)
    posizione=random.randint(0,3)
    clienti[posizione]+=cliente
for i,j in zip(store,clienti):
    print('nello store',i,'sono andati',j,'clienti')
for i,j in zip(store,clienti):
    if j>=25:
        print("nello store",i,"sono andati più di 25 clienti, per l'esattezza ",j,'clienti')
    else:
        print("nello store",i,"sono andati meno di 25 clienti")
print('Il totale delle presenze è:',sum(clienti))

# Es_3.3
store=['UL','Uc','UR','ML','MC','MR','LL','LC','LR']
clienti=[0,0,0,0,0,0,0,0,0]
store=np.array(store)
clienti=np.array(clienti)
iterazioni=200
for i in range(iterazioni):
    cliente=random.randint(0,4)
    posizione=random.randint(0,8)
    clienti[posizione]+=cliente
for i,j in zip(store,clienti):
    print('nello store',i,'sono andati',j,'clienti')
for i,j in zip(store,clienti):
    if j>=25:
        print("nello store",i,"sono andati più di 25 clienti, per l'esattezza ",j,'clienti')
    else:
        print("nello store",i,"sono andati meno di 25 clienti")
print('Il totale delle presenze è:',sum(clienti))

# Es_4 Chiedere all'utente di inserire un numero e dividerlo per 5. Gestiamo correttamente le eccezioni
divisore=5
while True:
    try:
        x=float(input('inserire un intero:'))
        rapporto=x/divisore
        break
    except:
        print('il valore inserito no è corretto, ritenta')
print('il rapporto tra',x,'e',divisore,'è pari a:',rapporto)

# Es_5 Data una trave di lunghezza X occorre inserire y rivetti tutti alla stessa distanza
L_trave=28.75
n_rivetti=15
distanziamento=np.linspace(0,L_trave,15)
print(distanziamento)

# Es_6.1 
iris=pd.read_csv("iris.data")
print(iris.head())
print(iris.columns) #Come si può notare in tale versione le colonne non hanno i nomi

# Es_6.2 Aggiungere manualmente i nomi alle colonne 
iris=pd.read_csv("iris.data",header=None,names= ['sepal length','sepal width','petal length','petal width'])
print(iris.head())
print(iris.tail(10))
print(iris.describe())

# Es_6.3
vini=pd.read_csv("wine.csv")
print('le prime 5 righe',vini.head())
print('le ultime 5 righe',vini.tail())
print('riepilogo dati statistici',vini.describe())
# Se ora considerando solo le ultime 6 colonne l'esercizio precedente diviene
vini=pd.read_csv("wine.csv",usecols=[7,8,9,10,11,12])
print('le prime 5 righe',vini.head())
print('le ultime 5 righe',vini.tail())
print('consideriamo le ultime 6 colonne',vini.columns)
print('riepilogo dati statistici',vini.describe()) 

# Es_8
# metodo 1
lista=[1,1,1,1,5,1,1,1,20,-4,0,42]
array=np.array(lista)
matrice=array.reshape(3,4)
print(matrice)
# metodo 2
matrice=[[1,1,1,1],[5,1,1,1],[20,-4,0,42]]
matrix=np.array(matrice)
print(matrix)

# Es_9
lista=[10,22,21,8,9,9,42,3,18,11,5,4,30,12,29,37,31,7,2,26,8,6,4,33,15]
minimo=min(lista)
massimo=max(lista)
lista_array=np.array(lista)
matrice=lista_array.reshape(5,5)
print(matrice)
for i in lista:
    operazione=(i-minimo)/(massimo-minimo)
    print(operazione)
