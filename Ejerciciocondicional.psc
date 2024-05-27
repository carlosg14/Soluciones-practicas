Algoritmo leche
	Definir cant_unidades Como Numerica
	definir jubilado Como Caracter
	definir descuento10, descuento15, descuento20, descuento25 Como Real
	definir precio_leche Como Real
	Definir unidades Como Entero
	
	Escribir "¿sos jubilado?"
	leer jubilado
	
	escribir "coloque cuantas unidades desea"
	leer cant_unidades
	
	precio_leche<-1000
	descuento10<-precio_leche*cant_unidades*0.9
	descuento15<-precio_leche*cant_unidades*0.85
	descuento20<-precio_leche*cant_unidades*0.80
	descuento25<-precio_leche*cant_unidades*0.75
	precio_sin_descuento<-precio_leche*cant_unidades
	
	si jubilado="si" Entonces
		si cant_unidades<12 Entonces
			Escribir "el precio de la leche es $", descuento10
		SiNo
			si cant_unidades>=12 y cant_unidades<=24 Entonces
				Escribir "el precio de la leche es $", descuento20
			SiNo
				escribir "el precio de la leche es $", descuento25
			FinSi
		FinSi
	SiNo
		si cant_unidades <=12 Entonces
			Escribir "el precio de la leche es $", precio_sin_descuento
		sino
			si cant_unidades >12 y cant_unidades <=24 Entonces
				escribir "el precio de la leche es $", descuento10
			sino
				escribir "el precio de la leche es $", descuento15
			FinSi
			
		FinSi
	FinSi
	
FinAlgoritmo