livello_serbatoio=float(input('inserire livello serbatoio'))
efficenza=float(input('inserire efficenza'))                                  # [km/l]
costo=float(input('inserire costo carburante'))                                      # costo carburante [£/l]
viaggio=float(input('inserire distanza viaggio '))                                     # lunghezza itinerario [km]
carburante_viaggio=viaggio/efficenza                    # carburante necessario [l]
costo_viaggio =carburante_viaggio*costo
autonomia=livello_serbatoio-carburante_viaggio
print('£',costo_viaggio)