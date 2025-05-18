print ('Ejercicios en Python para presentar')
print('Nombre: Pamela Blanco Vincent.', 'Matricula: 2023-1668.')

print('\nMenu de opciones:')
print('Seleccione la opcion que deseas')
print('1. POO.- Clase Persona')
print('2. POO.- Clase Cuenta ')
print('3. POO.- Clase Fraccion')
print('4. POO.- Clase Complejos')
print('5. POO.- Clase Banco y Cliente ')
print("6. POO - Cuenta, PlazoFijo y CajaAhorro")
print("7. Ciclo WHILE - Notas de Alumnos")
print("8. Ciclo WHILE - Sueldos de Empleados")
print("9. Ciclo WHILE - Notas de Alumnos")
print("10. Ciclo FOR - Suma de Últimos 5 Números")
print("11. Ciclo FOR - Tabla de Multiplicar")
print("12. Ciclo FOR - Coordenadas de Puntos")
print("13. Ciclo FOR - Tipos de Triángulos")
print("14. Funciones - Cuadrado y Producto")
print("15. Funciones - Contar Vocales")
print("16. Funciones - Listas de Números Positivos y Negativos")
print("17. Funciones - Contar Personas Mayores de Edad")
print("18. Simples - Manejo de Strings")
print("19. Otros - Validación de Nombres de Usuarios")
print("20. Otros - Juego de Adivinanza de Números")
print("0. Salir")

while True:
    entrada = input("\nIngrese una opcion: ")
    
    if entrada == "":
        print("No ingresaste ninguna opcion. Por favor, introduce una opcion valida.")
        continue
    
    try:
        opcion = int(entrada)
    except ValueError:
        print("Opción no válida. Por favor, introduce un número.")
        continue
    
    if opcion == 0:
        break
    
    if opcion == 1:
        

        #creacion de clase
        class Persona:

            #creacion del constructor
            def __init__(self, nombre, apellido, edad, casado, no_id):
                self.nombre = nombre
                self.apellido = apellido
                self.edad = edad
                self.casado = casado
                self.no_id = no_id
                
            #crear metodo para mostrar informacion
            def mostrar_info(self):
                return f"Nombre: {self.nombre} {self.apellido}, Edad: {self.edad}, Casado: {self.casado}, Documento: {self.no_id}"

            #Metodo para saber la profesion
            def trabajar(self):
                pass
            
            #Metodo para saber su hobby
            def jobby(self):
                pass
            #Metodo par saber lo que estudia
            def estudiar(self):
                pass
            
        #Crear los clases de tipo persona con diferentes profesiones
        #Clase Ingeniero  
        class Ingeniero(Persona):
            def trabajar(self):
                return "Diseño nuevos proyectos"

            def hobby(self):
                return "Me gusta leer libros"

            def estudiar(self):
                return "Aprendo nuevos lenguajes de programacion"
            
        #Clase Profesor
        class Profesor(Persona):
            def trabajar(self):
                return "Enseno a los estudiantes"

            def hobby(self):
                return "Me gusta escuchando música clásica"

            def estudiar(self):
                return "Estoy preparando una nueva lección"
            
        #Clase Abogado 
        class Abogado(Persona):
            def trabajar(self):
                return "Defiendo personas en el tribunal"

            def hobby(self):
                return "me gusta jugar golf"

            def estudiar(self):
                return "Estoy leyendo un libro de derecho"
            
        #Clase Cocinero
        class Cocinero(Persona):
            def trabajar(self):
                return "preporo platos de comida"
            def hobby(self):
                return "Me gusta preparar nuevos platos de comida"

            def estudiar(self):
                return "Estoy aprendiendo nuevas recetas"
            
        #Clase Arquitecto
        class Arquitecto(Persona):
            def trabajar(self):
                return "Estoy diseñando un nuevo edificio"

            def hobby(self):
                return "Me gusta dibujar bocetos"

            def estudiar(self):
                return "Estoy aprendiendo un nuevo software de diseño"

        #Clase Deportista
        class Deportista(Persona):
            def trabajar(self):
                return "Juego partidos"

            def hobby(self):
                return "Me gusta hacer stretching"

            def estudiar(self):
                return "Estoy analizando las estrategias del oponente"

        #Clase Medico
        class Medico(Persona):
            def trabajar(self):
                return "Atiendo pacientes"

            def hobby(self):
                return "Me gusta hacer ejercicios en el gimnasio"

            def estudiar(self):
                return "Estoy leyendo un artículo de investigación médica"

        #Crear objetos de tipo persona
        persona1 = Ingeniero("Juan", "Pérez", 30, True, "12345678")
        persona2 = Profesor("Pedro", "Rodríguez", 40, True, "11111111")
        persona3 = Abogado("Ana", "Díaz", 28, False, "22222222")
        persona4 = Cocinero("Luis", "Martínez", 32, True, "33333333")
        persona5 = Arquitecto("Sofía", "García", 29, False, "44444444")
        persona6 = Deportista("Carlos", "Hernández", 25, True, "55555555")
        persona7 = Medico("María", "González", 35, False, "98765432")

        print('Persona 1')
        print(persona1.mostrar_info())
        print(persona1.trabajar())
        print(persona1.hobby())
        print(persona1.estudiar())
              
        print ('\nPersona 2')
        print(persona2.mostrar_info())
        print(persona2.trabajar())
        print(persona2.hobby())
        print(persona2.estudiar())

        print ('\nPersona 3')
        print(persona3.mostrar_info())
        print(persona3.trabajar())
        print(persona3.hobby())
        print(persona3.estudiar())

        print ('\nPersona 4')
        print(persona4.mostrar_info())
        print(persona4.trabajar())
        print(persona4.hobby())
        print(persona4.estudiar())

        print ('\nPersona 5')
        print(persona5.mostrar_info())
        print(persona5.trabajar())
        print(persona5.hobby())
        print(persona5.estudiar())

        print ('\nPersona 6')
        print(persona6.mostrar_info())
        print(persona6.trabajar())
        print(persona6.hobby())
        print(persona6.estudiar())

        print ('\nPersona 7')
        print(persona7.mostrar_info())
        print(persona7.trabajar())
        print(persona7.hobby())
        print(persona7.estudiar())

    if opcion ==2:
        class Cuenta:
            def __init__(self, titular="", saldo=0.0):
                self.titular = titular
                self.saldo = saldo

            # Método para mostrar información de la cuenta
            def mostrar(self):
                return f"Titular: {self.titular}, Saldo: {self.saldo}"

            # Método para ingresar dinero en la cuenta
            def ingreso(self, cantidad):
                if cantidad > 0:
                    self.saldo += cantidad
                    print(f"Ingreso de {cantidad} realizado.")
                else:
                    print("La cantidad a ingresar debe ser positiva.")

            # Método para retirar dinero de la cuenta
            def reintegro(self, cantidad):
                if 0 < cantidad <= self.saldo:
                    self.saldo -= cantidad
                    print(f"Reintegro de {cantidad} realizado.")
                else:
                    print("Cantidad no válida o saldo insuficiente.")

            # Método para transferir dinero a otra cuenta
            def transferencia(self, otra_cuenta, cantidad):
                if 0 < cantidad <= self.saldo:
                    self.saldo -= cantidad
                    otra_cuenta.saldo += cantidad
                    print(f"Transferencia de {cantidad} a {otra_cuenta.titular} realizada.")
                else:
                    print("Cantidad no válida o saldo insuficiente.")
        
        # Creación de objetos Cuenta con diferentes constructores
        cuenta1 = Cuenta()  # Constructor por defecto
        cuenta2 = Cuenta("Juan Pérez", 1000.0)  # Constructor con parámetros

        # Uso de los métodos de la clase Cuenta
        print(cuenta1.mostrar())  # Titular: , Saldo: 0.00€
        print(cuenta2.mostrar())  # Titular: Juan Pérez, Saldo: 1000

        cuenta2.ingreso(500.0)
        print(cuenta2.mostrar())  # Titular: Juan Pérez, Saldo: 1500

        cuenta2.reintegro(200.0)
        print(cuenta2.mostrar())  # Titular: Juan Pérez, Saldo: 1300

        cuenta3 = Cuenta("Ana López", 300.0)
        cuenta2.transferencia(cuenta3, 100.0)
        print(cuenta2.mostrar())  # Titular: Juan Pérez, Saldo: 1200
        print(cuenta3.mostrar())  # Titular: Ana López, Saldo: 400

    if opcion ==3:
        import math

        class Fraccion:
            #Constructor de la clase Fraccion
            def __init__(self, numerador, denominador):
                self.numerador = numerador
                self.denominador = denominador

            def __str__(self):
               # Método para representar la fracción como string
                return f"{self.numerador}/{self.denominador}"

            def sumar(self, otra_fraccion):
                #Método para sumar dos fracciones
                nuevo_numerador = self.numerador * otra_fraccion.denominador + otra_fraccion.numerador * self.denominador
                nuevo_denominador = self.denominador * otra_fraccion.denominador
                return Fraccion(nuevo_numerador, nuevo_denominador)

            def restar(self, otra_fraccion):
                #Método para restar dos fracciones
                nuevo_numerador = self.numerador * otra_fraccion.denominador - otra_fraccion.numerador * self.denominador
                nuevo_denominador = self.denominador * otra_fraccion.denominador
                return Fraccion(nuevo_numerador, nuevo_denominador)

            def multiplicar(self, otra_fraccion):
                #Método para multiplicar dos fracciones
                nuevo_numerador = self.numerador * otra_fraccion.numerador
                nuevo_denominador = self.denominador * otra_fraccion.denominador
                return Fraccion(nuevo_numerador, nuevo_denominador)

            def dividir(self, otra_fraccion):
                #Método para dividir dos fracciones
                if otra_fraccion.numerador == 0:
                    raise ZeroDivisionError("No se puede dividir entre cero")
                nuevo_numerador = self.numerador * otra_fraccion.denominador
                nuevo_denominador = self.denominador * otra_fraccion.numerador
                return Fraccion(nuevo_numerador, nuevo_denominador)


        # Crear objetos de tipo Fraccion
        fraccion1 = Fraccion(1, 2)
        fraccion2 = Fraccion(1, 3)

        # Realizar operaciones con las fracciones
        print("Fracción 1:", fraccion1)
        print("Fracción 2:", fraccion2)

        print("Suma:", fraccion1.sumar(fraccion2))
        print("Resta:", fraccion1.restar(fraccion2))
        print("Multiplicación:", fraccion1.multiplicar(fraccion2))
        print("División:", fraccion1.dividir(fraccion2))

    if opcion ==4:
        class Complejo:
            def __init__(self, real, imaginario):
                self.real = real
                self.imaginario = imaginario

            def __str__(self):
                return f"{self.real} + {self.imaginario}i"

            # Método para sumar dos números complejos
            def sumar(self, otro):
                real = self.real + otro.real
                imaginario = self.imaginario + otro.imaginario
                return Complejo(real, imaginario)

            # Método para restar dos números complejos
            def restar(self, otro):
                real = self.real - otro.real
                imaginario = self.imaginario - otro.imaginario
                return Complejo(real, imaginario)

            # Método para multiplicar dos números complejos
            def multiplicar(self, otro):
                real = self.real * otro.real - self.imaginario * otro.imaginario
                imaginario = self.real * otro.imaginario + self.imaginario * otro.real
                return Complejo(real, imaginario)

            # Método para dividir dos números complejos
            def dividir(self, otro):
                if otro.real == 0 and otro.imaginario == 0:
                    raise ValueError("No se puede dividir por cero.")
        
                divisor = otro.real**2 + otro.imaginario**2
                real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
                imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
                return Complejo(real, imaginario)

        # Crear algunos números complejos para probar los métodos
        c1 = Complejo(4, 3)
        c2 = Complejo(2, -1)

        # Sumar números complejos
        resultado_suma = c1.sumar(c2)
        print("Suma:", resultado_suma)  # Suma: 6 + 2i

        # Restar números complejos
        resultado_resta = c1.restar(c2)
        print("Resta:", resultado_resta)  # Resta: 2 + 4i

        # Multiplicar números complejos
        resultado_multiplicacion = c1.multiplicar(c2)
        print("Multiplicación:", resultado_multiplicacion)  # Multiplicación: 11 + 2i

        # Dividir números complejos
        resultado_division = c1.dividir(c2)
        print("División:", resultado_division)  # División: 1.0 + 2.ii

    if opcion == 5:
        class Cliente:
            def __init__(self, nombre, cantidad=0):
                #Constructor de la clase Cliente
                self.nombre = nombre
                self.cantidad = cantidad

            def depositar(self, monto):
                #Método para depositar dinero
                self.cantidad += monto

            def extraer(self, monto):
                #Método para extraer dinero
                if monto > self.cantidad:
                    print("No tiene suficiente saldo")
                else:
                    self.cantidad -= monto

            def mostrar_total(self):
                #Método para mostrar el saldo total
                return self.cantidad


        class Banco:
            def __init__(self, cliente1, cliente2, cliente3):
                #Constructor de la clase Banco
                self.cliente1 = cliente1
                self.cliente2 = cliente2
                self.cliente3 = cliente3

            def operar(self):
                #Método para realizar operaciones con los clientes
                print("Operaciones:")
                self.cliente1.depositar(1000)
                self.cliente2.extraer(500)
                self.cliente3.depositar(2000)

            def deposito_total(self):
                #Método para calcular el depósito total
                return self.cliente1.mostrar_total() + self.cliente2.mostrar_total() + self.cliente3.mostrar_total()


        # Crear objetos de tipo Cliente
        cliente1 = Cliente("Juan", 1000)
        cliente2 = Cliente("Maria", 500)
        cliente3 = Cliente("Pedro", 2000)

        # Crear objeto de tipo Banco
        banco = Banco(cliente1, cliente2, cliente3)

        # Realizar operaciones con el banco
        banco.operar()

        # Mostrar el depósito total
        print("Depósito total:", banco.deposito_total())

    if opcion ==6:
        class Cuenta:
            def __init__(self, titular, cantidad):
                #Constructor de la clase Cuenta
                self.titular = titular
                self.cantidad = cantidad

            def imprimir_datos(self):
                #Método para imprimir los datos de la cuenta
                print(f"Titular: {self.titular}")
                print(f"Cantidad: {self.cantidad}")


        class CajaAhorro(Cuenta):
            def __init__(self, titular, cantidad):
                #Constructor de la clase CajaAhorro
                super().__init__(titular, cantidad)

            def mostrar_informacion(self):
                #Método para mostrar la información de la caja de ahorro
                self.imprimir_datos()
                print("Tipo de cuenta: Caja de Ahorro")


        class PlazoFijo(Cuenta):
            def __init__(self, titular, cantidad, plazo, interes):
                #Constructor de la clase PlazoFijo
                super().__init__(titular, cantidad)
                self.plazo = plazo
                self.interes = interes

            def obtener_interes(self):
                #Método para obtener el importe del interés
                return self.cantidad * self.interes / 100

            def mostrar_informacion(self):
                #Método para mostrar la información del plazo fijo

                self.imprimir_datos()
                print(f"Plazo: {self.plazo} meses")
                print(f"Interés: {self.interes}%")
                print(f"Total de interés: {self.obtener_interes()}")


        # Crear objetos de tipo CajaAhorro y PlazoFijo
        caja_ahorro = CajaAhorro("Juan Pérez", 1000)
        plazo_fijo = PlazoFijo("María García", 5000, 12, 5)

        # Mostrar la información de cada objeto
        print("Caja de Ahorro:")
        caja_ahorro.mostrar_informacion()
        print("\nPlazo Fijo:")
        plazo_fijo.mostrar_informacion()
                
        
    if opcion == 7:
        
        print("Programa para registrar notas de 10 alumnos")

        #Inicializar variables
        aprobados = 0
        suspendidos = 0
        contador_alumnos = 0

        #crear bucle
        while contador_alumnos < 10:
            contador_alumnos += 1
            while True:
                try:
                    nota = float(input(f"Ingrese la nota del alumno {contador_alumnos} (entre el 0-10): "))
                    if 0 <= nota <= 10:
                        break
                    else:
                        print("La nota debe estar entre 0 y 10. Intente nuevamente.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    
            #Aumentar aprobados
            if nota >= 5:
                aprobados += 1
            #aumentar suspendidos
            else:
                suspendidos += 1

        print(f"\nResultados:")
        print(f"Alumnos aprobados: {aprobados}")
        print(f"Alumnos suspendidos: {suspendidos}")


    if opcion == 8:
        
        # Solicitar el número de empleados
        n = int(input("Ingrese el número de empleados: "))

        # Inicializar contadores y variables
        menos_500 = 0
        mas_500 = 0
        total_gasto = 0
        i = 0

        # Solicitar los sueldos de los empleados
        while i < n:
            try:
                sueldo = float(input(f"Ingrese el sueldo del empleado {i + 1} (entre 100 y 1000): "))
                if 100 <= sueldo <= 1000:
                    total_gasto += sueldo
                    if sueldo < 500:
                        menos_500 += 1
                    else:
                        mas_500 += 1
                    i += 1
                else:
                    print("El sueldo debe estar entre 100 y 1000. Intente de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        # Informar resultados
        print('\n')
        print(f"Cantidad de empleados que cobran menos de 500: {menos_500}")
        print(f"Cantidad de empleados que cobran más de 500: {mas_500}")
        print(f"Total que gasta la empresa en pagar a sus empleados: {total_gasto}")


    if opcion == 9:
        
        print("Programa para registrar notas de 10 alumnos")

        #Inicializar variables
        aprobados = 0
        suspendidos = 0
        contador_alumnos = 0
        
        #Iniciar el ciclo
        while contador_alumnos < 10:
            contador_alumnos += 1
            while True:
                try:
                    nota = float(input(f"Ingrese la nota del alumno {contador_alumnos} (entre el 0-10): "))
                    if 0 <= nota <= 10:
                        break
                    else:
                        print("La nota debe estar entre 0 y 10. Intente nuevamente.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            
            if nota >= 5:
                aprobados += 1
            else:
                suspendidos += 1
        #Mostrar resultados
        print(f"\nResultados:")
        print(f"Alumnos aprobados: {aprobados}")
        print(f"Alumnos suspendidos: {suspendidos}")        

    if opcion == 10:
        #Declarar variable lista
        numeros = []
        
        #Iniciar bucle for
        for i in range(10):

            #solicitar numero
            num = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(num)
            
        #sumar ultimos 5 numeros
        suma = 0
        for i in range(-5, 0):
            suma += numeros[i]

        #Mostrar la suma
        print(f"La suma de los últimos 5 valores ingresados es: {suma}")


    if opcion == 11:
        #solicitar valor
        numero = int(input("Ingrese un valor entero entre 1 y 10: "))

        #Evaluar que el valor ingresado este entre 1 y 10
        if 1 <= numero <= 10:
            #Mostrar tabla de multiplicar
            print(f"Tabla de multiplicar del {numero}:")
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")
        else:
            print("Error: El valor ingresado debe estar entre 1 y 10.")


    if opcion == 12:
        #Solicitar ingresar los puntos
        total_puntos = int(input("Ingrese el total de puntos a procesar: "))

        #Declarar variables
        cuadrante_I = 0
        cuadrante_II = 0
        cuadrante_III = 0
        cuadrante_IV = 0

        #iniciar bucle
        for i in range(total_puntos):
            x = int(input(f"Ingrese la coordenada x del punto {i+1}: "))
            y = int(input(f"Ingrese la coordenada y del punto {i+1}: "))

            if x > 0 and y > 0:
                cuadrante_I += 1
            elif x < 0 and y > 0:
                cuadrante_II += 1
            elif x < 0 and y < 0:
                cuadrante_III += 1
            elif x > 0 and y < 0:
                cuadrante_IV += 1

        print(f"Cuadrante I: {cuadrante_I} puntos")
        print(f"Cuadrante II: {cuadrante_II} puntos")
        print(f"Cuadrante III: {cuadrante_III} puntos")
        print(f"Cuadrante IV: {cuadrante_IV} puntos")


    if opcion ==13:
        #Solicitar ingresar la cantidad de triangulos
        n_triangles = int(input("Ingrese el número de triángulos: "))
        equilateros = 0
        isosceles = 0
        escalenos = 0

        #Iniciar bucle
        for i in range(n_triangles):
            a = float(input(f"Ingrese la longitud del lado a del triángulo {i+1}: "))
            b = float(input(f"Ingrese la longitud del lado b del triángulo {i+1}: "))
            c = float(input(f"Ingrese la longitud del lado c del triángulo {i+1}: "))

            #Definir las condiciones para cada triangulo
            if a == b == c:
                tipo = "Equilátero"
                equilateros += 1
            elif a == b or a == c or b == c:
                tipo = "Isósceles"
                isosceles += 1
            else:
                tipo = "Escaleno"
                escalenos += 1

            print(f"El triángulo {i+1} es {tipo}.")
            
        #Mostrar resultados
        print(f"\nResumen:")
        print(f"Triángulos equiláteros: {equilateros}")
        print(f"Triángulos isósceles: {isosceles}")
        print(f"Triángulos escalenos: {escalenos}")

    if opcion == 14:
        #Funcion cuadrado
        def cuadrado():
            num= int(input('Ingresa un numero entero para saber su cuadrado: '))
            cua = num ** 2
            print(f" El cuadrado de {num} es {cua}")
                     
        #Funcion producto
        def producto():
            num1= int(input('Ingresa el primer valor para multiplicar: '))
            num2= int(input('Ingresa el primer valor para multiplicar: '))
            prod= num1 * num2
            print(f" El producto entre {num1} y {num2} es: {prod})")

        #Menu principal
        print('Pragrama que calcula cuadrados y productos')
        cuadrado()
        producto()


    if opcion == 16:

        #Crear funcion cargar lista
        def cargar_lista():
            n = int(input("Ingrese la cantidad de valores a cargar: "))
            lista = []
            for i in range(n):
                valor = int(input(f"Ingrese el valor {i+1}: "))
                lista.append(valor)
            return lista

        #Crear funcion para separar valores positivos y negativos
        def separar_valores(lista):
            negativos = [x for x in lista if x < 0]
            positivos = [x for x in lista if x > 0]
            return negativos, positivos

        #Funcion para mostras la cantidad de negativos y positivos
        def imprimir_listas(negativos, positivos):
            print("Lista de valores negativos:", negativos)
            print("Lista de valores positivos:", positivos)

        # Bloque principal
        print("Programa que separa valores negativos y positivos")
        lista = cargar_lista()
        negativos, positivos = separar_valores(lista)
        imprimir_listas(negativos, positivos)


    if opcion == 15:
        #Crear funcion para contar vocales
        def contar_vocales(cadena):
            vocales = "aeiouAEIOU"
            contador = 0
            for caracter in cadena:
                if caracter in vocales:
                    contador += 1
            return contador

        # Bloque principal
        print("Cantidad de vocales en 'Pamela'es :", contar_vocales("Pamela"))
        print("Cantidad de vocales en 'python es divertido' es :", contar_vocales("python es divertido"))
        print("Cantidad de vocales en 'Esto es un ejemplo'es :", contar_vocales("Esto es un ejemplo"))

    if opcion == 17:
        #Crear funcion para mayores de edad
        def contar_mayores(edades):
            contador = 0
            for edad in edades:
                if edad >= 18:
                    contador += 1
            return contador

        # Bloque principal
        edades = []
        while len(edades) < 3:
            edad = int(input("Introduce una edad (entero): "))
            edades.append(edad)

        print("Cantidad de personas con 18 años o más:", contar_mayores(edades))


    if opcion == 18:
        # Solicitar la carga por teclado de un string
        cadena = input("Introduce una cadena: ")

        # Mostrar el total de caracteres del string
        print("El total de caracteres es :", len(cadena))

        # Utilizar las funciones upper, lower y capitalize
        print("La cadena en mayúsculas:", cadena.upper())
        print("La cadena en minúsculas:", cadena.lower())
        print("La cadena Capitalizado:", cadena.capitalize())

    if opcion == 19:
        def validar_usuario(usuario):
            """
            Valida un nombre de usuario según los siguientes criterios:
            - Mínimo de 6 caracteres y máximo de 12.
            - Alfanumérico (solo letras y números).
            """
            
            if len(usuario) < 6:
                return "El nombre de usuario debe contener al menos 6 caracteres"
            elif len(usuario) > 12:
                return "El nombre de usuario no puede contener más de 12 caracteres"
            elif not usuario.isalnum():
                return "El nombre de usuario puede contener solo letras y números"
            else:
                return True

        #Solicitar el nombre de usuario
        usuario = input("Introduce un nombre de usuario: ")
        resultado = validar_usuario(usuario)
        if resultado == True:
            print("Nombre de usuario válido")
        else:
            print(resultado)


    if opcion == 20:
        import random

        # Almacenamos un número aleatorio entre 1 y 50
        numero_secreto = random.randint(1, 50)

        print("¡Bienvenido al juego de adivinanza!")
        print("He pensado un número entre 1 y 50. Intenta adivinarlo.")

        while True:
            # Pedimos al usuario que ingrese un número y lo convertimos a entero
            try:
                numero_usuario = int(input("Ingresa un número: "))
            except ValueError:
                print("Error: debes ingresar un número entero.")
                continue

            # Verificamos si el número ingresado es igual al número secreto
            if numero_usuario == numero_secreto:
                print("¡Felicidades! Has adivinado el número secreto.")
                break
            elif numero_usuario < numero_secreto:
                print("Tu número es demasiado bajo. Intenta de nuevo.")
            else:
                print("Tu número es demasiado alto. Intenta de nuevo.")

        
                
                
input("")








        
