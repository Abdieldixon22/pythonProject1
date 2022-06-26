
def linea():
    longitud = int(input("Ingrese la longitud: "))
    car_der = input("Ingrese el caracter derecho: ")
    car_iz = input("Ingrese el caracter izquierdo: ")
    car_centro = input("Ingrese el caracter central: ")
    for i in range(longitud):
        if i==0:
            print(car_iz,end='')
        elif i==longitud-1:
            print(car_der,end='')
        else:
            print(car_centro,end='')
linea()
