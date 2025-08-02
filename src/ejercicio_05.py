"""Implementa una función que reciba una lista de palabras y use ciclos anidados para encontrar y devolver todas las palabras que contienen una letra específica ingresada por el usuario."""

l_palabras=["hooola","jooooputa"]
def f(l_palabras):
    LETRA=input("Letra a buscar")
    for palabra in l_palabras:
        for letra in palabra:
            if LETRA == letra:
                print(palabra)
                break
    
    
f(l_palabras)