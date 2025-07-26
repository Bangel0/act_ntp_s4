#Ejercicio 1: Filtrado de Números Pares
"""Crea una función que reciba una lista de números y use un ciclo for para devolver una nueva lista con solo los números pares. Prueba la función con la lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]."""


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #lista de números a filtrar

def filtrar_pares(lista):
    """Filtra los números pares de una lista."""
    pares = []  #lista para almacenar los números pares
    for numero in lista:
        if numero % 2 == 0:   #verifica si el número es par
            pares.append(numero)
    return pares   
print(filtrar_pares(numeros))
