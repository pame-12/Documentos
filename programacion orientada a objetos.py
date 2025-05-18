'''
class cuenta_bancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        return

    def depositar(self, cantidad):
        self.saldo += cantidad


    def retirar (self, cantidad):
        self.saldo -= cantidad

    def mostrar_informacion(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")


mi_cuenta = cuenta_bancaria('pamela')
mi_cuenta.mostrar_informacion()

mi_cuenta.depositar(1000)
mi_cuenta.mostrar_informacion()

mi_cuenta.retirar(200)
mi_cuenta.mostrar_informacion()
'''




class calculadora:
    def __init__(self):
        self.num1 = int(input("Introduce el primer valor entero: "))
        self.num2 = int(input("Introduce el segundo valor entero: "))
        

    def suma(self):
        sum = self.num1 + self.num2
        print('La suma de los numeros es:', sum)
    

    def resta(self):
        res = self.num1 - self.num2
        print('La resta de los numeros es:', res)

    def multiplicacion(self):
        mul = self.num1 * self.num2
        print('La multiplicacion de los numeros es:', mul)

    def divicion(self):
        divi = self.num1 / self.num2
        print('La divicion de los numeros es:', divi)
    
    def mostrar_valores(self):
        print("Los valores son: ")
        print("Valor 1: ", self.num1)
        print("Valor 2: ", self.num2)
        

calcular=calculadora()
calcular.mostrar_valores()
calcular.suma()
calcular.resta()
calcular.multiplicacion()
calcular.divicion()








        
