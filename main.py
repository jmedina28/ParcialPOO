variable = int(input("Seleccione que ejercicio desea ejecutar(1,2 ó 4): "))
if variable == 1:
    import ejercicio1
elif variable == 2:
    import ejercicio2
elif variable == 4:
    import ejercicio4
else:
    print("Introduzca valores entre 1,2 ó 4.")