from functools import reduce

corriente = [0.5, 0.8, 1.2, -0.1, 2.5, 3.0, 1.8, 2.2, 0.9, 2.7, 1.0]

def es_valida(i):
    return i >= 0

corriente_filtrada = list(filter(es_valida, corriente))

def es_sobrecarga(i):
    return i > 2

sobrecargas = list(filter(es_sobrecarga, corriente_filtrada))

def contar(a, _):
    return a + 1

total_muestras = reduce(contar, corriente_filtrada, 0)
total_sobrecargas = reduce(contar, sobrecargas, 0)

porcentaje = (total_sobrecargas / total_muestras) * 100

def activar_alarma(porcentaje):
    if porcentaje > 30:
        return "⚠️ ALARMA: Sobrecarga detectada"
    else:
        return "✅ Operación normal"

print("Lecturas válidas:", corriente_filtrada)
print("Sobrecargas detectadas:", sobrecargas)
print(f"Porcentaje de tiempo en sobrecarga: {porcentaje:.2f}%")
print(activar_alarma(porcentaje))
