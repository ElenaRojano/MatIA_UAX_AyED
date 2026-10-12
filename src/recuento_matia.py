"""
MatIA · programa inicial de recuento
Datos completamente sintéticos para aprendizaje.

Ejecutar desde la raíz del repositorio:
    Windows: py -3 src/recuento_matia.py
    macOS/Linux: python3 src/recuento_matia.py
"""

import csv

RUTA_DATOS = "datos/casos_sinteticos.csv"

# Este es el único valor que cambiará la persona encargada de desarrollo
# durante la primera actividad.
CASO_SELECCIONADO = "coincide"

registros_del_caso = []

# Abrimos el CSV y conservamos solamente las filas del caso seleccionado.
with open(RUTA_DATOS, "r", encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        if fila["caso"] == CASO_SELECCIONADO:
            registros_del_caso.append(fila)

# Si no encontramos el caso, paramos con un mensaje claro.
if len(registros_del_caso) == 0:
    print(f"No se ha encontrado el caso: {CASO_SELECCIONADO}")
    raise SystemExit(1)

# Todas las filas del mismo caso comparten el mismo objetivo y cantidad esperada.
instrumento_objetivo = registros_del_caso[0]["instrumento_objetivo"]
cantidad_esperada = int(registros_del_caso[0]["cantidad_esperada"])

# Contamos solo las filas cuyo instrumento observado coincide con el objetivo.
cantidad_observada = 0

for fila in registros_del_caso:
    if fila["instrumento_observado"] == instrumento_objetivo:
        cantidad_observada = cantidad_observada + 1

print(f"Caso: {CASO_SELECCIONADO}")
print(f"Instrumento objetivo: {instrumento_objetivo}")
print(f"Cantidad esperada: {cantidad_esperada}")
print(f"Cantidad observada: {cantidad_observada}")

if cantidad_observada == cantidad_esperada:
    print("Resultado: COINCIDE")
elif cantidad_observada < cantidad_esperada:
    diferencia = cantidad_esperada - cantidad_observada
    print(f"Resultado: FALTAN {diferencia}")
else:
    diferencia = cantidad_observada - cantidad_esperada
    print(f"Resultado: SOBRAN {diferencia}")
