cadena = input("Ingrese una cadena: ")
minusculas = 0
mayusculas = 0
for palabra in cadena:
    if palabra == ".":
        break
    if "a" <= palabra <= "z":
        minusculas += 1
    elif "A" <= palabra <= "Z":
        mayusculas += 1
print("Cantidad de minúsculas:",minusculas)
print("Cantidad de mayúsculas:",mayusculas)