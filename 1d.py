#Escribe un programa que pida al usuario que ingrese una letra del alfabeto y determine si es una vocal o una consonante.

letra = input("Ingrese una letra del alfabeto: ")

if letra in ('a','e','i','o','u'):
    print(f"la letra {letra} es una vocal")
else:
    print(f"la letra {letra} es una consonante")