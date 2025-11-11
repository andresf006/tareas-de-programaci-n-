# Función de orden superior
def aplicar_funcion(f, lista):
    return [f(x) for x in lista]

# Funciones normales (no lambda)
def al_cuadrado(x):
    return x ** 2

def al_cubo(x):
    return x ** 3

# Aplicamos las funciones
print(aplicar_funcion(al_cuadrado, [1, 2, 3]))  # [1, 4, 9]
print(aplicar_funcion(al_cubo, [1, 2, 3]))      # [1, 8, 27]