lista = []
calif = -1
while(calif != 0):
    calif = int(input("Ingrese la calificacion"))
    if calif != 0:
        lista.append(calif)

total = 0
for x in range(len(lista)):
    total += lista[x]

promedio = total / len(lista)
print(promedio)
