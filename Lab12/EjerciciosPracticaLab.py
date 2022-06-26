def long():
    print("Cual desea ingresar")
    print("1. Cadena de texto\n2. Lista")
    option = int(input("Ingrese una opción: "))
    longitud = 0
    if option == 1:
        var = input("Ingrese la cadena: ")
        longitud = len(var)
    if option == 2:
        var1 = input("Ingrese la lista (separe por comas): ")
        list = []
        inicio = 0
        for i in var1:
            if i == ',':
                list.append(var1[inicio:var1.index(i, inicio)])
                inicio = var1.index(i, inicio) + 1
        list.append(var1[inicio])
        longitud = len(list)
    return longitud

aux = long()
print("Su longitud es: ",aux)