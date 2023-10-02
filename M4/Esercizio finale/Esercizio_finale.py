import pandas as pd
import numpy as np

covid_csv=pd.read_csv("owid-covid-data.csv")
# Punto 1
print('Dimensioni dataset:',covid_csv.shape)
print('Intestazioni dataset:',covid_csv.columns)

# Punto 2
filtro_continent_pieno=covid_csv['continent'].isnull()==False               # mi da True alle righe che non hanno continente vuoto   
selezione=covid_csv.loc[filtro_continent_pieno]
gb=selezione.groupby(['continent']).sum()[['new_cases']]                    # Per ottenere effettivamente i casi totali per singola nazione e poi continente vado a sommare i valori relativi ai nuovi casi
print(' casi totali raggruppati per singolo continente sono: ',gb)

# Punto 3
data_set=covid_csv
continente_1='Oceania'
continente_2='Africa'
def funzione(a,b,c):
    filtro_1=a['continent']==b
    filtro_2=a['continent']==c
    filtro_mondo=a['continent'].isnull()!=True  
    dataset_filtrato=a.loc[filtro_1 | filtro_2 ]
    dataset_non_filtrato=a.loc[filtro_mondo ]
    gb_3=dataset_filtrato.groupby('continent').sum('new_cases')
    gb_4=dataset_non_filtrato.groupby('continent').sum('new_cases')
    print('Confrontando i due continenti abbiamo seguenti descrittori statistici','\n',gb_3.describe())
    print('Considerando il dataset non filtrato abbiamo i seguenti descrittori statistici','\n',gb_4.describe())
funzione(data_set,continente_1,continente_2)

# Punto 4
continente_1='Oceania'
continente_2='Africa'
continente_3='Europe'
def funzione2(a,b,c,d):
    filtro_1=a['continent']==b
    filtro_2=a['continent']==c
    filtro_3=a['continent']==d
    filtro_mondo=a['continent'].isnull()!=True  
    dataset_filtrato=a.loc[filtro_1 | filtro_2 | filtro_3 ]
    dataset_non_filtrato=a.loc[filtro_mondo ]
    gb_3=dataset_filtrato.groupby('continent').sum('new_vaccinations')
    gb_4=dataset_non_filtrato.groupby('continent').sum('new_vaccinations')
    print(gb_3)
    print('Confrontando i tre continenti abbiamo seguenti descrittori statistici','\n',gb_3.describe())
    print('Considerando il dataset non filtrato abbiamo i seguenti descrittori statistici','\n',gb_4.describe())
funzione2(data_set,continente_1,continente_2,continente_3)
