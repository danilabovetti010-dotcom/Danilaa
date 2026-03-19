#Escribe un programa que pida al usuario que ingrese una cadena de texto y luego 
#cuente cuántas veces aparece una letra específica en la cadena.

cadena = input("Ingresa una cadena de texto: ")
letra = input("Ingresa una letra para contar: ")
contador = 0
indice = 0

while indice < len(cadena):
    if cadena[indice] == letra:
        contador += 1
    indice += 1
print(f"La letra '{letra}' aparece {contador} veces en la cadena")