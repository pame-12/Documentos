print('Pamela Blanco Vincent')
print('2023-1668')
print('\n')

class libro:
    def __init__ (self, titulo, autor, anio_publicacion, genero):
        self.titulo= titulo
        self.autor=autor
        self.anio_publicacion=anio_publicacion
        self.genero=genero



    def descripcion(self):
            return f"El libro {self.titulo} de {self.autor}, fue publicado en {self.anio_publicacion} y es de genero {self.genero}."

    def __str__(self):
        return self.descripcion()



mi_libro=libro("1984", "George Orwell", 1949, "Distopia")
print(mi_libro.titulo)
print(mi_libro.autor)
print(mi_libro.anio_publicacion)
print(mi_libro.genero)
    
mi_libro = libro("1984", "George Orwell", 1949, "Distopia")
print(mi_libro)

input()
