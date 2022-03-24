class Cuenta():
    def __init__(self, idaccount, nombre, apertura, numero, saldo, modo): # Desarrollo el constructor
        self.id = idaccount
        self.nombre = nombre
        self.apertura = apertura
        self.numero = numero
        self.saldo = saldo
        self.modo = modo
    
    def retiro(self):
        dineroretirar = int(input("""Ha seleccionado usted la opción de retirar dinero de su cuenta.

¿Cuánto dinero desea retirar?(Esta operación es libre de comisiones.)

"""))
        if 0 < dineroretirar <= self.saldo:
            self.saldo = self.saldo - dineroretirar
            print("Usted ha retirado " + str(dineroretirar) + "€ y su saldo actualmente es de " + str(self.saldo) + "€.")
        
    def ingreso(self):
        dineroingreso = int(input("""Ha seleccionado usted la opción de ingresar dinero a su cuenta.

¿Cuánto dinero desea ingresar?(Esta operación es libre de comisiones.)

"""))
        self.saldo += dineroingreso
        print("Usted ha ingresado " + str(dineroingreso) + "€ y su saldo actualmente es de " + str(self.saldo) + "€.")
       
    def transferencia(self):
        dinerotransferencia = int(input("""Ha seleccionado usted la opción de transferir dinero a otra cuenta.

¿Cuánto dinero desea transferir?(Esta operación es libre de comisiones.)

"""))
        A.saldo -= dinerotransferencia
        B.saldo += dinerotransferencia
        print("Usted ha transferido " + str(dinerotransferencia) + "€ y su saldo actualmente es de " + str(self.saldo) + "€.")
        print("El saldo de la cuenta B es de " + str(B.saldo) + "€.")
            


A = Cuenta(21323434, "Juan", "2 de enero", 23294934, 10000, 1)
B = Cuenta(21323432, "Ruben", "5 de enero", 43294934, 20000, 1)
Cuenta.transferencia(A)