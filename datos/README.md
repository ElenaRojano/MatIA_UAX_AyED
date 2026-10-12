# Datos sintéticos de MatIA

Todos los registros de esta carpeta son **inventados para aprendizaje**.

No proceden de pacientes, intervenciones, centros sanitarios ni sistemas empresariales. No se ha evaluado su representatividad clínica ni la utilidad profesional del prototipo.

## Archivo `casos_sinteticos.csv`

Cada fila representa **una unidad de instrumental observada** en un caso sintético.

| Columna | Tipo | Unidad / formato | Significado |
|---|---|---|---|
| `caso` | texto | identificador | Agrupa los registros que pertenecen al mismo escenario de prueba. |
| `registro_id` | texto | identificador sintético | Distingue una observación de otra dentro del caso. |
| `instrumento_observado` | texto | categoría | Tipo de instrumento registrado en esa fila. |
| `instrumento_objetivo` | texto | categoría | Tipo de instrumento que debe contar el ejercicio. Se repite en las filas del mismo caso para mantener el archivo autocontenido. |
| `cantidad_esperada` | entero | unidades | Número de unidades del instrumento objetivo que se esperan en ese caso. |

### Cómo interpreta el programa una fila

Ejemplo:

```csv
coincide,C01,pinza,pinza,2
```

Significa:

- el registro pertenece al caso `coincide`;
- su identificador sintético es `C01`;
- la unidad observada se ha registrado como `pinza`;
- el instrumento que se quiere contar en ese caso es `pinza`;
- se esperan 2 unidades de ese instrumento en el conjunto del caso.

`cantidad_esperada` se repite en todas las filas de un mismo caso para que cada registro conserve el contexto del escenario. En sesiones posteriores se podrá separar el inventario esperado de las observaciones.

## Casos iniciales

- `coincide`: 2 pinzas esperadas y 2 observadas.
- `faltan`: 2 pinzas esperadas y 1 observada.
- `sobran`: 2 pinzas esperadas y 3 observadas.

Estos tres casos se utilizan para comprobar que el programa diferencia coincidencia, faltantes y sobrantes.
