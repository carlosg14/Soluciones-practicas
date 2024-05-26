"""Un profesor de matemática necesita generar la tabla de multiplicar 
de un número entero comprendido entre 1 y 10. 
Por ejemplo para el 3 debería aparecer como salida:

3x1=3
3x2=6
3x3=9
…. y así hasta 10"""


#Ejercicio 5.2

"""5.2 Resuelva este problema utilizando un para 
y de modo que por la salida se emita la tabla tal como se propone."""


numero = int(input("Ingrese un número entre 1 y 10: "))

for i in range(1, 11):

    resultado = numero * i

    print(f"{numero}x{i}={resultado}")
