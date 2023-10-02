import json
import numpy as np
import pandas as pd
# Es_1
file_amazon=pd.read_csv("amazon.csv")
print(file_amazon.shape)
print(file_amazon.sample(10))
print(file_amazon.columns)
freq=file_amazon['Positive'].value_counts()
print(freq)
valutazioni=file_amazon['Positive']
print(valutazioni)
i=0
for j in valutazioni:
    if j==1:
        i+=1
print(i)
if i>=len(valutazioni)/2:
    print('valutazioni prevalentemente positive')
else:
    print('valutazioni prevalentemente negative')
# punto 4
colonna="reviewText"
ricerca_valore='game'
filtro_valore=file_amazon[colonna].str.contains(ricerca_valore, case=False)
risultato=file_amazon[filtro_valore].sum()
print(risultato)
# Punto 5
colonna="reviewText"
ricerca_valore='app'
filtro_valore=file_amazon[colonna].str.contains(ricerca_valore, case=False)
risultato=file_amazon[filtro_valore].sum()
print(risultato)
# Punto 6/7/8
filtro_recommend=file_amazon['reviewText'].str.contains('recommend', case=False)
filtro_positivo=file_amazon['Positive']==True
filtro_negativo=file_amazon['Positive']==False
risultato_1=file_amazon[filtro_positivo&filtro_recommend].value_counts()
risultato_2=file_amazon[filtro_negativo]
print(risultato_1)
print(risultato_2)
# Punto 9
filtro_all=file_amazon['reviewText'].str.contains('kindle', case=False)
filtro=file_amazon['reviewText'].str.contains('kindle', case=False)
risultato_overall=file_amazon[filtro_all]
filtro_positivo=file_amazon['Positive']==True
risultato_filtrato=file_amazon[filtro&filtro_positivo]
print(risultato_overall.shape[0]-risultato_filtrato.shape[0])
if risultato_overall.shape[0]<risultato_filtrato.shape[0]:
    print('negative')
else:
    print('positive')

# Es_2
db=pd.read_csv('diabetes.csv',sep=',')
diabete=pd.DataFrame(db)
print(diabete.shape)
print(diabete.sample(5))
print(diabete.info())
print(diabete.describe())
filtro_1=diabete.iloc[:,7]<20
print(filtro_1)
filtro_2=diabete.iloc[:,7].between(20,30)
print(filtro_2)
filtro_3=diabete.iloc[:,7].between(30,40)
print(filtro_3)
filtro_4=diabete.iloc[:,7].between(40,50)
print(filtro_4)
filtro_5=diabete.iloc[:,7]>50
print(filtro_5)

subset = diabete[filtro_3]
print(subset.iloc[:,7])

applied_filter = filtro_5
media_press_sang = diabete[applied_filter].iloc[:,2].mean()
print(media_press_sang)

import math as m

for x in range(0,diabete.iloc[:,7].max()):
    filtro_eta = diabete.iloc[:,7] == x
    media_press_sang = diabete[filtro_eta].iloc[:,2].mean()
    if m.isnan(media_press_sang):
        pass
    else:
        print("Per un paziente di età pari a:",x,"la pressione sanguigna media è uguale a:",round(media_press_sang,2))

