from math import(sqrt,pow)
a = int(input("Ingresa a: "))
b = int(input("Ingresa b: "))
c = int(input("Ingrece c: "))
if (pow(b,2)-(4*a*c))>=0:
    x1 = (-b + sqrt(pow(b,2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt(pow(b,2)-(4*a*c)))/(2*a)
    print("Las raices son: ",x1," ",x2)
else:
    print("No tiene solucion")