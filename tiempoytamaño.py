import time
import sys

# Creamos los arreglos
lista = [i for i in range(100000)]
tupla = tuple(i for i in range(100000))
conjunto = {i for i in range(100000)}
diccionario = {i: i for i in range(100000)}

# Solicitamos el tipo de arreglo 
tipo = input("¿Qué arreglo deseas probar? (lista o 1, tupla o 2, conjunto o 3, diccionario o 4): ").strip().lower()

# Solicitamos possición a consultar del dato

poscicion  = int(input("Ingresa la posición que deseas consultar (entre 0 y 99999): "))

print("memoria usada: ")
lista_mb = sys.getsizeof(lista) / (1024 * 1024)
tupla_mb = sys.getsizeof(tupla) / (1024 * 1024)
conjunto_mb = sys.getsizeof(conjunto) / (1024 * 1024)
diccionario_mb = sys.getsizeof(diccionario) / (1024 * 1024)

# mostramos el tamaño que ocupamos en la memoria ram en mb
print(f"{lista_mb:.6f} MB para lista")
print(f"{tupla_mb:.6f} MB para tupla")
print(f"{conjunto_mb:.6f} MB para conjunto")
print(f"{diccionario_mb:.6f} MB para diccionario")

# Verificamos q esté en el rango
if not 0 <= poscicion  < 100000:
    print("El número debe estar entre 0 y 99999.")
    exit()

# buscamos el arreglo seleccionado y calculamos el tiempo de busqueda de la posccicion en el mismo 
if tipo == "lista" or "1":
    tiempo_inicial = time.time()
    resultado = lista[poscicion ]
    tiempo_total = time.time() - tiempo_inicial
    print(f"Acceso a lista en posición {poscicion }: {resultado}")
    print(f"Tiempo: {tiempo_total:.8f} segundos ({tiempo_total * 1000:.3f} ms)")

elif tipo == "tupla":
    tiempo_inicial = time.time()
    resultado = tupla[poscicion ]
    tiempo_total = time.time() - tiempo_inicial
    print(f"Acceso a tupla en posición {poscicion }: {resultado}")
    print(f"Tiempo: {tiempo_total:.8f} segundos ({tiempo_total * 1000:.3f} ms)")

elif tipo == "conjunto":
    tiempo_inicial = time.time()
    encontrado = poscicion  in conjunto
    tiempo_total = time.time() - tiempo_inicial
    print(f"Búsqueda en conjunto del valor {poscicion }: {encontrado}")
    print(f"Tiempo: {tiempo_total:.8f} segundos ({tiempo_total * 1000:.3f} ms)")

elif tipo == "diccionario":
    tiempo_inicial = time.time()
    resultado = diccionario[poscicion ]
    tiempo_total = time.time() - tiempo_inicial
    print(f"Acceso a diccionario con clave {poscicion }: {resultado}")
    print(f"Tiempo: {tiempo_total:.8f} segundos ({tiempo_total * 1000:.3f} ms)")

else:
    print("Opción no válida. Elige entre lista, tupla, conjunto o diccionario.")
