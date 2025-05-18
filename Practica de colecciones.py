print('Pamela Blanco. 2023-1668')

print('\n          ====================Ejercicios de listas====================')
print("1. Escribe un programa que tome una lista de números como entrada y devuelva la suma de todos los números en la lista.\n")
lista=[1, 2, 3, 4, 5]
print('La lista de numeros es:', lista)
suma = 0

for i in lista:
    suma += i
print('La suma de los numeros de la lista es:', suma)


print('\n2. Crea un programa que encuentre el número más grande en una lista dada.\n')

grande=[5, 10, 15, 20]
print('\nLa lista de valores es:', grande)

print('\nEl numero mas gande de la lista es:', max(grande))


print('\n3. Escribe un programa que tome una lista y devuelva una nueva lista que contenga solo los elementos pares de la lista original.\n')
pares = [1, 2, 3, 4, 5, 6, 7, 8]
print('La lista de numeros es:', pares)
nueva_lista = []

for i in pares:
    if i % 2 ==0:
        nueva_lista.append(i)
    else:
        pass
        
print('\nLa nueva lista solo con los numeros pares es:', nueva_lista)


print('\n4. Crea un programa que tome una lista de palabras como entrada y devuelva una nueva lista que contenga solo las palabras que tienen más de cinco letras.\n')
palabras=['paloma', 'sol', 'cabello', 'programa', 'python']
print('La lista de palabras es:', palabras)
palabras5=[]

for i in palabras:
    if len(i) >= 5:
        palabras5.append(i)
print('\nLa lista con las nuevas palabras con mas de 5 letras es:', palabras5)

print('\n5. Escribe un programa que tome dos listas y devuelva una nueva lista que contenga solo los elementos que son comunes entre las dos listas (sin duplicados).\n')

# Listas de ejemplo
lista1 = [1, 2, 2, 3, 4, 5]
print('Los valores de la primera lista son:', lista1 )
lista2 = [3, 4, 4, 5, 6]
print('Los valores de la segunda lista son:', lista2 )

# Convertir ambas listas a conjuntos para eliminar duplicados
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Encontrar la intersección de los dos conjuntos
interseccion = conjunto1.intersection(conjunto2)

# Convertir el conjunto de nuevo a una lista
lista_comun = list(interseccion)

# Imprimir el resultado
print('\nLos valores comunes entre las listas son:', lista_comun)  # Salida: [3, 4, 5]


print('\n6. Crea un programa que tome una lista y devuelva una nueva lista que contenga los elementos en orden inverso.\n",')

orden = [1, 2, 3]
print('\nLa lista de palabras es:', orden)

orden1 = orden[::-1]
   
print('La nueva lista es con el orden invertido es:', orden1)


print('\n7.Escribe un programa que tome una lista de números y devuelva una nueva lista que contenga solo los elementos únicos de la lista original (eliminando los duplicados).\n",')
lista = [1, 2, 2, 3, 4, 4, 5]
print('La lista de elementos es:', lista)

# Crear una nueva lista con los elementos únicos
elementos_unicos = list(set(lista))

# Imprimir el resultado
print('\nLa nueva lista sin los elementos duplicados:', elementos_unicos)  # Salida: [1, 2, 3, 4, 5]


print('\n8. Crea un programa que tome una lista de números como entrada y devuelva una lista que contenga el mismo conjunto de números pero ordenados de menor a mayor.\n')
lista_num =[2,1,3,4,7,6,5]
print('La lista de numeros es:', lista_num)

lista_ordenada = sorted(lista_num)
print('\nLa lista ordenada de menor a mayor es:', lista_ordenada)

print('\n9. Escribe un programa que tome una lista de palabras y devuelva la palabra más larga de la lista.\n')

palabras = ['El', 'Dia', 'Esta', 'Soleado']

palabra_larga =""

for palabra in palabras:
    if len(palabra) > len(palabra_larga):
        palabra_larga= palabra
        

print("Lista de palabras:", palabras)
print("\nLa palabra más larga es:", palabra_larga)


print('\n10. Crea un programa que tome dos listas y devuelva una nueva lista que contenga solo los elementos que están en la primera lista pero no en la segunda lista.\n')

lista_1=[1, 2, 3, 4, 5, 6]
lista_2=[2, 4, 6, 8, 10]
resultado = []

for i in lista_1:
    if i not in lista_2:
        resultado.append(i)
        
print("Lista 1:", lista_1)
print("Lista 2:", lista_2)
print("Elementos que estan en la Lista 1 pero no en la Lista 2:", resultado)
        



print('\n           ====================Ejercicios con tuplas====================')

print("\n1. Escribe un programa que tome una lista de tuplas, donde cada tupla contiene un nombre y una edad, y devuelva una nueva lista de tuplas que contenga solo las personas mayores de 18 años, ordenadas alfabéticamente por nombre.\n")

# Lista de tuplas (nombre, edad)
personas = [("Ana", 22), ("Juan", 17), ("María", 19), ("Pedro", 21), ("Lucía", 15)]

# Filtramos las personas mayores de 18 años
mayores_de_18 = []
for persona in personas:
    if persona[1] > 18:
        mayores_de_18.append(persona)

# Ordenamos la lista de personas mayores de 18 años alfabéticamente por nombre
for i in range(len(mayores_de_18)):
    for j in range(len(mayores_de_18) - 1):
        if mayores_de_18[j][0] > mayores_de_18[j + 1][0]:
            mayores_de_18[j], mayores_de_18[j + 1] = mayores_de_18[j + 1], mayores_de_18[j]

print("Lista original:", personas)
print("Personas mayores de 18 años ordenadas alfabéticamente por nombre:", mayores_de_18)



print('\n2. Crea un programa que tome una lista de tuplas, donde cada tupla contiene el nombre de un estudiante y una lista de sus calificaciones, y devuelva una nueva lista de tuplas que contenga el nombre del estudiante y su calificación más alta.\n')

# Lista de tuplas (nombre, lista de calificaciones)
estudiantes = [("Juan", [85, 90, 92]), 
               ("María", [88, 85, 90]), 
               ("Pedro", [95, 89, 92]), 
               ("Ana", [82, 88, 91])]

# Lista para almacenar el nombre del estudiante y su calificación más alta
maximas_calificaciones = []

# Iteramos sobre cada tupla de la lista de estudiantes
for nombre, calificaciones in estudiantes:
    # Obtenemos la calificación más alta del estudiante
    max_calificacion = max(calificaciones)
    # Añadimos el nombre del estudiante y su calificación más alta a la lista resultante
    maximas_calificaciones.append((nombre, max_calificacion))

print("Lista original:", estudiantes)
print("Lista de nombres y calificaciones más altas:", maximas_calificaciones)


print('\n3. Escribe un programa que tome una lista de tuplas, donde cada tupla contiene la información de un libro (título, autor, año de publicación), y devuelva una nueva lista de tuplas ordenadas por año de publicación de manera descendente.\n')

# Lista de tuplas (título, autor, año de publicación)
libros = [("El Aleph", "Jorge Luis Borges", 1949),
          ("Cien años de soledad", "Gabriel García Márquez", 1967),
          ("El Principito", "Antoine de Saint-Exupéry", 1943)]

# Ordenamos la lista de libros por año de publicación de manera descendente
libros_ordenados = sorted(libros, key=lambda libro: libro[2], reverse=True)

print("Lista original de libros:", libros)
print("\nLista de libros ordenada por año de publicación (descendente):", libros_ordenados)


print('\n4. Crea un programa que tome una lista de tuplas, donde cada tupla contiene el nombre de un producto y su precio, y devuelva una nueva lista de tuplas ordenadas por precio de manera ascendente.\n')

productos = [("Laptop", 1200), 
             ("Mouse", 20), 
             ("Teclado", 50), 
             ("Monitor", 300)]

productos_ordenados = sorted(productos, key=lambda producto: producto[1])


print('La lista de productos es:', productos)
print('\nLa lista de productos ordenada con los precios de manea ascendente es:', productos_ordenados )


print('\n5. Escribe un programa que tome una lista de tuplas, donde cada tupla contiene la información de un estudiante (nombre, edad, grado) y devuelva una nueva lista de tuplas ordenadas por grado de manera ascendente y luego por edad de manera descendente.\n')

estudiantes = [('Juan', 15, 6),
               ('Manuel', 12, 4),
               ('Paola', 7, 2)]

grados_ordenados= sorted(estudiantes, key=lambda estudiante: estudiante[2])
edad_descentdente = sorted(estudiantes, key = lambda estudiante: estudiante[1], reverse = True)

print('\nLa lista de estudiantes es:', estudiantes)
print('\nLa lista de estudiantes ordenados por grado de forma ascendnte es:', grados_ordenados )
print('\nLa lista de estudiantes ordenados por edad de forma descendente es:',edad_descentdente )


print('\n6.Crea un programa que tome dos listas de tuplas, donde cada tupla contiene la información de un empleado (nombre, salario), y devuelva una nueva lista de tuplas que contenga el nombre de los empleados y la diferencia entre sus salarios en la primera y la segunda lista.\n')

# Dos listas de tuplas de empleados (nombre, salario)
empleados_lista1 = [("Juan", 3000), 
                    ("María", 3500), 
                    ("Pedro", 2800)]

empleados_lista2 = [("Juan", 3200), 
                    ("María", 3600), 
                    ("Pedro", 3000)]

# Lista para almacenar el nombre de los empleados y la diferencia de salarios
diferencias_salarios = []

# Iteramos sobre los empleados de la primera lista
for empleado1 in empleados_lista1:
    nombre = empleado1[0]
    salario1 = empleado1[1]
    
    # Buscamos al empleado en la segunda lista
    for empleado2 in empleados_lista2:
        if empleado2[0] == nombre:
            salario2 = empleado2[1]
            diferencia = salario2 - salario1
            diferencias_salarios.append((nombre, diferencia))
            break  # Terminamos de buscar una vez encontrado el empleado


print('Primera lista:', empleados_lista1)
print('segunda lista:', empleados_lista2)
print("Lista de diferencias de salarios entre las dos listas:")
print(diferencias_salarios)


print('\n7. Escribe un programa que tome una lista de tuplas, donde cada tupla contiene el nombre de una ciudad y su temperatura actual en grados Celsius, y devuelva una nueva lista de tuplas que contenga el nombre de las ciudades y su temperatura convertida a grados Fahrenheit.\n')
# Lista de tuplas (ciudad, temperatura en Celsius)
ciudades_temperaturas = [("Santo Domingo", 30), 
                         ("New York", 20), 
                         ("Tokyo", 25), 
                         ("London", 15)]

# Lista para almacenar el nombre de las ciudades y su temperatura en Fahrenheit
ciudades_temperaturas_fahrenheit = []

# Iteramos sobre las tuplas de ciudades y temperaturas en Celsius
for ciudad, temperatura_celsius in ciudades_temperaturas:
    # Convertimos la temperatura de Celsius a Fahrenheit
    temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
    # Agregamos el nombre de la ciudad y la temperatura en Fahrenheit a la lista resultante
    ciudades_temperaturas_fahrenheit.append((ciudad, temperatura_fahrenheit))

print("Lista original de ciudades y temperaturas en Celsius:")
print(ciudades_temperaturas)
print("\nLista de ciudades y temperaturas convertidas a Fahrenheit:")
print(ciudades_temperaturas_fahrenheit)


print('\n8. Crea un programa que tome una lista de tuplas, donde cada tupla contiene el nombre de un país y su población, y devuelva una nueva lista de tuplas que contenga el nombre del país y su población en notación científica.\n')

# Lista de tuplas (país, población)
paises_poblacion = [("China", 1439323776), 
                    ("India", 1380004385), 
                    ("Estados Unidos", 331002651), 
                    ("Indonesia", 273523615)]

# Lista para almacenar el nombre de los países y su población en notación científica
paises_poblacion_cientifica = []

# Iteramos sobre las tuplas de países y poblaciones
for pais, poblacion in paises_poblacion:
    # Convertimos la población a notación científica
    poblacion_cientifica = "{:.2e}".format(poblacion)
    # Agregamos el nombre del país y su población en notación científica a la lista resultante
    paises_poblacion_cientifica.append((pais, poblacion_cientifica))

print("Lista original de países y poblaciones:")
print(paises_poblacion)
print("\nLista de países y poblaciones en notación científica:")
print(paises_poblacion_cientifica)

print('\n9. Escribe un programa que tome una lista de tuplas, donde cada tupla contiene el nombre de un artículo y su cantidad en inventario, y devuelva una nueva lista de tuplas que contenga el nombre del artículo y su cantidad en inventario, pero solo para aquellos artículos cuya cantidad sea mayor que cero.\n')

articulos_en_inventario = [('Manzanas', 15),
                        ('Uvas', 20),
                        ('Pera', 0),
                        ('Naranjas', 3),
                        ('Melon', 0)]

articulos_disponibles=[]

for articulo, cantidad in articulos_en_inventario:
    if cantidad >0:
        articulos_disponibles.append((articulo, cantidad))
        

print('\nLa lista de productos es:', articulos_en_inventario)
print('\nLa lista de productos disponibles con cantidades mayor que cero es:', articulos_disponibles)



print('\n10. Crea un programa que tome una lista de tuplas, donde cada tupla contiene el nombre de un cliente y una lista de sus compras (nombre del producto, precio), y devuelva una nueva lista de tuplas que contenga el nombre del cliente y el total gastado en todas sus compras.')

clientes = [('Juan',[('Laptop', 12000), ('Mouse', 200), ('Teclado', 500)])]

total_compras = []

for cliente, compras in clientes:
    total = sum(precio for _, precio in compras)
    total_compras.append((cliente, total))

print("\nLista original de clientes y sus compras:")
print(clientes)
print("\nLista de clientes y el total gastado en sus compras:")
print(total_compras)


print('\n          ====================Diccionarios==================== \n')

print('\n1. Escribe un programa que cree un diccionario con nombres de personas como clave y sus edades como valor, y luego imprima el nombre de la persona más joven.\n')

personas = {'Pamela': 20, 'Juan': 35, 'Maria': 15, 'Veronica': 23, 'Jessica': 18}
# Encontrar la persona más joven
persona_mas_joven = min(personas, key=personas.get)

# Imprimir el nombre de la persona más joven
print('El diccionario es:', personas)
print(f"La persona más joven es {persona_mas_joven} con {personas[persona_mas_joven]} años.")


print('\n2. Crea un programa que tome dos diccionarios que contienen información sobre productos (nombre del producto y precio), los combine y devuelva un nuevo diccionario con el nombre del producto y su precio total.\n')
# Diccionarios de ejemplo con productos y precios
productos1 = {
    "Manzanas": 2.5,
    "Peras": 3.0,
    "Plátanos": 1.75
}

productos2 = {
    "Manzanas": 2.0,
    "Naranjas": 2.5,
    "Plátanos": 1.5
}

# Combinar los diccionarios y calcular el precio total
productos_totales = {}

for producto, precio in productos1.items():
    if producto in productos_totales:
        productos_totales[producto] += precio
    else:
        productos_totales[producto] = precio

for producto, precio in productos2.items():
    if producto in productos_totales:
        productos_totales[producto] += precio
    else:
        productos_totales[producto] = precio

# Imprimir el nuevo diccionario con precios totales
print('Diccionario1:', productos1)
print('Diccionario2:', productos2)
print('Precios tatales', productos_totales)


print('\n3.Escribe un programa que tome un diccionario con nombres de países como clave y su población como valor, y devuelva una lista de los países con una población superior a 100 millones.\n')
paises = {
    "China": 1444216107,
    "India": 1393409038,
    "Estados Unidos": 331893745,
    "Brasil": 213993437,
    "Rusia": 145912025,
    "México": 126014024,
    "Japón": 125836021,
    "Filipinas": 111046913,
    "Egipto": 104258327
}

paises_mas_de_100_millones = []

for pais, poblacion in paises.items():
    if poblacion > 100000000:
        paises_mas_de_100_millones.append(pais)


print('\nLos paises y sus habitantes son:', paises)
print('\nLos paises con mas de 100 Millones de habitantes son:', paises_mas_de_100_millones)


print('\n4.Crea un programa que tome un diccionario con nombres de frutas como clave y su cantidad en inventario como valor, y devuelva el nombre de la fruta con la mayor cantidad en inventario.\n')


# Diccionario con nombres de frutas y sus cantidades en inventario
inventario = {
    "Manzanas": 150,
    "Peras": 500,
    "Plátanos": 200,
    "Naranjas": 75,
    "Uvas": 125
}

mayor = 0
for fruta, cantidad in inventario.items():
    if cantidad > mayor:
        mayor = cantidad
        nombre = fruta

print('Los productos en inventario son:', inventario)    
print('La fruta con mayor cantidad en inventario es:', nombre)



print('\n5. Escribe un programa que tome un diccionario con nombres de personas como clave y una lista de sus pasatiempos como valor, y devuelva una lista de todos los pasatiempos únicos.\n')
# Diccionario con nombres de personas y sus pasatiempos
pasatiempos_personas = {
    "Ana": ["leer", "correr", "pintar"],
    "Luis": ["correr", "fútbol", "nadar"],
    "Carlos": ["pintar", "videojuegos", "leer"],
    "Marta": ["nadar", "bailar", "fútbol"],
    "Sofia": ["correr", "videojuegos", "bailar"]
}

# Lista para almacenar pasatiempos únicos
pasatiempos_unicos = []

# Iterar sobre los valores del diccionario y agregar pasatiempos a la lista si no están ya presentes
for pasatiempos in pasatiempos_personas.values():
    for pasatiempo in pasatiempos:
        if pasatiempo not in pasatiempos_unicos:
            pasatiempos_unicos.append(pasatiempo)

# Imprimir la lista de pasatiempos únicos
print('\nLa lista de las personas y los pasatiempos es:',pasatiempos_personas )
print('\nLa lista de los pasatiempos unicos:', pasatiempos_unicos)




print('\n6. Crea un programa que tome un diccionario con nombres de estudiantes como clave y una lista de sus calificaciones como valor, y devuelva el nombre del estudiante con el promedio más alto.\n')


# Diccionario con nombres de estudiantes y sus calificaciones
calificaciones_estudiantes = {
    "Ana": [90, 85, 88],
    "Luis": [75, 80, 85],
    "Carlos": [100, 95, 98],
    "Marta": [70, 78, 82],
    "Sofia": [85, 87, 90]
}

# Variables para almacenar el nombre del estudiante con el promedio más alto y el promedio más alto
estudiante_mejor_promedio = ""
mejor_promedio = 0

# Iterar sobre los elementos del diccionario para calcular los promedios y encontrar el más alto
for estudiante, calificaciones in calificaciones_estudiantes.items():
    promedio = sum(calificaciones) / len(calificaciones)
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        estudiante_mejor_promedio = estudiante

# Imprimir el nombre del estudiante con el promedio más alto
print('\nEl listado de los estudiantes y sus calificaciones es:', calificaciones_estudiantes)
print(f"\nEl estudiante con el promedio más alto es {estudiante_mejor_promedio} con un promedio de {mejor_promedio:.2f}")


print('\n7. Escribe un programa que tome un diccionario con nombres de productos como clave y su precio como valor, y devuelva el precio promedio de todos los productos.\n')
# Diccionario con nombres de productos y sus precios
precios_productos = {
    "Manzanas": 50,
    "Peras": 45,
    "Plátanos": 30,
    "Naranjas": 10,
    "Uvas": 100
}

# Calcular la suma de todos los precios
suma_precios = sum(precios_productos.values())

# Calcular el número de productos
numero_productos = len(precios_productos)

# Calcular el precio promedio
precio_promedio = suma_precios / numero_productos

# Imprimir el precio promedio
print('La lista de los productos con sus presios es:', precios_productos)
print(f"El precio promedio de todos los productos es {precio_promedio:.2f}")


print('\n8. Crea un programa que tome un diccionario con nombres de ciudades como clave y una lista de temperaturas como valor, y devuelva el nombre de la ciudad con la temperatura más alta.\n')

# Diccionario con nombres de ciudades y sus temperaturas
temperaturas_ciudades = {
    "Madrid": [30, 32, 35, 33],
    "Barcelona": [28, 29, 27, 31],
    "Sevilla": [36, 37, 34, 33],
    "Valencia": [29, 30, 31, 28],
    "Santo Domingo": [25, 27, 26, 28]
}

# Variables para almacenar el nombre de la ciudad con la temperatura más alta y la temperatura más alta
ciudad_mas_caliente = ""
temperatura_maxima = float('-inf')  # Inicializamos con el valor más bajo posible

# Iterar sobre los elementos del diccionario para encontrar la temperatura más alta
for ciudad, temperaturas in temperaturas_ciudades.items():
    max_temp_ciudad = max(temperaturas)  # Obtener la temperatura más alta de la ciudad actual
    if max_temp_ciudad > temperatura_maxima:
        temperatura_maxima = max_temp_ciudad
        ciudad_mas_caliente = ciudad

# Imprimir el nombre de la ciudad con la temperatura más alta
print('Lista de las ciudades', temperaturas_ciudades)
print(f"\nLa ciudad con la temperatura más alta es {ciudad_mas_caliente} con una temperatura de {temperatura_maxima}°C")


print('\n9. Escribe un programa que tome un diccionario con nombres de países como clave y una lista de sus ciudades más pobladas como valor, y devuelva una lista de todos los países con al menos una ciudad con una población superior a 5 millones.\n')

# Diccionario con nombres de países y sus ciudades más pobladas
ciudades_poblacion = {
    "España": ["Madrid", "Barcelona", "Valencia"],
    "Francia": ["París", "Marsella", "Lyon"],
    "Italia": ["Roma", "Milán", "Nápoles"],
    "China": ["Pekín", "Shanghái", "Guangzhou"],
    "Japón": ["Tokio", "Osaka", "Nagoya"]
}

# Lista para almacenar los países con al menos una ciudad con población superior a 5 millones
paises_poblacion_superior_5m = []

# Iterar sobre los elementos del diccionario para encontrar los países adecuados
for pais, ciudades in ciudades_poblacion.items():
    for ciudad in ciudades:
        # Supongamos una población ficticia para ejemplificar la lógica
        poblacion_ciudad = 6000000  # Población ficticia de ejemplo
        if poblacion_ciudad > 5000000:
            paises_poblacion_superior_5m.append(pais)
            break  # Terminar la búsqueda para este país si se encuentra una ciudad con población suficiente

# Imprimir la lista de países con al menos una ciudad con población superior a 5 millones
print("Países con al menos una ciudad con población superior a 5 millones:")
print(paises_poblacion_superior_5m)

print('\n10. Crea un programa que tome dos diccionarios que contienen información sobre empleados (nombre del empleado y salario), los combine y devuelva un nuevo diccionario con el nombre del empleado y su salario incrementado en un 10%.\n')

# Diccionarios de ejemplo con información de empleados
empleados1 = {
    "Juan": 30000,
    "María": 35000,
    "Pedro": 32000
}

empleados2 = {
    "Ana": 15000,
    "Carlos": 31000,
    "Elena": 20000
}

# Función para incrementar el salario en un 10%
def incrementar_salario(salario):
    return salario * 1.10

# Combinar los diccionarios y aplicar el incremento de salario
nuevo_diccionario = {}
for empleado, salario in empleados1.items():
    nuevo_diccionario[empleado] = incrementar_salario(salario)

for empleado, salario in empleados2.items():
    nuevo_diccionario[empleado] = incrementar_salario(salario)

# Imprimir el nuevo diccionario con salarios incrementados
print('\nlistados de empleados1:', empleados1)
print('\nlistados de empleados2:', empleados2)
print("\nDiccionario con salarios incrementados en un 10%:")
print(nuevo_diccionario)


input('')
