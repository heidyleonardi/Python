#imprimir todos los numeros pares que existen entre dos numeros leídos por teclado usando bucles for
numero_1 = int(input("Ingrese un primer numero: "))
numero_2 = int(input("Ingrese un segundo numero: "))
print("Los numeros pares entre {numero_1} y {numero_2} son: ")
for numero in range(numero_1, numero_2 + 1):
    if numero % 2 == 0:
        print(numero)