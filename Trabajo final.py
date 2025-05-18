import os
from decimal import Decimal
import datetime
import mysql.connector
import sys

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("\nPresiona Enter para volver al menú principal...")




# Clase para representar un usuario
class Usuario:
    def __init__(self, id, nombre, contraseña, es_admin=False):
        self.id = id
        self.nombre = nombre
        self.contraseña = contraseña
        self.es_admin = es_admin
        
# Clase para representar un producto
class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
# Clase para representar una venta
class Venta:
    def __init__(self, id, nombre_cliente, productos, total):
        self.id = id
        self.nombre_cliente = nombre_cliente
        self.productos = productos
        self.total = total
        self.fecha = datetime.datetime.now()
        
# Clase principal que maneja la lógica de la ferretería
class Ferreteria:
    def __init__(self):
        # Conexión a la base de datos MySQL
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pbv.120803",
            database="ferreteria"
        )
        self.cursor = self.conn.cursor(buffered=True)
        self.usuario_actual = None
        
     
    def inicializar_inventario(self):
        # Verificar si la tabla Productos ya tiene datos
        self.cursor.execute("SELECT COUNT(*) FROM Productos")
        (count,) = self.cursor.fetchone()
    
        if count == 0:
            # Lista de productos iniciales
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

            # Insertar productos en la base de datos
            for nombre, precio, stock in productos:
                self.cursor.execute("INSERT INTO Productos (nombre, precio, stock) VALUES (%s, %s, %s)", (nombre, precio, stock))
            self.conn.commit()
            print("Inventario inicializado exitosamente.")
        else:
            print("El inventario ya está inicializado.")
            

    def agregar_usuario(self, nombre, contraseña, es_admin=False):
        # Agregar un nuevo usuario a la base de datos
        self.cursor.execute("INSERT INTO Usuarios (nombre, contraseña, es_admin) VALUES (%s, %s, %s)", (nombre, contraseña, es_admin))
        self.conn.commit()
    
        
    def login(self):
    # Iniciar sesión de usuario
        while True:
            nombre = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            self.cursor.execute("SELECT * FROM Usuarios WHERE nombre = %s", (nombre,))
            usuario = self.cursor.fetchone()
            
            if usuario:
                if usuario[2] == contraseña:
                    self.usuario_actual = Usuario(usuario[0], usuario[1], usuario[2], usuario[3])
                    print(f"¡Bienvenido, {nombre}!")
                    return True
                else:
                    print("Contraseña incorrecta. Por favor, intente de nuevo.")
            else:
                # Verificamos si la contraseña ingresada es incorrecta aunque el usuario no exista
                self.cursor.execute("SELECT * FROM Usuarios WHERE contraseña = %s", (contraseña,))
                user_with_password = self.cursor.fetchone()
                if user_with_password:
                    print("Usuario incorrecto. Por favor, intente de nuevo.")
                else:
                    print("Usuario y contraseña incorrectos. Por favor, intente de nuevo.")
            
            print("")

    def logout(self):
        # Cerrar sesión de usuario
        self.usuario_actual = None
        print("Sesión cerrada.")

    def mostrar_inventario(self):
        # Mostrar inventario de productos
        print("\nInventario:")
        try:
            # Cerrar el cursor existente y crear uno nuevo
            if self.cursor:
                self.cursor.close()
            self.cursor = self.conn.cursor(buffered=True)
            
            self.cursor.execute("SELECT * FROM Productos")
            productos = self.cursor.fetchall()
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}, Stock: {producto[3]}")

        except mysql.connector.Error as err:
            print(f"Error al mostrar el inventario: {err}")

        finally:
            # Asegurarse de que todos los resultados se consuman
            if self.cursor.with_rows:
                self.cursor.fetchall()
            self.conn.commit()
            

    def agregar_producto(self):
        # Agregar un nuevo producto al inventario
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese la cantidad en stock: "))
        self.cursor.execute("INSERT INTO Productos (nombre, precio, stock) VALUES (%s, %s, %s)", (nombre, precio, stock))
        self.conn.commit()
        print("Producto agregado exitosamente.")

    def modificar_producto(self):
        # Modificar los detalles de un producto existente
        id = int(input("Ingrese el ID del producto a modificar: "))
        self.cursor.execute("SELECT * FROM Productos WHERE id = %s", (id,))
        producto = self.cursor.fetchone()
        if producto:
            nombre = input(f"Ingrese el nuevo nombre ({producto[1]}): ") or producto[1]
            precio = float(input(f"Ingrese el nuevo precio ({producto[2]}): ") or producto[2])
            stock = int(input(f"Ingrese el nuevo stock ({producto[3]}): ") or producto[3])
            self.cursor.execute("UPDATE Productos SET nombre = %s, precio = %s, stock = %s WHERE id = %s", (nombre, precio, stock, id))
            self.conn.commit()
            print("Producto modificado exitosamente.")
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self):
        # Eliminar un producto del inventario
        id = int(input("Ingrese el ID del producto a eliminar: "))
        self.cursor.execute("DELETE FROM Productos WHERE id = %s", (id,))
        self.conn.commit()
        print("Producto eliminado exitosamente.")

    def realizar_venta(self):
        # Realizar una venta de productos
        if not self.usuario_actual:
            print("Debe iniciar sesión para realizar una venta")
            return

        nombre_cliente = input("Ingrese el nombre del cliente: ")
        productos = self.seleccionar_productos()
        if not productos:
            print("No se seleccionaron productos")
            return

        total = Decimal('0')
        productos_vendidos = []
        for id_producto, cantidad in productos:
            self.cursor.execute("SELECT * FROM Productos WHERE id = %s", (id_producto,))
            producto = self.cursor.fetchone()
            total += Decimal(str(producto[2])) * Decimal(str(cantidad))
            self.cursor.execute("UPDATE Productos SET stock = stock - %s WHERE id = %s", (cantidad, id_producto))
            productos_vendidos.append((producto, cantidad))

        self.cursor.execute("INSERT INTO Ventas (nombre_cliente, total, fecha) VALUES (%s, %s, %s)",
                            (nombre_cliente, str(total), datetime.datetime.now()))
        id_venta = self.cursor.lastrowid
        for producto, cantidad in productos_vendidos:
            self.cursor.execute("INSERT INTO DetallesVentas (id_venta, id_producto, cantidad) VALUES (%s, %s, %s)",
                                (id_venta, producto[0], cantidad))
        self.conn.commit()
        print(self.generar_factura(Venta(id_venta, nombre_cliente, productos_vendidos, total)))

    def seleccionar_productos(self):
        # Seleccionar productos para la venta
        productos_seleccionados = []
        while True:
            self.mostrar_inventario()
            seleccion = input("Seleccione el ID del producto (o 'f' para finalizar): ")
            if seleccion.lower() == 'f':
                break
            try:
                id_producto = int(seleccion)
                self.cursor.execute("SELECT * FROM Productos WHERE id = %s", (id_producto,))
                producto = self.cursor.fetchone()
                if not producto:
                    print("Producto no válido. Intente de nuevo.")
                    continue
                cantidad = int(input("Ingrese la cantidad: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")
                    continue
                if cantidad > producto[3]:
                    print("Stock insuficiente.")
                    continue
                productos_seleccionados.append((id_producto, cantidad))
            except ValueError:
                print("Entrada no válida. Intente de nuevo.")
        return productos_seleccionados

    def agregar_usuario(self, nombre, contraseña, es_admin=False):
        self.cursor.execute("INSERT INTO Usuarios (nombre, contraseña, es_admin) VALUES (%s, %s, %s)", (nombre, contraseña, es_admin))
        self.conn.commit()
        print(f"Usuario '{nombre}' agregado exitosamente.")
        pause()

    def modificar_usuario(self):
        nombre = input("Ingrese el nombre del usuario a modificar: ")
        self.cursor.execute("SELECT * FROM Usuarios WHERE nombre = %s", (nombre,))
        usuario = self.cursor.fetchone()
        if usuario:
            nueva_contraseña = input("Ingrese la nueva contraseña (deje en blanco para no cambiar): ")
            es_admin = input("¿Es administrador? (s/n): ").lower() == 's'
            if nueva_contraseña:
                self.cursor.execute("UPDATE Usuarios SET contraseña = %s, es_admin = %s WHERE nombre = %s", (nueva_contraseña, es_admin, nombre))
            else:
                self.cursor.execute("UPDATE Usuarios SET es_admin = %s WHERE nombre = %s", (es_admin, nombre))
            self.conn.commit()
            print(f"Usuario '{nombre}' modificado exitosamente.")
        else:
            print("Usuario no encontrado.")

    def eliminar_usuario(self):
        nombre = input("Ingrese el nombre del usuario a eliminar: ")
        self.cursor.execute("DELETE FROM Usuarios WHERE nombre = %s", (nombre,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Usuario '{nombre}' eliminado exitosamente.")
        else:
            print("Usuario no encontrado.")

    def generar_factura(self, venta):
        # Generar factura para la venta
        subtotal = venta.total
        itbis = subtotal * Decimal('0.18')
        descuento = Decimal('0')  # Puedes implementar lógica de descuento aquí si lo deseas
        total = subtotal + itbis - descuento

        factura = f"\nFactura #{venta.id}\n"
        factura += f"Fecha: {venta.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
        factura += f"Cliente: {venta.nombre_cliente}\n"
        factura += "Productos:\n"
        for producto, cantidad in venta.productos:
            factura += f"  {producto[1]} x {cantidad}: ${producto[2]:.2f} c/u \n"
        factura += f"Subtotal: ${subtotal:.2f}\n"
        factura += f"ITBIS (18%): ${itbis:.2f}\n"
        factura += f"Descuento: ${descuento:.2f}\n"
        factura += f"Total: ${total:.2f}"
        return factura

    def mostrar_historial_ventas(self):
        # Mostrar historial de ventas (solo para administradores)
        if not self.usuario_actual or not self.usuario_actual.es_admin:
            print("No tiene permisos para ver el historial de ventas")
            return

        print("\nHistorial de Ventas:")
        self.cursor.execute("SELECT * FROM Ventas")
        for venta in self.cursor.fetchall():
            print(f"Venta #{venta[0]} - Cliente: {venta[1]}, Total: ${venta[2]:.2f}, Fecha: {venta[3].strftime('%Y-%m-%d %H:%M:%S')}")


            # Obtener los detalles de la venta
            self.cursor.execute("""
                SELECT p.nombre, p.precio, dv.cantidad
                FROM DetallesVentas dv
                JOIN Productos p ON dv.id_producto = p.id
                WHERE dv.id_venta = %s
            """, (venta[0],))
            
            detalles = self.cursor.fetchall()
            print("  Productos:")
            for detalle in detalles:
                nombre, precio, cantidad = detalle
                total_producto = precio * cantidad
                print(f"    {nombre} x {cantidad}: ${precio:.2f} c/u - Total: ${total_producto:.2f}\n")

    def cerrar_conexion(self):
        # Cerrar la conexión a la base de datos
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


            
# Menú principal del sistema
def menu_principal(ferreteria):
    while True:
        limpiar_pantalla()
        print("\n**** Menú Principal ****")
        print("1. Iniciar sesión")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if ferreteria.login():
                menu_usuario(ferreteria)
        elif opcion == "2":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            ferreteria.cerrar_conexion()
            sys.exit()
        else:
            print("Opción no válida. Intente de nuevo.")
            
# Menú de opciones para el usuario
def menu_usuario(ferreteria):
    while True:
        pausa()
        limpiar_pantalla()
        print("\n**** Menú de Usuario ****")
        print("1. Mostrar inventario")
        print("2. Realizar venta")
        if ferreteria.usuario_actual.es_admin:
            print("3. Agregar producto")
            print("4. Modificar producto")
            print("5. Eliminar producto")
            print("6. Mostrar historial de ventas")
            print("7. Agregar usuario")
            print("8. Modificar usuario")
            print("9. Eliminar usuario")
        print("0. Cerrar sesión")
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
        elif opcion == "7" and ferreteria.usuario_actual.es_admin:
            nombre = input("Ingrese el nombre del nuevo usuario: ")
            contraseña = input("Ingrese la contraseña del nuevo usuario: ")
            es_admin = input("¿Es administrador? (s/n): ").lower() == 's'
            ferreteria.agregar_usuario(nombre, contraseña, es_admin)
        elif opcion == "8" and ferreteria.usuario_actual.es_admin:
            ferreteria.modificar_usuario()
        elif opcion == "9" and ferreteria.usuario_actual.es_admin:
            ferreteria.eliminar_usuario()
        elif opcion == "0":
            ferreteria.logout()
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            

# Inicialización y ejecución del programa
try:
    # Crear instancia de la clase Ferreteria
    ferreteria = Ferreteria()
    ferreteria.inicializar_inventario()


    # Ejecutar el menú principal
    menu_principal(ferreteria)
    
# Manejo de errores
except Exception as e:
    
    print(f"Se produjo un error: {e}")
    input("Presione Enter para salir...")
    





