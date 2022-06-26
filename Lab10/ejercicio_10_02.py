Estudiantes = {"a1010":"Juarez","a2020":"Gonzalo","a3030":"Pinto","a4040":"Quispe","a5050":"Ponce"}
# 2.1
print(Estudiantes)
for clave,valor in Estudiantes.items(): print(clave,valor)
# 2.2
print(f"Existen {len(Estudiantes)} alumnos")
# 2.3
print("Las claves son: ",Estudiantes.keys())
# 2.4
print("Los valores son: ",Estudiantes.values())
# 2.5
codigo = input("Ingrese una clave: ")
print(Estudiantes.get(codigo,"NO EXISTE"))
# 2.6
print("Ingrese un nuevo valor")
new_key = input("Ingrese su clave: ")
new_value = input("Ingrese su valor: ")
Estudiantes[new_key] = new_value
# 2.7
print(Estudiantes)
# 2.8
print("Ingrese un nuevo valor")
new_key1 = input("Ingrese su clave: ")
new_value1 = input("Ingrese su valor: ")
aux = {new_key1:new_value1}
Estudiantes.update(aux)
print(Estudiantes)
# 2.9
key_pop = input("¿Qué valor desea eliminar? (ingrese su clave): ")
Estudiantes.pop(key_pop)
print(Estudiantes)
# 2.10
copia = Estudiantes.copy()
print(copia)
# 2.11
Estudiantes.clear()
print(Estudiantes)