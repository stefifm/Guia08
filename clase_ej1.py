# suma = 0
# i = 1
# while i <= 5:
#     n = int(input("Numero mayor a cero: "))
#     if n <= 0:
#         break
#     suma += n
#     i += 1
# print("Suma de los números ingresados es:",suma)

# suma = 0
# for i in range(5):
#     n = int(input("Numero mayor a cero: "))
#     if n <= 0:
#         break
#     suma += n
# print("Suma de los números ingresados es:",suma)

# suma = 0
# i = 1
# while i <= 5:
#     n = int(input("Numero mayor a cero: "))
#     if n > 0:
#         continue
#     suma += n
#     i += 1
# print("Suma de los números ingresados es:",suma)

# suma = 0
# for i in range(5):
#     n = int(input("Numero mayor a cero: "))
#     if n <= 0:
#         continue
#     suma += n
# print("Suma de los números ingresados es:",suma)

n = int(input("Ingrese un número: "))

if n < 0:
    pass
else:
    print("El valor es positivo")