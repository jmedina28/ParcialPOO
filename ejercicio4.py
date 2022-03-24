class Cuenta():
    def __init__(self, idaccount, nombre, apertura, numero, saldo, modo): # Desarrollo el constructor
        self.id = idaccount
        self.nombre = nombre
        self.apertura = apertura
        self.numero = numero
        self.saldo = saldo
        self.modo = modo

A = Cuenta(21323434, "Juan", "2 de enero", 23294934, 10000, 1)