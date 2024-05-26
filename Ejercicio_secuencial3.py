"""Un hincha de fútbol desea conocer la cantidad de puntos que su

equipo lleva acumulados en el campeonato, para ello recibe cada semana la

información de la cantidad total de partidos, desde el inicio del campeonato, que

el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado

recibe un punto, por cada partido ganado tres puntos y por los perdidos cero

puntos."""


partidos_ganados = int (input ("ingrese la cantidad de partidos ganados: "))
partidos_empatados = int (input ("ingrese la cantidad de partidos empatados: "))
partidos_perdidos = int (input ("ingrese la cantidad de partidos perdidos: "))

puntos_obtenidos_G = partidos_ganados * 3
puntos_obtenidos_E = partidos_empatados 

Puntos_totales= puntos_obtenidos_E + puntos_obtenidos_G

partidos_jugados= partidos_empatados + partidos_ganados + partidos_perdidos


print("Los puntos que consiguio el equipo es un total de: " , Puntos_totales)
print ("Los partidos que jugaron son: " , partidos_jugados)