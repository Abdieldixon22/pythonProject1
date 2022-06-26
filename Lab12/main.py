option = 1
productos={}
while option!=3:
      print("Menú de opciones\n======================\n1. Ingresar productos"
            "\n2. Mostrar productos\n3. Salir")
      option = int(input("Ingrese una opciónn: "))
      if option==1:
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            productos[codigo] = nombre
      else:
            print("Código  Nombre")
            for i in productos.items():
                  print(i[0],"  ",i[1])

