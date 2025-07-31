#Ejercicio 2: Calificaciones del Usuario
"""Crea una función que solicite al usuario ingresar calificaciones usando un ciclo while hasta que escriba 'fin'. Almacena las calificaciones en una lista y calcula el promedio, la nota más alta y más baja."""

calificaciones = []  #lista para almacenar las calificaciones

while True:
    ingreso = input("Ingresa una calificación (o escribe 'fin' para terminar): ")
    if ingreso.lower() == 'fin':  #verifica si el usuario quiere terminar
        if ingreso.lower() == 'fin':
            print(f"Promedio de notas es igual { sum(calificaciones) / len(calificaciones) if calificaciones else 0}")
            print(f"La nota más alta es {max(calificaciones) if calificaciones else 'N/A'}")
            print(f"La nota más baja es {min(calificaciones) if calificaciones else 'N/A'}")
        break
    try:
        calificacion = float(ingreso)  #convierte la entrada a float
        calificaciones.append(calificacion)  #agrega la calificación a la lista.
        print(f"Calificación agregada: {calificacion}")
    except NameError:
        print("Por favor ingrese un valor numérico válido.")


