'''PARTE I

REALICE ESTOS PROGRAMAS HACIENDO USO DEL CICLO FOR 

1.Escriba un programa que pregunte cuántos números se van a introducir,
pida esos números y muestre cuántos números negativos ha introducido'''
print('ejercio 1')
#Preguntar al usuario cuantos numeros se van a introducir
n = int(input('cuantos numeros vas a introducir?:...'))

#Inicializar el contador de numeros negativos
numeros_negativos=0

#Pedir al usuario que ingrese los numeros y contar los negativos
for x in range (n):
            i = int(input(f'Introduce el numero {x+1}:...'))
            if i < 0:
                numeros_negativos += 1

#Mostrar el resultado
print(f'la cantidad de numeros negativos es de: {numeros_negativos}')


print('\n ejercio 2')
'''2. Escriba un programa que solicite dos numeros. Debe mostrar
la secuencia descendente desde el numero mas grande hasta el numero menor.'''

#Solicitar los dos numeros
a=int(input('\n Ingrese el primer numero por favor:...'))
b=int(input('Ingrese el segundo numero por favor:...'))

#Evaluar el mayor o menor y mostrar la secuencia
print('\n La secuencia de numeros descendente es:')
if a > b:
    for i in range (a,b-1,-1):
        print(i)
elif b > a:
    for i in range (b,a-1,-1):
        print(i)


'''3.Escriba un programa que solicite un numero al usuario. Si el numero es mayor
que 10 y es impar, mostrar la secuencia de ascendente del 100 al 500, de 10 en
10. Si es mayor que 10 y es par mostrar un saludo 5 veces.
Si es menor o igual que 10 mostrar su nombre y matricula 15 veces.'''

print('\n ejercio 3')
#solicitar numero al usuario
n= int(input('\n Ingrese un numero por favor'))

#Mostrar la secuencia ascendente
if n > 10 and n%2 == 1:
    for i in range(100,510,+10):
        print(i)

#Mostrar saludo 5 veces
elif n > 10 and n%2==0:
    for x in range(1,5+1,):
        print('Hello')

#Mostrar nombre y matricula 5 veces
elif n <= 10:
    for x in range(1,5+1,):
        print('Pamela Blanco, 2023-1668')     


#PARTE II. (USO DE ARREGLOS)
'''1. PROGRAMA QUE LE PIDA AL USUARIO 5 NÚMEROS Y LOS ALMACENE EN UN ARREGLO. CUANDO
EL USUARIO TERMINE DE INGRESARLOS  DEBE MOSTRAR LA SUMATORIA DE ESOS NÚMEROS.'''

print('\n ejercio 1.2')
#Declar el arreglo
a = []
suma = 0

#ingresar los datos y sumar
for i in range (5):
    a = float(input(f'\n ingrsa el numero {i+1}:'))
    suma += a
    
print('La suma de todos los datos ingresados es:..', suma)




'''2.PROGRAMA QUE RECIBA 7 NÚMEROS DE PARTE DEL USUARIO. DEBE VERIFICAR
SI DENTRO DE ELLOS ESTA EL 23. EN CASO DE QUE ASÍ SEA,MOSTRAR
UN SALUDO Y SALIR. EN CASO CONTRARIO MOSTRAR UNA DESPEDIDA Y SALIR.'''

print('\n ejercio 2.2')

#Declar el arreglo
a = []

#ingresar los datos 
for i in range (7):
    x = int(input(f'\n ingrsa el numero {i+1}:'))
    a.append(x)


if x == 23:
    print('Hola, encontre tu numero!!!!')
else:
    print('Adios!!!! no encontre tu numero')
    


'''3.PROGRAMA QUE LEA 10 NÚMEROS ENTEROS INGRESADOS POR EL USUARIO Y LOS INSERTE EN UN ARREGLO.
A CONTINUACIÓN, EL PROGRAMA DEBE CONTAR Y CLASIFICAR CUÁNTOS NÚMEROS PARES
Y CUÁNTOS NÚMEROS IMPARES HAY DENTRO DEL ARREGLO, Y MOSTRAR ESOS RESULTADOS.'''

print('\n ejercio 3.2')
#Declarar arreglo
arreglo = []
suma_par=0
suma_impar=0
for i in range(10):
    x= int(input(f'\n Ingresa el valor{i+1}:'))
    arreglo.append(x)
    if x%2 ==0:
        suma_par += 1
    else:
        suma_impar += 1
print(f'La cantidad de numeros pares es de {suma_par}')
print(f'La cantidad de numeros impares es de {suma_impar}')


'''
4.PROGRAMA QUE LEA 5 NÚMEROS POR TECLADO. DEBE COPIAR LOS VALORES EN UN SEGUNDO ARREGLO,
SIGUIENDO ESTE REQUERIMIENTO:


SI EL NUMERO DE TURNO DEL PRIMER ARREGLO ES PAR, COPIARLO AL SEGUNDO ARREGLO MULTIPLICADO
POR 10
EN CASO CONTRARIO COPIARLO AL SEGUNDO ARREGLO TAL COMO ESTA.
'''
print('\n ejercio 4.2')
#Declarar arreglo
primer_arreglo =[]
segundo_arreglo=[]

for i in range(5):
    n = int(input(f'\n Ingresa el numero{i+1}:'))
    primer_arreglo.append(n)

    if n%2==0:
        segundo_arreglo.append(n*10)
    else:
        segundo_arreglo.append(n)
print('Los valores del primer arreglo son')
print(primer_arreglo)
print('Los valores del segundo arreglo son')
print(segundo_arreglo)
                  
