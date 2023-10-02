import json
import numpy as np
import pandas as pd

# Esercizio 3
insurance=pd.read_csv('insurance.csv')
print("il dataset\'insurance.csv\'contiene i seguenti dati:\n", insurance)
print('il dataset ha il seguente numero di righe e colonne',insurance.shape)
print('mostriamo 10 righe a caso in modo da dare una panoramica del dataset', insurance.sample(10))
print('le colonne del dataset sono:', insurance.columns)
# Punto 1
media_charges_regione=insurance.groupby('region')['charges'].mean()
print('le medie di "charges" rispetto a "region" vengono riportate di seguito:',media_charges_regione)
# Punto 2
media_charges_smoker = insurance.groupby('smoker')['charges'].mean()
print('le medie di "smoker" rispetto a "region" vengono riportate di seguito:',media_charges_smoker)
# Punto 3
media_charges_sex = insurance.groupby('sex')['charges'].mean()
print('le medie di "sex" rispetto a "region" vengono riportate di seguito:',media_charges_sex)
# Punto 4
bmi_stats = insurance['bmi'].describe()
print("Di seguito vengono riportate le statistiche relative a 'bmi'")
print(bmi_stats)
# Punto 5
quartili = np.percentile(insurance['bmi'], [25, 50, 75])
diff_quartili = insurance.groupby(pd.cut(insurance['bmi'], bins=[0, quartili[0], quartili[1], quartili[2], float('inf')]))['charges'].agg(['min', 'mean', 'max'])
print("\nDi seguito si riportano Minimo, Media e Massimo di \'charges\' rispetto ai diversi quartili di \'bmi\':")
print(diff_quartili)