
print ('Realizar los siguientes ejercicios en python')

print ('\n1.Saludo Personalizado:')

nombre = input('¿Cuál es tu nombre? 😊--->')
print('Hola', nombre, 'es un gusto saludarte')

print ('\n2.Mensaje de Bienvenida:')

print('HOLA!!! BIENVENIDO A ESTA NUEVA AVENTURA 😊😊😊')

print ('\n3. Tabla de Multiplicar:')

n = 7
x = 1
while x <= 10:
     m = x * n
     print (n,'*', x, '=', m)
     x = x+1

print ('\n4. Mensaje de Despedida:')

print('¡Gracias por usar nuestro programa! ¡Adiós!')


print ('\n5. Patrón de Asteriscos:')

print('* * * *')
print('*     *')
print('*     *')
print('* * * *')


print ('\n6. Lista de Números:')

for i in range(1,11):
    print(i, end= "")


print ('\n7. Mensaje de Error:')

n = int(input('Ingresa un numero entero de dos digito por favor:...'))
if n < 10:
        print('Gracas!!! Ingresaste el numero', n)
else:
    print('ERROOOORRRRR!!!!! valor no valido, ingresa un numero valido para la proxima')



print ('\n8.Mensaje de Advertencia')

nivel_bateria = int(input("Ingresa el nivel de batería actual: "))

if nivel_bateria < 20:
    print("ADVERTENCIA: El nivel de batería es bajo. Por favor, conecta tu dispositivo.")
else:
    print("El nivel de batería es suficiente.")



print ('\n9.Menú de Opciones:')

print('''--------------- MENU DE COLORES ---------------
                 1. Azul
                 2. Blanco
                 3. Negro
                 4. Rosa
                 5. Verde
                 6. Naranja
                 7. Gris
                 8. Morado
                 9. Marron
                 10. Amarillo''')


opcion=input('¿Cuál color prefieres? Ingresa el numero:..')

if opcion == "1":
    print("Has elegido la Opción 1. Prefieres el color Azul")
elif opcion == "2":
    print("Has elegido la Opción 2. Prefieres el color Blanco")
elif opcion == "3":
    print("Has elegido la Opción 3. Prefieres el color Negro")
elif opcion == "4":
    print("Has elegido la Opción 4. Prefieres el color Rosa")
elif opcion == "5":
    print("Has elegido la Opción 5.Prefieres el color verde")
elif opcion == "6":
    print("Has elegido la Opción 6. Prefieres el color Naranja")
elif opcion == "7":
    print("Has elegido la Opción 7. Prefieres el color Gris")
elif opcion == "8":
    print("Has elegido la Opción 8.Prefieres el color Morado")
elif opcion == "9":
    print("Has elegido la Opción 9. Prefieres el color Marron")
elif opcion == "10":
    print("Has elegido la Opción 10. Prefieres el color Amarillo") 
else:
    print("Opción no válida. Por favor, elige una opción válida del menú.")



print ('\n10. Información Personal:')

nombre = input('ingresa tu nombre:..')
edad = int(input('ingresa tu edad:..'))
ciudad = input('ingresa tu ciudad:..')
residencia = input('ingresa tu residencia:..')

print('\n Tus datos personales son')
print('Tu nombre es:',nombre)
print('Tu edad es:',edad)
print('Tu ciudad es:',ciudad)
print('Tu lugar de residencia es:',residencia)


print ('\n11. Dibujo Simple:')

print('    /\ ')
print('   /  \ ')
print('  /    \ ')
print(' /______\ ')
print('  |    |')
print('  |    |')
print('  |____|')


print ('\n12. Lista de Frutas:')

frutas = ['Manzana', 'Uva', 'Banana', 'limon', 'Naranja', 'fresa']

for i in frutas:
    print(i)

print ('\n13. Mensaje de Confirmación:')

respuesta = input("¿Estás seguro de que deseas continuar? (sí/no): ")

if respuesta == "sí" or respuesta == "si":
    print("Has confirmado que deseas continuar.")
elif respuesta == "no":
    print("Has decidido no continuar.")
else:
    print("Respuesta no válida. Por favor, ingresa 'sí' o 'no'.")


print ('\n14. Mensaje de Éxito:')
print ('Juguemos,¿ le ganas a la maquina? ')
a= int(input('Ingresa el primer numero entero:..'))
b= int(input('Ingresa el segundo numero entero:..'))
print('Cuanto es la suma de',a, '+', b)
resul = int(input('Ingresa el resultado que crees:..'))

suma = a+b
if resul == suma:
            print('FELICIDADES!!!!!!! LE HAS GANADO A LA MAQUINA')


print ('\n15. Mensaje de Felicitación:')
nombre = input("Por favor, ingresa tu nombre: ")
logro = input("Me puedes escribir un logro o hito que hayas logrado: ")


print(f"¡Felicitaciones, {nombre}! Has alcanzado un hito importante: {logro}.")
print("Estamos muy orgullosos de ti y de tus logros. ¡Sigue así!")


input('')

