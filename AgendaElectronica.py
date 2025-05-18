import mysql.connector
from datetime import datetime

class AgendaElectronica: # Clase para manejar la agenda electrónica
    def __init__(self):
        # Inicializa la conexión con la base de datos MySQL
        self.conn = mysql.connector.connect(
            host="localhost",# Host donde se encuentra la base de datos
            user="root",# Usuario para conectar a la base de datos
            password="Pbv.120803",# Contraseña del usuario
            database="agenda" # Nombre de la base de datos
        )
        self.cursor = self.conn.cursor() # Crea un cursor para ejecutar consultas SQL

    # Método para guardar un nuevo evento en la base de datos
    def guardar(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingresa el apellido: ")
        telefono = input("Ingresa el teléfono: ")
        correo = input("Ingresa el Correo electrónico: ")
        direccion = input("Ingresa la dirección: ")
        fecha_nacimiento = input("Ingresa la fecha de nacimiento (YYYY-MM-DD): ")
        fecha_inicio = input("Ingresa la fecha de inicio del evento (YYYY-MM-DD HH:MM:SS): ")
        fecha_fin = input("Ingresa la fecha de fin del evento (YYYY-MM-DD HH:MM:SS): ")
        notas = input("Ingresa tus nota del evento: ")


        # Consulta SQL para insertar un nuevo registro en la tabla AgendaElectronica
        query = """ INSERT INTO AgendaElectronica
                    (Nombre, Apellido, Telefono, CorreoElectronico, Direccion, 
                    FechaNacimiento, FechaInicioEvento, FechaFinEvento, Notas)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (nombre, apellido, telefono, correo, direccion, 
                  fecha_nacimiento, fecha_inicio, fecha_fin, notas)
        
        self.cursor.execute(query, values)# Ejecuta la consulta SQL con los valores proporcionados
        self.conn.commit()# Confirma los cambios en la base de datos
        print("Evento guardado exitosamente.")
        print(f"ID del evento guardado: {self.cursor.lastrowid}")
        
    # Método para actualizar un evento existente
    def actualizar(self): 
        self.mostrar_eventos() 
        id = input("Ingrese el ID del evento a actualizar: ")
        print("Campos disponibles: Nombre, Apellido, Telefono, CorreoElectronico, Direccion, FechaNacimiento, FechaInicioEvento, FechaFinEvento, Notas")
        campo = input("Ingrese el campo a actualizar: ")
        valor = input("Ingrese el valor a actualizar: ")

        # Consulta SQL para actualizar un registro específico
        query = f"UPDATE AgendaElectronica SET {campo} = %s WHERE ID = %s"
        self.cursor.execute(query, (valor, id))# Ejecuta la consulta SQL con el nuevo valor
        self.conn.commit() # Confirma los cambios en la base de datos
        print("Evento actualizado exitosamente")

        
    # Método para borrar un evento
    def borrar(self):
        self.mostrar_eventos()
        id = input("Ingrese el ID del evento a borrar: ")

        # Consulta SQL para borrar un registro específico
        query = "DELETE FROM AgendaElectronica WHERE ID = %s"
        self.cursor.execute(query, (id,))# Ejecuta la consulta SQL para borrar el evento
        self.conn.commit()# Confirma los cambios en la base de datos
        print("Evento borrado exitosamente.")

        
    # Método para buscar eventos por un campo específico
    def buscar(self):
        print("Campos disponibles: Nombre, Apellido, Telefono, CorreoElectronico, Direccion, FechaNacimiento, FechaInicioEvento, FechaFinEvento, Notas")
        campo = input("Ingresa el campo que deseas buscar: ")
        valor = input("Ingresa el valor a buscar: ")

        # Consulta SQL para buscar registros que coincidan con un valor específico
        query = f"SELECT * FROM AgendaElectronica WHERE {campo} LIKE %s"
        self.cursor.execute(query, (f"%{valor}%",))# Ejecuta la consulta SQL con el valor proporcionado
        resultados = self.cursor.fetchall()# Obtiene todos los resultados de la consulta
        
        if resultados:
            for resultado in resultados:
                self.mostrar_evento(resultado)
        else:
            print("No se encontraron resultados")

    def mostrar_eventos(self):
        self.cursor.execute("SELECT * FROM AgendaElectronica")
        eventos = self.cursor.fetchall()

        
        if eventos:
            for evento in eventos:# Muestra cada resultado encontrado
                self.mostrar_evento(evento)
        else:
            print("No hay eventos guardados.")

    # Método para mostrar los detalles de un evento específico
    def mostrar_evento(self, evento):
        print(f"ID: {evento[0]}")
        print(f"Nombre: {evento[1]}")
        print(f"Apellido: {evento[2]}")
        print(f"Teléfono: {evento[3]}")
        print(f"Correo Electrónico: {evento[4]}")
        print(f"Dirección: {evento[5]}")
        print(f"Fecha de Nacimiento: {evento[6]}")
        print(f"Fecha de Inicio del Evento: {evento[7]}")
        print(f"Fecha de Fin del Evento: {evento[8]}")
        print(f"Notas: {evento[9]}")
        print("-" * 30)
        
    # Método para mostrar el menú principal y manejar la interacción del usuario
    def menu(self):
        while True:
            print("\n--- Agenda Electrónica ---")
            print("1. Guardar")
            print("2. Actualizar")
            print("3. Borrar")
            print("4. Buscar")
            print("5. Mostrar todos los eventos")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            # Maneja la selección del usuario y llama al método correspondiente
            if opcion == "1":
                self.guardar()
            elif opcion == "2":
                self.actualizar()
            elif opcion == "3":
                self.borrar()
            elif opcion == "4":
                self.buscar()
            elif opcion == "5":
                self.mostrar_eventos()
            elif opcion == "6":
                print("Gracias por usar la Agenda Electrónica.")
                break
            else:
                print("La opción no es válida. Intente otra opción")
# Punto de entrada del programa
if __name__ == "__main__":
    agenda = AgendaElectronica()
    agenda.menu()
