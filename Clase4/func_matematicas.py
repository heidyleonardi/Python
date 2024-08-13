def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    if(b == 0):
        return "No se puede dividir por 0"
    else:
        return a/b
def raiz(a,b = 2):
    return a ** 0,5

if __name__ == '__main__':
    print("La suma de 2 y 5 son: ", suma(2,5))
    print("La resta de 10 y 5 son: ", resta(10,5))
    print("La multiplicacion de 3 y 4 son: ", multiplicacion(3,4))
    print("La division entre 10 y 2 es: ", division(10,2))
    print("La raiz de 25 es: ", raiz(25))