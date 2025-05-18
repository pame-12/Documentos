def metodo_1():
    print("Hala soy el metodo 1")

class miclase:
    variable = 5
    def metodo_2(self):
        print(self.variable)

        
metodo_1()
objeto=miclase()
objeto.metodo_2()
