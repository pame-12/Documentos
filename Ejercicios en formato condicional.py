
#Ejercicios condicionales 

print ('NOMBRE: Pamela Blanco')
print ('MATRICULA:20231668')

print('\n1- Pida a usuario la edad y el sexo, para que la computadora le indique si ya puede jubilarse.')
edad = int(input('Ingresa tu edad por favor:'))
sexo = input('Ingrese su sexo (Hombre/Mujer):').lower()

if sexo == 'hombre':
    if edad >= 60:
        print('¡Usted puede jubilarse!')
    else:
        print("Usted aún no puede jubilarse.")
elif sexo == 'mujer':
    if edad >= 54:
        print('¡Usted puede jubilarse!')
    else:
        print("Usted aún no puede jubilarse.")
else:
    print("Sexo ingresado incorrecto. Por favor, ingrese 'Hombre' o 'Mujer'.")



print('\n Solicitar al usuario que introduzca la figura geometrica y que introduzca el valor del area que desea calculara. ')
# Solicitar al usuario ingresar la figura geométrica
figura = input("Ingrese la figura geométrica de la cual desea calcular el área (cuadrado/circulo/triangulo): ").lower()

# Determinar qué tipo de figura se ingresó y solicitar el valor del área correspondiente
if figura == "cuadrado":
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    area = lado ** 2
    print(f"El área del cuadrado con lado {lado} es: {area}")
elif figura == "circulo":
    radio = float(input("Ingrese el radio del círculo: "))
    area = 3.1416 * (radio ** 2)
    print(f"El área del círculo con radio {radio} es: {area}")
elif figura == "triangulo":
    base = float(input("Ingrese la longitud de la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo con base {base} y altura {altura} es: {area}")
else:
    print("Figura geométrica ingresada incorrecta.")



print('\nEscribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.')

# Solicitar al usuario ingresar su nombre y sexo
nombre = input("Ingrese su nombre: ").capitalize()
sexo = input("Ingrese su sexo (Hombre/Mujer): ").lower()

# Determinar a qué grupo pertenece
if sexo == "mujer" and nombre < "M":
    grupo = "A"
elif sexo == "hombre" and nombre > "N":
    grupo = "A"
else:
    grupo = "B"

# Mostrar el grupo al que pertenece el usuario
print(f"{nombre}, perteneces al grupo {grupo}.")



print('\nEl programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada ')

edad = int(input("Ingrese la edad del cliente: "))

# Determinar el precio de la entrada según la edad
if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10

# Mostrar el precio de la entrada
print(f"El precio de la entrada es: {precio} USD")



print('\nSi los datos son el estado de los interruptores, determine si el equipo funcionará.')
# Solicitar al usuario ingresar el estado de los tres interruptores
interruptor1 = int(input("Ingrese el estado del interruptor 1 (1 para cerrado, 0 para abierto): "))
interruptor2 = int(input("Ingrese el estado del interruptor 2 (1 para cerrado, 0 para abierto): "))
interruptor3 = int(input("Ingrese el estado del interruptor 3 (1 para cerrado, 0 para abierto): "))

# Contar cuántos interruptores están cerrados
cerrados = interruptor1 + interruptor2 + interruptor3

# Determinar si el equipo funcionará
if cerrados >= 2:
    print("El equipo funcionará.")
else:
    print("El equipo no funcionará.")



print('\nEscribir un programa que almacene la cadena de caracteres contraseña en una variable,')

# Almacenar la cadena de caracteres contraseña en una variable
contraseña_guardada = "miContraseñaSecreta"

# Preguntar al usuario por la contraseña
contraseña_ingresada = input("Ingrese la contraseña: ")

# Comparar las contraseñas sin tener en cuenta mayúsculas y minúsculas
if contraseña_guardada.lower() == contraseña_ingresada.lower():
    print("La contraseña introducida es correcta.")
else:
    print("La contraseña introducida es incorrecta.")




print('\nEscribe un programa que lea dos números y determine cuál de ellos es el mayor.')

# Solicitar al usuario ingresar el primer número
numero1 = float(input("Ingrese el primer número: "))

# Solicitar al usuario ingresar el segundo número
numero2 = float(input("Ingrese el segundo número: "))

# Determinar cuál de los dos números es el mayor
if numero1 > numero2:
    print(f"El número mayor es: {numero1}")
elif numero2 > numero1:
    print(f"El número mayor es: {numero2}")
else:
    print("Ambos números son iguales.")




print('\n Realice un programa que lea un valor entero y determine si se trata de un número par o impar.')

# Solicitar al usuario ingresar un número entero
numero = int(input("Ingrese un número entero: "))

# Determinar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")



print('\n Escribe un programa que lea del teclado un carácter e indique en la pantalla si el carácter es una vocal minúscula o no.')

# Solicitar al usuario ingresar un carácter
caracter = input("Ingrese una vocal: ")

# Verificar si el carácter es una vocal minúscula
if len(caracter) != 1:
    print("Por favor, ingrese un solo carácter.")
elif caracter in 'aeiou':
    print(f"El carácter '{caracter}' es una vocal minúscula.")
elif caracter in 'AEIOU':
    print(f"El carácter '{caracter}' es una vocal mayúscula.")
else:
    print(f"El carácter '{caracter}' no es una vocal.")


print('\n Escribe un programa que reciba un año y nos diga si es bisiesto o no')

# Solicitar al usuario ingresar un año
anio = int(input("Ingrese un año: "))

# Verificar si el año es bisiesto
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")



print('\n Realiza un programa que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.')

def calcular_costo_viaje(num_alumnos):
    if num_alumnos >= 100:
        costo_por_alumno = 65
    elif num_alumnos >= 50:
        costo_por_alumno = 70
    elif num_alumnos >= 30:
        costo_por_alumno = 95
    else:
        costo_por_alumno = 4000 / num_alumnos
    
    costo_total_viaje = costo_por_alumno * num_alumnos
    
    return costo_total_viaje, costo_por_alumno

# Ejemplo de uso:
num_alumnos = int(input("Ingrese el número de alumnos que iran al viaje: "))
costo_total_viaje, costo_por_alumno = calcular_costo_viaje(num_alumnos)

print("El costo total del viaje es de", costo_total_viaje, "euros.")
print("El costo por alumno es de", costo_por_alumno, "euros.")



input()
