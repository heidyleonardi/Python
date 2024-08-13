
numero_1 = int(input("Ingrese un primer numero: "))
numero_2 = int(input("Ingrese un segundo numero: "))
print("Los numeros primos entre {} y {} son: ". format(numero_1, numero_2))
for numero in range(numero_1, numero_2 + 1):
    primo = True 
    if numero < 2:
        primo = False
    else: 
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break
    if primo:
        print(numero)