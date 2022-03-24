# Ejercicio 1
class Libro():
    def __init__(self, titulo, npaginas, fechapublicacion, autor, sbn):
        self.titulo = titulo
        self.npaginas = npaginas
        self.fechapublicacion = fechapublicacion
        self.autor = autor
        self.sbn = sbn
    # Estos son los getter
    def titulo(self):
        return self.titulo
    def npaginas(self):
        return self.npaginas
    def fechapublicacion(self):
        return self.fechapublicacion
    def autor(self):
        return self.autor
    def sbn(self):
        return self.sbn
    # desarrollando los setter
    def titulo(self, nuevo):
        print ("Modificamos el título")
        self.titulo = nuevo
        print ("El título se ha sustituido por")
        print (self.titulo) #Aquí vuelvo a pedir que retorne el atributo para confirmar

l = Libro("1984", "d","s","George Orwell",121213)
l.titulo = "Rebelión en la granja"
print(l.titulo)

