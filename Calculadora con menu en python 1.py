# Calculadora con menu en python 

while True:

    print('\n\tCalculadora con menu en python\n')

    print('Menu Principal para las operaciones arimeticas')

    print('1.- Sumar')

    print('2.- Restar')

    print('3.- Dividir')

    print('4.- Multiplicar')

    print('5.- Potencia')

    print('6.- Modulo')

    print('7.- Division Exacta')

    print('0.- Salir')



    opcion = int(input('Favor elegir la opcion a realizar'))

    if opcion > 0: 



        numero1 = int(input('Favor digitar el numero uno...: '))

        numero2 = int(input('Favor digitar el numero dos...: '))



        #numero1 = 15

        #numero2 = 5

        #suma

        match opcion:

            case 1:

                resultado = numero1 + numero2

                print(f' el resultado de la suma es...: {resultado}')

            case 2:

              #resta

                

                #resultado = numero1 - numero2

                print(' el resultado de la resta es...: ', numero1 - numero2)

            case 3:

              #division

                if numero2 > 0:

                    resultado = numero1 / numero2

                    print(' el resultado de la division es...: ', resultado)

                else:

                    print('ERROR:  No podemos dividir entre 0')

            case 4:

              #multiplicacion

                #resultado = numero1 * numero2

                print(f' el resultado de la suma es...: {numero1 * numero2}')

            case 5:

              #potencia

                resultado = numero1 ** numero2

                print(' el resultado de la potencia es...: ', resultado)

            case 6:

              #modulo

                resultado = numero1 % numero2

                print(' el resultado del modulo es...: ', resultado)

            case 7:

              #division exacta

                resultado = numero1 // numero2

                print(' el resultado de la division exacta es...: ', resultado)

            case 0:

                print('Saliendo del programa')

                

                break

            case _:

                print('La opcion seleccionada no existe, favor elegir una del menu')

    else:

        print('Saliendo del programa')

        break        

