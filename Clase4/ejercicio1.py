numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el siguiente numero: "))

if(numero_1 > numero_2):
    print("{} es mayor que {}". format(numero_1, numero_2))
    if(numero_1 % 2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
elif(numero_1 < numero_2):
    print("{} es mayor que {}". format(numero_2, numero_1))
    if(numero_2 % 2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
else: 
    print("Los numeros ingresados son iguales")