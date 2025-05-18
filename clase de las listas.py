'''
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)

mi_lista.append(6)
print(mi_lista)

mi_lista.insert(0, 0)
print(mi_lista)

mi_lista.remove(3)
print(mi_lista)

print("El primer elemento es", mi_lista[0])
print("El ultimo elemento es", mi_lista[-1])



lista = [1, 2, 3, 5]
print(lista)

suma = 0

for i in lista:
    suma += i

print(suma)


lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = []

print(lista)

for i in lista:
    if i % 2 == 0:
        lista2.append(i)
    else:
        pass

print('\nLos numeros pares de la lista son')
print(lista2)



def ordenar_tupla(tupla):
    lista=list(tupla)
    lista.sort()
    tupla_ordenada = tuple(lista)
    return tupla_ordenada

tupla = (5, 3, 4, 6, 2)
tupla_ordenada = ordenar_tupla(tupla)
print('La tupla original es:', tupla)
print('La tupla ordenada es:', tupla_ordenada)


import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2  

    def circunferencia(self):
        return 2 * math.pi * self.radio 

# Crear el objeto
mi_circulo = Circulo(5)

print("Área:", mi_circulo.area())
print("Circunferencia:", mi_circulo.circunferencia())


def obtener_claves(diccionario):
    return list(diccionario.keys())


mi_diccionario = {'Nombre1': 'Pamela', 'Nombre2': 'Monica', 'Nombre3': 'Jessica'}
resultado = obtener_claves(mi_diccionario)
print(resultado)

'''


import datetime
import sys

class Usuario:
    def __init__(self, nombre, contraseña, es_admin=False):
        self.nombre = nombre
        self.contraseña = contraseña
        self.es_admin = es_admin

class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Venta:
    def __init__(self, id, nombre_cliente, productos, total):
        self.id = id
        self.nombre_cliente = nombre_cliente
        self.productos = productos
        self.total = total
        self.fecha = datetime.datetime.now()

class Ferreteria:
    def __init__(self):
        self.usuarios = {}
        self.inventario = {}
        self.ventas = []
        self.usuario_actual = None

    def inicializar_inventario(self):
        productos = [
            ("Martillo", 15.99, 50),
            ("Destornillador Phillips", 5.99, 100),
            ("Llave inglesa", 12.50, 30),
            ("Cinta métrica", 8.75, 75),
            ("Sierra de mano", 22.50, 25),
            ("Taladro eléctrico", 89.99, 15),
            ("Caja de clavos (100 unidades)", 3.50, 200),
            ("Pintura blanca (1 galón)", 29.99, 40),
            ("Brocha de 2 pulgadas", 4.50, 60),
            ("Nivel de burbuja", 9.99, 35)
        ]
        for id, (nombre, precio, stock) in enumerate(productos, start=1):
            self.inventario[id] = Producto(id, nombre, precio, stock)

    def agregar_usuario(self, nombre, contraseña, es_admin=False):
        self.usuarios[nombre] = Usuario(nombre, contraseña, es_admin)

    def login(self):
        nombre = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if nombre in self.usuarios and self.usuarios[nombre].contraseña == contraseña:
            self.usuario_actual = self.usuarios[nombre]
            print(f"Bienvenido, {nombre}!")
            return True
        print("Usuario o contraseña incorrectos.")
        return False

    def logout(self):
        self.usuario_actual = None
        print("Sesión cerrada.")

    def mostrar_inventario(self):
        print("\nInventario:")
        for producto in self.inventario.values():
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: ${producto.precio:.2f}, Stock: {producto.stock}")

    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese la cantidad en stock: "))
        id = max(self.inventario.keys()) + 1 if self.inventario else 1
        self.inventario[id] = Producto(id, nombre, precio, stock)
        print(f"Producto agregado con ID: {id}")

    def modificar_producto(self):
        id = int(input("Ingrese el ID del producto a modificar: "))
        if id in self.inventario:
            producto = self.inventario[id]
            producto.nombre = input(f"Ingrese el nuevo nombre ({producto.nombre}): ") or producto.nombre
            producto.precio = float(input(f"Ingrese el nuevo precio ({producto.precio}): ") or producto.precio)
            producto.stock = int(input(f"Ingrese el nuevo stock ({producto.stock}): ") or producto.stock)
            print("Producto modificado exitosamente.")
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self):
        id = int(input("Ingrese el ID del producto a eliminar: "))
        if id in self.inventario:
            del self.inventario[id]
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")

    def realizar_venta(self):
        if not self.usuario_actual:
            print("Debe iniciar sesión para realizar una venta")
            return

        nombre_cliente = input("Ingrese el nombre del cliente: ")

        productos = self.seleccionar_productos()
        if not productos:
            print("No se seleccionaron productos")
            return

        total = 0
        productos_vendidos = []
        for id_producto, cantidad in productos:
            producto = self.inventario[id_producto]
            total += producto.precio * cantidad
            producto.stock -= cantidad
            productos_vendidos.append((producto, cantidad))

        id_venta = len(self.ventas) + 1
        venta = Venta(id_venta, nombre_cliente, productos_vendidos, total)
        self.ventas.append(venta)
        print(self.generar_factura(venta))

    def seleccionar_productos(self):
        productos_seleccionados = []
        while True:
            self.mostrar_inventario()
            seleccion = input("Seleccione el ID del producto (o 'f' para finalizar): ")
            if seleccion.lower() == 'f':
                break
            try:
                id_producto = int(seleccion)
                if id_producto not in self.inventario:
                    print("Producto no válido. Intente de nuevo.")
                    continue
                cantidad = int(input("Ingrese la cantidad: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")
                    continue
                if cantidad > self.inventario[id_producto].stock:
                    print("Stock insuficiente.")
                    continue
                productos_seleccionados.append((id_producto, cantidad))
            except ValueError:
                print("Entrada no válida. Intente de nuevo.")
        return productos_seleccionados

    def generar_factura(self, venta):
        factura = f"\nFactura #{venta.id}\n"
        factura += f"Fecha: {venta.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
        factura += f"Cliente: {venta.nombre_cliente}\n"
        factura += "Productos:\n"
        for producto, cantidad in venta.productos:
            factura += f"  {producto.nombre} x {cantidad}: ${producto.precio * cantidad:.2f}\n"
        factura += f"Total: ${venta.total:.2f}"
        return factura

    def mostrar_historial_ventas(self):
        if not self.usuario_actual or not self.usuario_actual.es_admin:
            print("No tiene permisos para ver el historial de ventas")
            return

        print("\nHistorial de Ventas:")
        for venta in self.ventas:
            print(f"Venta #{venta.id} - Cliente: {venta.nombre_cliente}, Total: ${venta.total:.2f}, Fecha: {venta.fecha.strftime('%Y-%m-%d %H:%M:%S')}")

def menu_principal(ferreteria):
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if ferreteria.login():
                menu_usuario(ferreteria)
        elif opcion == "2":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            sys.exit()
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_usuario(ferreteria):
    while True:
        print("\n--- Menú de Usuario ---")
        print("1. Mostrar inventario")
        print("2. Realizar venta")
        if ferreteria.usuario_actual.es_admin:
            print("3. Agregar producto")
            print("4. Modificar producto")
            print("5. Eliminar producto")
            print("6. Mostrar historial de ventas")
        print("7. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ferreteria.mostrar_inventario()
        elif opcion == "2":
            ferreteria.realizar_venta()
        elif opcion == "3" and ferreteria.usuario_actual.es_admin:
            ferreteria.agregar_producto()
        elif opcion == "4" and ferreteria.usuario_actual.es_admin:
            ferreteria.modificar_producto()
        elif opcion == "5" and ferreteria.usuario_actual.es_admin:
            ferreteria.eliminar_producto()
        elif opcion == "6" and ferreteria.usuario_actual.es_admin:
            ferreteria.mostrar_historial_ventas()
        elif opcion == "7":
            ferreteria.logout()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Inicialización y ejecución del programa
ferreteria = Ferreteria()
ferreteria.inicializar_inventario()
ferreteria.agregar_usuario("admin", "admin123", True)
ferreteria.agregar_usuario("vendedor", "vendedor123")

menu_principal(ferreteria)


