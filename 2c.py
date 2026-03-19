#Escribe un programa que muestre las tablas de multiplicar del 1 al 10.

for j in range(1, 11):
    for i in range(1, 11):
        print(f"{j} x {i} = {j * i}")