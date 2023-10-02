import json
import numpy as np
import pandas as pd

pokemon = pd.read_csv("pokemon.csv", sep=",")
print(pokemon)

print(pokemon.shape)
print(pokemon.sample(10))
print(pokemon.columns)

# Confronto dell'indice con la colonna #
if pokemon['#'][-1] == pokemon.shape[0]-1:
    print("I valori finali della colonna indice e della colonna \'#\' coincidono.")
else:
    pokemon.set_index('#')
    print("I valori finali della colonna indice e della colonna \'#\' non coincidono.\nLa colonna '#' è stata impostata come indice.")

# Confronto alternativo
if len(set(pokemon['Name'])) == pokemon.shape[0]-1:
    print("I valori finali della colonna indice e della colonna \'#\' coincidono.")
else:
    pokemon.set_index('Name')
    print("I valori finali della colonna indice e della colonna \'#\' non coincidono.\nLa colonna '#' è stata impostata come indice.")

# Ci sono ripetizioni, ovvero righe che si riferiscono allo stesso Pokémon?
duplicati = pokemon.duplicated()
if duplicati.empty:
    print("Non ci sono ripetizioni nel dataset.")
else:
    print("Ci sono ripetizioni nel dataset.")

# Per ogni tipo in Type 1 quanti ce ne sono?
contegg_pokemon_type1 = pokemon["Type 1"].value_counts()
print("\nConteggio dei Pokémon \'Type 1\':\n")
print(contegg_pokemon_type1)

# Quali sono i Pokémon leggendari?
pokemon_legg = pokemon[pokemon['Legendary'] == True]
print("\nDi seguito si riportano i nomi di tutti i Pokémon Leggendari:\n")
print(pokemon_legg[['Name', 'Type 1', 'Legendary']])

# E quali sono i leggendari di tipo 1 Grass?
pokemon_legg = pokemon[pokemon['Legendary'] == True]
legendary_grass = pokemon_legg[pokemon_legg['Type 1'] == 'Grass']
print("\nDi seguito di riportano i nomi di tutti i Pokémon Leggendari di tipo \'Erba\':\n")
print(legendary_grass[['Name', 'Type 1', 'Legendary']])

# E leggendari di tipo 1 Ice o Fire? [Inclusi gli Electric, extra]
pokemon_legg = pokemon[pokemon['Legendary'] == True]
legendary_ice_fire = pokemon_legg[(pokemon_legg['Type 1'] == 'Ice') | (pokemon_legg['Type 1'] == 'Fire') | (pokemon_legg['Type 1'] == 'Electric')]
print("\nDi seguito di risportano i nomi di tutti i Pokémon Leggendari di tipo \'Ghiaccio\' o \'Fuoco\':\n")
print(legendary_ice_fire[['Name', 'Type 1', 'Legendary']])

# Ordiniamo il dataset per la colonna Name
pokemon.sort_values(by='Name', inplace=True)

# Trasformiamo Name nell'indice
pokemon.set_index('Name', inplace=True)

# Come accediamo alle statistiche di tutti i Pokémon il cui nome inizia per D?
nomi_pokemon_iniziale_d = pokemon[pokemon["Name"].str.startswith('D')]
print("\nDi seguito si riportano i nomi dei Pokémon il cui nome inizia per 'D':\n")
print(nomi_pokemon_iniziale_d[['Name', 'Type 1', 'Legendary']])

# Quali sono i Pokémon della prima generazione con attacco > 50 e HP < 60?
filtro_generazione = pokemon[pokemon['Generation'] == 1]
filtro_pokemon = filtro_generazione[(filtro_generazione['Attack'] > 50) & (filtro_generazione['HP'] < 60)]
print("\nDi seguito si riportano i nomi dei Pokémon di prima generazione con attacco > 50 e HP < 60:\n")
print(filtro_pokemon[['Name', 'Type 1', 'Legendary']])

# Ci sono dati nulli?
null_data = pokemon.isnull().sum()
print("\nDi seguito si riporta il conteggio dei dati nulli per ogni colonna all'interno del dataset:\n")
print(null_data)