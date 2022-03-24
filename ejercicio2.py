class Animal():
    def __init__(self, nombre):
        self.nombre = nombre
class Mamifero(Animal):
    Animal.__init__()
class Oviparo(Animal):
    Animal.__init__()
class Pollo(Oviparo):
    Oviparo.__init__()
class Gato(Mamifero):
    Mamifero.__init__()
class Ornitorrinco(Mamifero):
    Mamifero.__init__()