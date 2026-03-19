#Escribe un programa que pida al usuario que ingrese un número y luego 
#muestre la suma de los números impares desde 1 hasta ese número.

numero = int(input("Ingrese un numero: "))
suma_impares = 0

for i in range (1, numero + 1, 2):
    suma_impares += i
    print(f"la suma de los numeros impares desde 1 hasta {numero} es: {suma_impares}")
