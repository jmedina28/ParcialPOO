import random
from datetime import datetime
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
        decision = int(input("¿Desea continuar realizando operaciones? En caso afirmativo pulse 1, en caso contrario pulse cualquier otra tecla por favor: "))
        if decision == 1:
            operacion()
        else:
            exit()        
    def ingreso(self):
        dineroingreso = int(input("""Ha seleccionado usted la opción de ingresar dinero a su cuenta.

¿Cuánto dinero desea ingresar?(Esta operación es libre de comisiones.)

"""))
        self.saldo += dineroingreso
        print("Usted ha ingresado " + str(dineroingreso) + "€ y su saldo actualmente es de " + str(self.saldo) + "€.")
        decision = int(input("¿Desea continuar realizando operaciones? En caso afirmativo pulse 1, en caso contrario pulse cualquier otra tecla por favor: "))
        if decision == 1:
            operacion()
        else:
            exit()      
    def transferencia(self):
        if A.modo != 1:    
            dinerotransferencia = int(input("""Ha seleccionado usted la opción de transferir dinero a otra cuenta.

    ¿Cuánto dinero desea transferir?(Esta operación es libre de comisiones.)

"""))
            if 0 < dinerotransferencia <= self.saldo*2:    
                A.saldo -= dinerotransferencia
                B.saldo += dinerotransferencia
                print("Usted ha transferido " + str(dinerotransferencia) + "€ y su saldo actualmente es de " + str(self.saldo) + "€.")
                print("El saldo de la cuenta B es de " + str(B.saldo) + "€.")
            decision = int(input("¿Desea continuar realizando operaciones? En caso afirmativo pulse 1, en caso contrario pulse cualquier otra tecla por favor: "))
            if decision == 1:
                operacion()
            else:
                exit()
        else:
            dinerotransferencia = int(input("""Ha seleccionado usted la opción de transferir dinero a otra cuenta.

¿Cuánto dinero desea transferir?(Esta operación es libre de comisiones.)

"""))

            if 0 < (dinerotransferencia + dinerotransferencia * 0.05) <= self.saldo:        
                A.saldo -= dinerotransferencia + dinerotransferencia * 0.05
                B.saldo += dinerotransferencia
                print("Usted ha transferido " + str(dinerotransferencia) + "€ y su saldo actualmente es de " + str(self.saldo) + "€.")
                print("El saldo de la cuenta B es de " + str(B.saldo) + "€.")
                decision = int(input("¿Desea continuar realizando operaciones? En caso afirmativo pulse 1, en caso contrario pulse cualquier otra tecla por favor: "))
                if decision == 1:
                    operacion()
                else:
                    exit()

def creacioncuenta():
            nombre = str(input("""Ha seleccionado usted la opción de crear una cuenta bancaria.

Introduzca su nombre por favor: 

"""))
            global A, B
            modo = int(input("Si desea crear una cuenta a plazo fijo pulse 1, en cambio si desea crear una cuenta VIP pulse cualquier otro valor: "))
            numero = str(random.randint(100000000000, 999999999999))
            A = Cuenta(str(random.randint(100000, 999999)), nombre, datetime.today(),numero, 10000, modo)
            print("Hola " + nombre + ". Usted ha creado una cuenta en nuestro banco a fecha de " + str(datetime.today()) + " con el número de cuenta: " + numero)
            B = Cuenta(str(random.randint(100000, 999999)), "Persona B", datetime.today(), str(random.randint(100000000000, 999999999999)), 10000, 5)
            print("La segunda cuenta con la que va a poder operar ha sido creada por defecto a nombre de Esther, con un saldo también de 10000 euros y fue creada el 15/07/2014, es una cuenta VIP.")
def operacion():
    seleccion = int(input("""Introduzca que tipo de operación desea realizar:
- Pulse 1 si desea RETIRAR dinero de su cuenta.
-Pulse 2 si desea INGRESAR dinero a su cuenta.
-Pulse 3 si desea TRANSFERIR dinero de una cuenta a otra.
"""))
    if seleccion == 1:
        Cuenta.retiro(A)
    if seleccion == 2:
        Cuenta.ingreso(A)
    if seleccion == 3:
        Cuenta.transferencia(A)
creacioncuenta()
operacion()