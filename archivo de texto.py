#procesar archivo en plano TXT en python

#crear un archivo nuevo de tipo texto
print ('creando un archivo')
#nuevotxt = open ('archivo.txt','x')

'''
modo
r= leer
a= anexar(agregar)
w= escribir
x=crear en blanco


print('agregando datos al archivo')
file = open('arch_pame.txt', 'a')
file.write('\nBernardo Batista      bbatista@itla.edu.do        profesor3')
file.close()


print('leyendo el archivo')
print('\n')
file = open('arch_pame.txt', 'r')
print(file.read())
file.close()
'''
#leer el archivo por linea = readline()
print('leer archivo plano por linea (iterar)')
file = open('arch_pame.txt', 'r')
for registro in file:
    if registro.startswith('Bernardo'):
        print('El nombre es Bernardo y tiene mas de 70')
        print(registro)
    elif registro.startswith('Antonio'):
        print('El nombre es Antonio ')
        print(registro)
file.close()
