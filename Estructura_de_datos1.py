
nombres = []


for i in range(10):
    nombre = input("Ingrese un nombre: ")
    
    
    if nombre in nombres:
        print("Este nombre ya ha sido ingresado. Por favor, ingrese otro.")
    else:
        nombres.append(nombre)


print("\nLos nombres ingresados son:")
for nombre in nombres:
    print(nombre)
