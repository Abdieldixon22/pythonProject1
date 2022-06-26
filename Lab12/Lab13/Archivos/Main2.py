from Operaciones import *

n = int(input("Ingrese el número de elementos: "))
lista = []
for i in range(n):
    number = int(input("Ingrese un número: "))
    lista.append(number)
print("La suma de sus elementos es: ",funcion_suma(lista))
print("El producto de sus elementos es: ",funcion_prod(lista))