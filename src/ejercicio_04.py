"""Desarrolla una función que simule un carrito de compras. Usa una lista para almacenar productos y un ciclo while para mostrar un menú que permita agregar, eliminar, mostrar productos y calcular el total."""

carrito = []  # Lista para almacenar productos
precios = {}  # Diccionario para almacenar precios de productos

def mostrar_menu():
    print("\nMenú del Carrito de Compras:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos")
    print("4. Calcular total")
    print("5. Salir")
def agregar_producto():
    producto = input("Ingresa el nombre del producto: ")
    precio = float(input(f"Ingresa el precio de {producto}: "))
    carrito.append(producto)
    precios[producto] = precio
    print(f"{producto} agregado al carrito.")

def eliminar_producto():
    producto = input("Ingresa el nombre del producto a eliminar: ")
    if producto in carrito:
        carrito.remove(producto)
        del precios[producto]
        print(f"{producto} eliminado del carrito.")
    else:
        print(f"{producto} no se encuentra en el carrito.")
def mostrar_productos():
    if carrito:
        print("\nProductos en el carrito:")
        for producto in carrito:
            print(f"{producto}: ${precios[producto]:.2f}")
    else:
        print("El carrito está vacío.")

def calcular_total():
    total = sum(precios[producto] for producto in carrito)
    print(f"Total del carrito: ${total:.2f}")

  # Bucle principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        mostrar_productos()
    elif opcion == "4":
        calcular_total()
    elif opcion == "5":
        print("Gracias por usar el carrito de compras. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")


