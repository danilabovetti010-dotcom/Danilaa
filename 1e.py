#Escribe un programa que pida al usuario que ingrese un número del 1 al 7 y determine a qué día de la semana 
#corresponde (1 es lunes, 2 es martes, etc.). Si el número no está en ese rango, el programa debe mostrar un mensaje de error.

numero = int(input("Ingrese un numero del 1 al 7: "))

if numero == 1:
    print("El numero corresponde a lunes")
elif numero == 2:
    print("El numero corresponde a martes")
elif numero == 3:
    print("El numero corresponde a miercoles")
elif numero == 4:
    print("El numero corresponde a jueves")
elif numero == 5:
    print("El numero corresponde a viernes")
elif numero == 6:
    print("El numero corresponde a sabado")
elif numero == 7:
    print("El numero corresponde a domingo")
else:
    print("El numero no está en el rango valido")