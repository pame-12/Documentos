print('Pamela Blanco Vincent')
print('2023-1668')

print("\n Ejercicio 1: ")
import math
class punto:
    def  __init__(self, x, y):
        self.x=x
        self.y=y

    def distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return math.sqrt(dx**2 + dy**2)

    def desplazar(self, dx, dy):
        self.x += dx
        self.y += dy
        return self.x, self.y 

    def __str__(self):
        return f"({self.x}, {self.y})"

mi_punto = punto(4, 2)
otro_punto = punto(1, 1)

print(f"Mi punto: {mi_punto}")
print(f"Otro punto: {otro_punto}")

# Calcular la distancia
dist = mi_punto.distancia(otro_punto)
print(f"Distancia entre mi punto y otro punto: {dist}")

# Desplazar mi punto
mi_punto.desplazar(3, 4)
print(f"Mi punto después de desplazar: {mi_punto}")




print("\n Ejercicio 2: ")

class Rectangulo:
    def __init__(self):
        self.longitud = float(input("Introduce el valor de la longitud: "))
        self.ancho = float(input("Introduce el valor del ancho: "))

    def area(self):
        return self.longitud * self.ancho

    def perimetro(self):
        return 2 * (self.longitud + self.ancho)


mi_rectangulo = Rectangulo()
print(f"El area del rectángulo es : {mi_rectangulo.area()}")
print(f"El perímetro del rectángulo es : {mi_rectangulo.perimetro()}")


print("\n Ejercicio 3: ")

class Estudiante:
    def __init__(self):
        self.nombre = input("Introduce el nombre del estudiante: ")
        self.edad = int(input("Introduce la edad del estudiante: "))
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def __str__(self):
        promedio = self.calcular_promedio()
        return f"El/La estudiante de Nombre: {self.nombre}, de edad: {self.edad}, tiene un promedio de: {promedio:.2f}"


estudiante1=Estudiante()
estudiante1.agregar_calificacion(90)
estudiante1.agregar_calificacion(95)
estudiante1.agregar_calificacion(93)
print(estudiante1)


print("\n Ejercicio 4: ")
class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo_total = 0.0
        self.cuentas = {}

    def agregar_cuenta(self, numero_cuenta):
        if numero_cuenta in self.cuentas:
            print(f"La cuenta {numero_cuenta} ya existe.")
        else:
            self.cuentas[numero_cuenta] = 0.0
            print(f"Cuenta {numero_cuenta} agregada exitosamente.")

    def realizar_deposito(self, numero_cuenta, cantidad):
        if numero_cuenta in self.cuentas:
            self.cuentas[numero_cuenta] += cantidad
            self.saldo_total += cantidad
            print(f"Depósito de {cantidad} en la cuenta {numero_cuenta} realizado exitosamente.")
        else:
            print(f"La cuenta {numero_cuenta} no existe.")

    def retirar_dinero(self, numero_cuenta, cantidad):
        if numero_cuenta in self.cuentas:
            if self.cuentas[numero_cuenta] >= cantidad:
                self.cuentas[numero_cuenta] -= cantidad
                self.saldo_total -= cantidad
                print(f"Retiro de {cantidad} en la cuenta {numero_cuenta} realizado exitosamente.")
            else:
                print(f"Fondos insuficientes en la cuenta {numero_cuenta}.")
        else:
            print(f"La cuenta {numero_cuenta} no existe.")

    def mostrar_informacion(self):
        print(f"Banco: {self.nombre}")
        print(f"Saldo total: {self.saldo_total}")
        print("Cuentas y saldos:")
        for cuenta, saldo in self.cuentas.items():
            print(f"Cuenta {cuenta}: {saldo}")

# Ejemplo de uso:
mi_banco = Banco("Banco Central")

# Agregar cuentas
mi_banco.agregar_cuenta("123")
mi_banco.agregar_cuenta("456")

# Realizar depósitos
mi_banco.realizar_deposito("123", 1000)
mi_banco.realizar_deposito("456", 2000)

# Retirar dinero
mi_banco.retirar_dinero("123", 500)
mi_banco.retirar_dinero("456", 1000)

# Mostrar información del banco
mi_banco.mostrar_informacion()
    

print("\n Ejercicio 5: ")
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        if producto in self.productos:
            print(f"El producto '{producto}' ya está en la tienda.")
        else:
            self.productos.append(producto)
            print(f"Producto '{producto}' agregado exitosamente.")

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"Producto '{producto}' eliminado exitosamente.")
        else:
            print(f"El producto '{producto}' no se encuentra en la tienda.")

    def mostrar_productos(self):
        if self.productos:
            print("Productos disponibles en la tienda:")
            for producto in self.productos:
                print(f"- {producto}")
        else:
            print("No hay productos disponibles en la tienda.")

# Ejemplo de uso:
mi_tienda = Tienda("Tienda Central")

# Agregar productos
mi_tienda.agregar_producto("Manzanas")
mi_tienda.agregar_producto("Bananas")
mi_tienda.agregar_producto("Leche")

# Mostrar productos
mi_tienda.mostrar_productos()

# Eliminar un producto
mi_tienda.eliminar_producto("Bananas")

# Mostrar productos después de eliminar
mi_tienda.mostrar_productos()



input()





        
