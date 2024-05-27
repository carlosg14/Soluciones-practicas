Algoritmo Equipo_futbol
	Definir PG, PE, PP Como Entero
	definir PtsG, PtsE, Pts, part como entero
	
	escribir "nombre del equipo"
	leer eq
	
	escribir "ingrese la cantidad de partidos ganados"
	Leer PG
	
	escribir "ingrese la cantidad de partidos empatados"
	Leer PE
	
	escribir "ingrese la cantidad de partidos `perdidos"
	Leer PP
	
	PtsG<-PG*3
	PtsE<-PE*1
	Pts= PtsG+PtsE
	part=PG+PE+PP
	
	Escribir "equipo: ", eq, "jugo: ", part, "partidos"
	
	Escribir "Gano: ", PG " partidos"
	
	Escribir "Empato: ", PE " partidos"
	
	Escribir "Perdio: ", PP " partidos"
	
	Escribir "puntos acumulados", Pts
	
FinAlgoritmo
