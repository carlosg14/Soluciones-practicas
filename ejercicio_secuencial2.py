"""EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo

que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

cliente le indica que necesita conocer el costo de mano de obra para pintar una

pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

pintar la pared."""


metros_cuadrados= float (input("Ingrese los metros cuadrados a pintar: "))

monto_por_metrocuadrado= 1000

precio_total= metros_cuadrados*monto_por_metrocuadrado

print ("El precio final del trabajo es de: $", precio_total)
