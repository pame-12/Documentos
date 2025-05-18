
#Herencia
class empleado:
    def __init__(self, nombre, salario):
        self.nombre=nombre
        self.salario=salario

    def mostrar_info(self):
        return f" Nombre: {self.nombre}, Salario: {self.salario}"

    def aumentar_salario(self, porcentaje):
        incremento = self.salario * (porcentaje / 100)
        self.salario += incremento
        return self.salario
    

class gerente(empleado):
        def __init__(self, nombre, salario, departamento):
            super().__init__(nombre, salario)
            self.departamento=departamento
            
        def mostrar_info(self):
            return f"Nombre: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}"

class desarrollador(empleado):
        def __init__(self, nombre, salario, lenguaje_programacion):
            super().__init__(nombre, salario)
            self.lenguaje_programacion=lenguaje_programacion

        
        def mostrar_info(self):
            return f" Nombre: {self.nombre}, Salario: {self.salario}, Lenguage de programacion: {self.lenguaje_programacion}"


mi_gerente=gerente("pamela", 20000, "Ventas")
mi_desarrollador=desarrollador("Juan", 40000, "programacion")

mi_gerente.aumentar_salario(10)
mi_desarrollador.aumentar_salario(10)

print(mi_gerente.mostrar_info())
print(mi_desarrollador.mostrar_info())
