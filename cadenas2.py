print("Procesamiento de cadenas")

cont_vocales = 0
cont_consonantes = 0
cont_palabras = 1
cont_la = 0
cont_letras = -1
vocales = "aeiouAEIOU"
cadena = input("Cargue una cadena de caracteres: ")
for letra in cadena:
    cont_letras += 1
    if letra in vocales:
        cont_vocales += 1
    else:
        if letra != " ":
            cont_consonantes += 1
        else:
            cont_palabras += 1
    if cont_letras > 0:
        if letra == "a":
            if cadena[cont_letras-1] == "l" or cadena[cont_letras-1] == "L" \
                    and (cont_letras == 2 or cadena[cont_letras-2] == " "):
                cont_la += 1

print("Cantidad de vocales:",cont_vocales)
print("Cantidad de consonantes:",cont_consonantes)
print("Cantidad total de palabras:",cont_palabras)
print("Cantidad de palabras que comienzan con la:",cont_la)
