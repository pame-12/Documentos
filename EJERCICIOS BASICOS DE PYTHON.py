
#TAREA 1 - EJERCICIOS BASICOS EN PYTHON

print ('NOMBRE: Pamela Blanco')
print ('MATRICULA:20231668')
print('\n 1.Declarar variable de los diferentes tipos,asignarles valor e imprimir el valor:')

Entero = 11
Flotante = 12.05
Cadena = "Hola soy Pamela"
Booleano = True
Lista = [1,2,3,4,5]
Tupla= (6,7,8,9,10)
Diccionario = {'Nombre': 'Pamela', 'Apellido': 'Blanco'}

print("Entero:", Entero)
print("Flotante:", Flotante)
print("Cadena:", Cadena)
print("Booleano:", Booleano)
print("Lista:", Lista)
print("Tupla:", Tupla)
print("Diccionario:", Diccionario)


print('\n2. Calcular la distancia. Solicitar al usuario ingresar la velocidad y el tiempo')

velocidad = float(input('Ingrese el valor de la velocidad por favor (en km/h)...:'))
tiempo = float(input('Ingrese el valor del tiempo por favor (en h)...:'))

distancia = velocidad * tiempo
print('La distancia recorrida es de...:', distancia,"km")


print('\n3. Calcular el promedio simple de notas de un estudiante de sus tres notas parciales N1, N2, N3')
n1 = float(input('Ingrese el valor de la primera nota por favor...:'))
n2=float(input('Ingrese el valor de la segunda nota por favor...:'))
n3=float(input('Ingrese el valor de la tercera nota por favor...:'))

promedio = (n1+n2+n3)/3
print(f" El promedio de las notas es del estudiante es de...: {promedio}")



print('\n4. Hacer un programa que permita ingresar el número de partidos ganados, perdidos y empatados, se  debe  de  mostrar  su  puntaje  total')  

partidos_ganados = int(input("Ingrese el número de partidos ganados: "))
partidos_perdidos = int(input("Ingrese el número de partidos perdidos: "))
partidos_empatados = int(input("Ingrese el número de partidos empatados: "))

puntaje_total = (partidos_ganados * 3) + (partidos_empatados * 1) + (partidos_perdidos * 0)
print(f"El puntaje total en el torneo de apertura es de: {puntaje_total} puntos")


print ('\nCalcular el perimetro y superficie d eun rectangulo. Se debe solicitar al usuario introduzca la base y la altura.')

base = float(input("Ingrese la base del rectángulo (en unidades): "))
altura = float(input("Ingrese la altura del rectángulo (en unidades): "))

perimetro = 2 * (base + altura)
superficie = base * altura


print(f"El perímetro del rectángulo es: {perimetro} unidades")
print(f"La superficie del rectángulo es: {superficie} unidades cuadradas")


print('\n6. Calcular el area y el volumen de un cilindro. Soliictar al usuario introduzca el radio y la altura.')
import math
radio = float(input("Ingrese el radio del cilindro (en unidades): "))
altura = float(input("Ingrese la altura del cilindro (en unidades): "))

area = 2 * math.pi * radio * (radio + altura)
volumen = math.pi * (radio ** 2) * altura

print(f"El área del cilindro es: {area:.2f} unidades cuadradas")
print(f"El volumen del cilindro es: {volumen:.2f} unidades cúbicas")



print('\n7. Calcular el volumen de una esfera. Pedir al usuario introduzca el Radio.')
radio = float(input("Ingrese el radio de la esfera (en unidades): "))

volumen = (4/3) * math.pi * (radio ** 3)

print(f"El volumen de la esfera es: {volumen:.2f} unidades cúbicas")


print('\nCalcular el Perímetro de un tríangulo equilatero. Pedir al usuario ingrese la altura del triangulo.')
altura = float(input("Ingrese la altura del triángulo equilátero (en unidades): "))
perimetro = 3 * altura
print(f"El perímetro del triángulo equilátero es: {perimetro} unidades")


print("\nCalcular el cambio de moneda dominicana a dolares y euros. pedir al usuario introduzca cantidad de pesos.")
pesos_dominicanos = float(input("Ingrese la cantidad de pesos dominicanos que desea cambiar: "))
tasa_cambio_dolar = 0.018
dolares = pesos_dominicanos * tasa_cambio_dolar
print(f"{pesos_dominicanos} pesos dominicanos son aproximadamente:")
print(f"{dolares:.2f} dólares")


print('\n10. Calcule la velocidad de un automóvil. Pedir al usuario ingrese tiempo en segundos y distincia en metros.')
tiempo_segundos = float(input("Ingrese el tiempo en segundos: "))
distancia_metros = float(input("Ingrese la distancia en metros: "))


velocidad = distancia_metros / tiempo_segundos

# Imprimir la velocidad calculada
print(f"La velocidad del automóvil es: {velocidad} m/s")


print("\n11 Escribe un programa que convierta una cadena que contiene un número entero en un tipo de dato int.")
# Solicitar al usuario ingresar una cadena que contenga un número entero
cadena_numero = input("Ingrese un un número como cadena: ")

# Convertir la cadena a un tipo de dato int
numero_entero = int(cadena_numero)

# Imprimir el número entero convertido
print("El número entero convertido es:", numero_entero)

print('\n12 Escribe un programa que convierta una cadena que contiene un número flotante en un tipo de dato float.')
cadena = input('Ingresa un numero como cadena:')
numero_float = float(cadena)
print('El numero flotante convertido es:', numero_float)

print('\n13 Escribe un programa que convierta un número entero a una cadena.')
numero = int(input('Ingresa un numero entero'))
cadena = str(numero)
print('El numero entero convertido a cadena es', cadena)


print('\n14 Escribe un programa que convierta una lista de números enteros a una cadena, donde cada número esté separado por comas.')

# Solicitar al usuario ingresar una lista de números enteros separados por espacios
numeros_enteros = input("Ingrese una lista de números enteros separados por espacios: ")

# Convertir la cadena de entrada en una lista de números enteros
numeros_enteros = [int(numero) for numero in numeros_enteros.split()]

# Convertir la lista de números enteros a una cadena separada por comas
cadena_numeros = ', '.join(str(numero) for numero in numeros_enteros)

# Imprimir la cadena resultante
print("La lista de números enteros convertida a una cadena es:", cadena_numeros)


print('\n15 Escribe un programa que convierta una cadena de números separados por comas a una lista de enteros.')
# Solicitar al usuario ingresar una cadena de números separados por comas
cadena_numeros = input("Ingrese una cadena de números separados por comas: ")

# Dividir la cadena en una lista de cadenas
numeros_como_cadenas = cadena_numeros.split(',')

# Convertir cada cadena a un número entero
numeros_enteros = [int(numero) for numero in numeros_como_cadenas]

# Imprimir la lista de enteros resultante
print("La lista de enteros obtenida es:", numeros_enteros)


print('\n16 Escribe un programa que convierta un diccionario a una lista de tuplas.')

diccionario = {'a': 1, 'b': 2, 'c': 3}
print('El diccionario es', diccionario)
lista_de_tuplas = list(diccionario.items())
print("La lista de tuplas obtenida es:", lista_de_tuplas)


print('\n17 Escribe un programa que convierta una lista de tuplas a un diccionario.')
lista_de_tuplas = [("a", 1), ("b", 2), ("c", 3)]

# Convertir la lista de tuplas a un diccionario
diccionario = dict(lista_de_tuplas)

# Imprimir el diccionario resultante
print("El diccionario obtenido es:", diccionario)

input()
