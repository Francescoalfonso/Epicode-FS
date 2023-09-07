efficenza=18                                    # [km/l]
costo=1.87                                         # costo carburante [£/l]
viaggio=100                                     # lunghezza itinerario [km]
carburante=viaggio/efficenza                    # carburante necessario [l]
costo_viaggio =carburante*costo
print('£',costo_viaggio)