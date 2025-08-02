"""Crea una función que genere una tupla con las coordenadas (x, y) de 10 puntos aleatorios. Usa un ciclo for para calcular cuáles puntos están dentro de un círculo de radio 5 centrado en el origen."""

import random

def f():
    coords= []
    ret = []
    for i in range(11):
        l_temp=[random.randint(0,10),random.randint(0,10)]
        coords.append(l_temp)
    t_coords=tuple(coords)
    for x,y in t_coords:
        if x<=5 and y<=5:
            t=[x,y]
            ret.append(t)
        if not ret:
            return False,[]
    return True,ret

for i in range(1,20):
    ret,coords=f()
    if not ret:
        continue
    print(f"Esta coordenada se encuentra a 5 puntos del centro {coords}")