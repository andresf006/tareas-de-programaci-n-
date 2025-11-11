corriente = [0.5, 0.8, 1.2, -0.1, 2.5, 3.0, 1.8, 2.2, 0.9, 2.7, 1.0]

# 1️⃣ Filtrar lecturas válidas
corriente_filtrada = []
for i in corriente:
    if i >= 0:
        corriente_filtrada.append(i)

# 2️⃣ Detectar sobrecargas
sobrecargas = []
for i in corriente_filtrada:
    if i > 2:
        sobrecargas.append(i)

# 3️⃣ Contar muestras y sobrecargas
total_muestras = len(corriente_filtrada)
total_sobrecargas = len(sobrecargas)

# 4️⃣ Calcular porcentaje de sobrecarga
porcentaje = (total_sobrecargas / total_muestras) * 100

# 5️⃣ Mostrar resultados y activar alarma
print("Lecturas válidas:", corriente_filtrada)
print("Sobrecargas detectadas:", sobrecargas)
print(f"Porcentaje de tiempo en sobrecarga: {porcentaje:.2f}%")

if porcentaje > 30:
    print("⚠️ ALARMA: Sobrecarga detectada")
else:
    print("✅ Operación normal")