"""Pedir que el usuario ingrese (input) nombre de personas y 
mostrarlos hasta que el valor de lo que ingresa sea “fin”"""

nombre = ""

while nombre != "fin":

    nombre = input("Ingrese un nombre (o 'fin' para terminar): ")

    if nombre != "fin":
        
        print(nombre)
