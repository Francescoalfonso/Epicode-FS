import numpy as np
import pandas as pd
import random


# Es_9
lista=[10,22,21,8,9,9,42,3,18,11,5,4,30,12,29,37,31,7,2,26,8,6,4,33,15]
minimo=min(lista)
massimo=max(lista)
lista_array=np.array(lista)
matrice=lista_array.reshape(5,5)
matrice=(matrice-minimo)/(massimo-minimo)
print(matrice)
'''for i in lista:
    operazione=(i-minimo)/(massimo-minimo)
    print(operazione)'''