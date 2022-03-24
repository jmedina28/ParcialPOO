class Animal():
    def __init__(self, nombre):
        self.nombre = nombre
class Mamifero(Animal):
    def __init__(self,nombre,especie):
        Animal.__init__(self,nombre)
        self.especie = especie
class Oviparo(Animal):
    def __init__(self,nombre,especie):
        Animal.__init__(self,nombre)
        self.especie = especie
class Pollo(Oviparo):
    def __init__(self, nombre, especie, edad):
        Oviparo.__int__(self, nombre, especie)
        self.edad = edad
class Gato(Mamifero):
    def __init__(self, nombre, especie, edad):
        Mamifero.__int__(self, nombre, especie)
        self.edad = edad
class Ornitorrinco(Mamifero):
    def __init__(self, nombre, especie, edad):
        Mamifero.__init__(self, nombre, especie)
        self.edad = edad        
ornitorrinco = Ornitorrinco("Perry", "ornitorrinco",3)

print(ornitorrinco.nombre)