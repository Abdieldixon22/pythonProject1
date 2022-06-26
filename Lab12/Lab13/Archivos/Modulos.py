def fibonacci(n):
    a,b = 0,1
    lista = []
    while b<n:
        lista.append(b)
        a,b = b,a+b
    return lista


def suma_fibonacci(n):
    suma = 0
    for i in n:
        suma += i
    return suma


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
