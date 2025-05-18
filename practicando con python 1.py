print('LE GANAS A LA MAQUINA')
         
print('Que quieres realizar')
print('1:.....Suma')
print('2:.....Resta')
print('3:.....Multiplicacion')
print('4:.....Divicion') 

opc = int(input('Elige la opcion que quieres realizar'))

if opc == 1:
    num1 = int(input('Ingresa tu primer numero:....'))
    num2 = int(input('Ingresa tu segundo numero:....'))
    suma = num1 + num2
    res = int(input('El resultado de la suma es:....'))
    if res == suma:
              print('FELICIDADES!!!!! ERES MUY INTELIENTE, LE GANASTE A LA MAQUINA')
    else:
        print('RESPUESTA INCORECTA, TE HA GANADO LA MAQUINA')
        
              
             
