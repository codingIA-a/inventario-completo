

"""
crear un simulador de inventario para una tienda ficticia. 
El programa debe permitir agregar productos y mostrar el inventario .
Para resolver esto deberá:
1.-Crear  una función para agregar productos al inventario.
2.-Crear una función para mostrar TODO el inventario.
3.-

"""

import time, os
inventario = {
    'laptop' : {'precio': 1000, 'cantidad':10},
    'smartphone':{'precio' : 500, 'cantidad':20},
    'teclado': {'precio': 50, 'cantidad': 30}
}
#Crear una función que reciba 3 parámetros. El primer parámetro será el nombre del producto, 
# el segundo el precio y el tercero la cantidad
#La función deberá validar si el parametro que representa el nombre del producto existe dentro del inventario
#Si no existe deberá agregar el nuevo producto con su respectivo precio y cantidad
#Si el producto existe, deberá sumar el stock existente y actualizar el precio de ser necesario
def agregar_producto(nombre, precio, cantidad):
    if nombre in inventario:
        inventario[nombre]["precio"] = precio
        inventario[nombre]["cantidad"] += cantidad
    else:
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}
       

def mostrar_inventario():
    print("Inventario:")
    for producto, detalles in inventario.items():
        print(f"{producto}: Precio ${detalles['precio']}, Cantidad en stock: {detalles['cantidad']}")

def menu_principal():
    while True:
        print("\n----- Menú Principal -----")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad en stock: "))
            agregar_producto(nombre, precio, cantidad)
        elif opcion == "2":
            os.system('clear')
            mostrar_inventario()
            time.sleep(10)
            print('\n')

        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del menú.")

if __name__ == "__main__":
    menu_principal()


