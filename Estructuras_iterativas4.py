"""En una escuela, luego de tomar un determinado examen, 
es necesario calcular el promedio de notas 
(las notas van de 0 a 10) de los alumnos de un curso. 
Se necesita saber si el rendimiento ha sido elevado 
(el promedio es mayor a 8), 
aceptable (el promedio está comprendido entre 6 y 8) 
o bajo (promedio es inferior a 6). 
Desarrollar un algoritmo que resuelva este problema. 
Para tener en cuenta: 
las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen."""


cantidad_alumnos = 12
suma_notas = 0

for _ in range(cantidad_alumnos):
    nota = float(input("Ingrese la nota del alumno (de 0 a 10): "))
    suma_notas += nota

promedio = suma_notas / cantidad_alumnos

if promedio > 8:
    print("El rendimiento es elevado.")

elif 6 <= promedio <= 8:
    print("El rendimiento es aceptable.")
    
else:
    print("El rendimiento es bajo.")
