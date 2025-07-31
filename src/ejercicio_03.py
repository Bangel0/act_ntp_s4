"""Crea una función que reciba dos listas de igual tamaño y use un ciclo for para combinarlas elemento por elemento en una nueva lista. Ejemplo: [1,2,3] + ['a','b','c'] = [1,'a',2,'b',3,'c']."""

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']  

def combinar_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener el mismo tamaño.")
    
    lista_combinada = []
    for i in range(len(lista1)):
        lista_combinada.append(lista1[i])
        lista_combinada.append(lista2[i])
    
    return lista_combinada

print(combinar_listas(lista1, lista2))