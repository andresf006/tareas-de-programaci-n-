diccionario_ejm = {1: "ejemplo 1", 2: "ejemplo 2", 3: "ejemplo 3"}
print(diccionario_ejm)

# Guardamos el diccionario en el archivo creado
with open("diccionario.txt", "w") as archivo:
    archivo.write(str(diccionario_ejm))

# Leemos el diccionario desde el archivo
diccionario_leido = eval(open("diccionario.txt", "r").read())

# Pedimos una llave al usuario y buscamos si ya esta
llave = int(input("Ingresa la llave que quieres buscar: "))

if llave in diccionario_leido:
    print("El valor es:", diccionario_leido[llave]) #analiza si el valor existe si no guarda la llave si si, imprime "esa llave no existe en el diccionario"
else:
    print("llave no existente en el diccionario.") 


nueva_llave = int(input("Ingrese una nueva llave (un numero): ")) #Se pide una nueva llave y le damos un valor
nuevo_valor = input("Ingrese el valor para esa llave: ")

diccionario_leido[nueva_llave] = nuevo_valor #Agregamos la nueva llave y valor al diccionario. [] Permite agregar o modificar elementos en un diccionario accediendo asu llave
# y dandole el valor que queremos


with open("diccionario.txt", "w") as archivo: #En el archivo se guarda el nuevo diccionario actualizado
    archivo.write(str(diccionario_leido))

print("Diccionario actualizado:")
print(diccionario_leido)
with open("diccionario.txt", "w") as archivo:#gpt
    archivo.write(str(diccionario_leido))


# 🔽 Mostrar el contenido del archivo actualizado
print("\nContenido del archivo 'diccionario.txt':")#gpt
with open("diccionario.txt", "r") as archivo:#gpt
    print(archivo.read())#gpt
