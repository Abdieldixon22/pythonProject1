option = 0
clientes = {}
while option!=6:
    print("1. Registrar clientes\n2. Mostrar clientes\n3. Buscar clientes\n4. Actualizar clientes"
          "\n5. Eliminar clientes\n6. Salir")
    option = int(input("Ingrese una opción: "))
    if option == 1:
        ruc = input("Ingrese su RUC: ")
        if len(ruc) == 11 and (ruc[0]+ruc[1] in ['20','10','15','16','17']):
            name = input("Ingrese el nombre de la empresa: ")
            clientes[ruc] = name
            print("Se registró con éxito al nuevo cliente")
        else:
            print("ESE RUC NO ES VÁLIDO")
            continue
    elif option == 2:
        print(f"La lista consta de {len(clientes)} clientes")
        print(clientes)
    elif option == 3:
        search = input("Ingrese el RUC: ")
        if search in clientes.keys():
            print(f"El RUC {search} le pertenece a la empresa {clientes[search]}")
        else:
            print(f"EL RUC {search} NO FUE ENCONTRADO")
            continue
    elif option == 4:
        clave = input("Ingrese el RUC: ")
        if clave in clientes.keys():
            print("Nombre original: ",clientes[clave])
            new_name = input("Ingrese el nuevo nombre de la empresa: ")
            if len(new_name)>0:
               clientes[clave] = new_name
               print("Se modificó con éxito los datos del cliente")
            else: print("Ingrese un nombre válido")
        else:
            print(f"EL RUC {clave} NO FUE ENCONTRADO")
            continue
    elif option == 5:
        pop = input("Ingrese el RUC: ")
        if pop in clientes.keys():
            name_pop = clientes[pop]
            clientes.pop(pop)
            print(f"La empresa {name_pop} con RUC {pop} fue borrada con éxito")
        else:
            print(f"EL RUC {clave} NO FUE ENCONTRADO")
            continue