"""Mostrar sólo los números pares desde 0 hasta el número ingresado (input)
Nota: 
para saber si un número es par hacer i % 2 == 0)"""


numero = int(input("Ingrese un número: "))


for i in range(numero + 1):

    if i % 2 == 0:
        
        print(i)
