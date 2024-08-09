#operadores aritméticos
#imprimir la suma de 3+4
print("La suma de 10 + 4 es: ", 3 + 4)

print("El resultado de las siguientes operaciones; 10-4, 10*4, 10/4, 10%4, 10//4, 10**4 son: ", (10 - 4), (10 * 4), (10 / 4), (10 % 4), (10 // 4) , (10 ** 4))

#resolver la ecuación cuadrática 2x-7x+3=0
a = 2
b = -7
c = 3
x1 = ((-b)+(((b ** 2) - 4 * a * c) ** 0.5)) / (2 * a)
x2 = ((-b)-(((b ** 2) - 4 * a * c) ** 0.5)) / (2 * a)
print("X1: ",x1,  "    X2: ", x2)

#operaciones con cadenas de texto
print("SNPP " + "CTFPPJ " + "PROGRAMACIÓN PYTHON")
#print("Aula" + 2102)
print("Aula" + str(2102))

#Operaciones mixtas
print("Tun Chi " * 5)
print("Ja " *(2 ** 3))

#Operadores de Comparación
print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)

#Operaciones con cadena de texto
print("python " > "PYTHON")
print("aaaa " >= "abaa") #ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) #cuenta caracteres

print("python" != "PYTHON")

#operadores lógicos
print(10 > 4 and "Z" > "A")
print(10 > 4 or "Z" > "A")
print(not(10 > 4 and "Z" > "A"))
