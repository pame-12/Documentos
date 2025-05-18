'''#diccionario en paython
productos = {}
print (productos)
print (type(productos))

productos = {
    'Nombre' : 'Libro de python',
    'Cantidad': 5,
    'Precio':  500.00}
print(productos)

print( '')
print( 'Trabajando con diccionario en python')
print( '')

#Diccionario la agenda = nombre, direccion, telefonp, email
agenda= {
    'Bernardo':['Santo Somingo', 8295677898, 'bbatista.edu.do'],
    'Paulina': ['Villa Mella', 8096784576, 'paulinagimenez.edu.do'],
    'Alain': {'direccion': 'ciudad juan bosch', 'Telefono': 8294556909, 'Email':
              'alain@gmail.com'}
    }

print(agenda)
print('valores')
print(agenda.values())
print('keys')
print(agenda.keys())

print('ver contacto')
print(f' Informacion del contacto...: {agenda["Paulina"]}')

print('imprimir un contacto')

existePaulina= ('Paulina' in agenda)
if existePaulina:
    print(agenda['Paulina'])
else:
    print('En la agenda no hay ninguna paulina')

#Con el comando Get se busca un contacto que exista, si no existe
#presenta una segunda opcion
print('imprimir un contactocon el comando get')
print(agenda.get('Paulina', 'Paulina no esta'))

print('items')
print(agenda.items())

print(len(agenda))


guardarlo para visualizar despues print('\n')
print('======:: Practica con un diccionario en python ======')
print('\n')

#crear el diccionario
usuario = { 'id': [],
            'nombre': [],
            'celular': []
            }

#definir el tamano
tamano = 3

#leer datos para llenar el diccionario desde el teclado
for i in range (tamano):
    print('\t================================================')
    print('\t por favor ingrese los datos del usuario...:', i + 1)
    print('\t================================================')
    print('\n')
    id = input('Por favor ingrese el id del usuario...: ')
    nombre = input('Por favor ingrese el nombre del usuario...: ')
    celular = input('Por favor ingrese el numero del usuario...: ')


    #Agregar datos para llenar el diccionario
    usuario['id'].append(id)
    usuario['nombre'].append(nombre)
    usuario['celular'].append(celular)
     
     
for i in range (tamano):
    print('\t================================================')
    print('\t visualizar los datos del usuario...:', i + 1)
    print('\t================================================')
    print('\n')


    print('id...:', usuario['id'] [i])
    print('nombre...:', usuario['nombre'] [i])
    print('celular...:', usuario['celular'] [i])



print('\t================================================')
print('\t visualizar el diccionario completo...:')
print('\t================================================')
print('\n')
print(usuario)


'''

    


print('\n')
print('======:: Practica con un diccionario en python ======')
print('\n')

#crear el diccionario
usuario = { 'id': [],
            'nombre': [],
            'celular': []
            }

#definir el tamano
tamano = 3

'''#leer datos para llenar el diccionario desde el teclado
for i in range (tamano):
    print('\t================================================')
    print('\t por favor ingrese los datos del usuario...:', i + 1)
    print('\t================================================')
    print('\n')
    id = input('Por favor ingrese el id del usuario...: ')
    nombre = input('Por favor ingrese el nombre del usuario...: ')
    celular = input('Por favor ingrese el numero del usuario...: ')


    #Agregar datos para llenar el diccionario
    usuario['id'].append(id)
    usuario['nombre'].append(nombre)
    usuario['celular'].append(celular)
     
     
for i in range (tamano):
    print('\t================================================')
    print('\t visualizar los datos del usuario...:', i + 1)
    print('\t================================================')
    print('\n')


    print('id...:', usuario['id'] [i])
    print('nombre...:', usuario['nombre'] [i])
    print('celular...:', usuario['celular'] [i])



print('\t================================================')
print('\t visualizar el diccionario completo...:')
print('\t================================================')
print('\n')
print(usuario)'''


while True:
    print('\n\n')
    print('1.- agregar un dato al diccionario')
    print('2.- modificar un dato al diccionario')
    print('3.- visualizar un dato al diccionario')
    print('4.- eliminar un dato al diccionario')
    print('5.- limpiar un dato del diccionario')
    print('0.- salir del sistema')

    opcion = int(input('Seleccione una opción: '))
    

    if opcion== 0:
                 
                 print('Gracias por usar nuestros servicios')
                 break
                
    elif opcion == 1:
        
        #leer datos para llenar el diccionario desde el teclado
        for i in range (tamano):
            
            print('\t================================================')
            print('\t por favor ingrese los datos del usuario...:', i + 1)
            print('\t================================================')
            print('\n')
            id = input('Por favor ingrese el id del usuario...: ')
            nombre = input('Por favor ingrese el nombre del usuario...: ')
            celular = input('Por favor ingrese el numero del usuario...: ')


    #Agregar datos para llenar el diccionario
    usuario['id'].append(id)
    usuario['nombre'].append(nombre)
    usuario['celular'].append(celular)
    
    print("Usuario agregado exitosamente.")

   
   elif opcion 2:
       
       




