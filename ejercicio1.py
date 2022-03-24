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
    # desarrollo los setter