#Escribe un programa que pida al usuario que ingrese dos números y determine cuál es el número más grande.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print("El primer número es el más grande.")
elif numero2 > numero1:
    print("El segundo número es el más grande.")
else:
    print("Ambos números son iguales.")