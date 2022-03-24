# Ejercicio 1
class Libro():
    def __init__(self, titulo, npaginas, fechapublicacion, autor, isbn):
        self.titulo = titulo
        self.npaginas = npaginas
        self.fechapublicacion = fechapublicacion
        self.autor = autor
        self.isbn = isbn
    # Estos son los getter
    def titulo(self):
        return self.titulo
    def npaginas(self):
        return self.npaginas
    def fechapublicacion(self):
        return self.fechapublicacion
    def autor(self):
        return self.autor
    def isbn(self):
        return self.isbn
    # desarrollando los setter
    def titulo(self, nuevo):
        print ("Modificamos el título")
        self.titulo = nuevo
        print ("El título se ha sustituido por")
        print (self.titulo) #Aquí vuelvo a pedir que retorne el atributo para confirmar

l = Libro("1984", "326","1949","George Orwell",
9788499890944)
l.titulo = "Rebelión en la granja"
print(l.titulo)

