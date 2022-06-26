n = int(input("Cuántos usuarios desea ingresar: "))
usuarios = {}
for i in range(n):
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    usuarios[email] = password
    aux = input("¿Desea continuar(s/n)?: ")
    if aux == "s": continue
    else: break
print("Los usuarios ingresados fueron: \n",usuarios)