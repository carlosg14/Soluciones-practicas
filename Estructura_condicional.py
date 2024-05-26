"""Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
Si el cliente compra más de 12  unidades (y hasta 24 unidades), 
el costo tiene un descuento del 10%. 
Si compra más de 24 unidades, el descuento es del 15%. 
Además posee la promoción a los jubilados. 
La promoción de jubilados es sumarle un 10% de descuento 
(si posee otros descuentos, se suma los descuentos)."""


unidadesDeLeche = int(input("Ingrese la cantidad de unidades de leche que compra el cliente"))
esJubiado = int(input("Ingrese 0 si el cliente no es jubilado, cualquier otro numero si el cliente es Jubilado"))

montoParcial = unidadesDeLeche * 1000
print(f"unidadesDeLeche {unidadesDeLeche} esJubiado {esJubiado}")
#unidadesDeLeche = 15 y esJubiado=1
if(unidadesDeLeche <=12 and not esJubiado):
    print("unidadesDeLeche <=12 and not esJubiado")
    montoAPagar = montoParcial
elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubiado):
    print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubiado")
    montoAPagar = montoParcial * 0.9
elif(unidadesDeLeche > 24 and not esJubiado):
    print("unidadesDeLeche > 24 and not esJubiado")
    montoAPagar = montoParcial * 0.85
elif(unidadesDeLeche <=12 and esJubiado):
    print("unidadesDeLeche <=12 and esJubiado")
    montoAPagar = montoParcial * 0.9
elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubiado):#ok
    print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubiado")#ok
    montoAPagar = montoParcial * 0.8
elif(unidadesDeLeche > 24 and esJubiado):
    print("unidadesDeLeche > 24 and esJubiado")
    montoAPagar = montoParcial * 0.75

print(f"El monto sin descuento es: {montoParcial} y el monto total a pagar es: {montoAPagar}")