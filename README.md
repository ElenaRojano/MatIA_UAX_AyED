# MatIA · repositorio inicial
**Algoritmos y Estructuras de Datos · Grado en Computación e Inteligencia Artificial · UAX Mare Nostrum · curso 2026–2027**

## 1. Qué es este repositorio

Este repositorio contiene el punto de partida del proyecto **MatIA** para la asignatura.

Durante el proyecto trabajaremos con **datos completamente sintéticos e inventados para aprendizaje**. El objetivo técnico será construir progresivamente herramientas sencillas que permitan:

1. leer y revisar registros de instrumental;
2. contar unidades observadas;
3. comparar cantidades esperadas y observadas;
4. detectar discrepancias;
5. organizar incidencias y revisiones;
6. justificar las estructuras de datos y los algoritmos utilizados.

En la primera sesión **no** se desarrolla todavía la herramienta completa. El objetivo es aprender a trabajar con el repositorio, ejecutar un programa pequeño y publicar cambios de forma ordenada.

> El prototipo es docente. Los datos no representan actividad clínica real y el programa no está validado para uso sanitario, asistencial ni profesional.

## 2. Qué haremos el 13 de octubre

Al terminar la sesión, cada integrante del grupo debe haber podido:

- localizar el repositorio docente;
- trabajar sobre **un único fork del grupo**;
- clonar ese fork en su propio ordenador;
- configurar su identidad de autor en Git;
- comprobar el acceso a GitHub;
- ejecutar `src/recuento_matia.py`;
- realizar una modificación pequeña;
- utilizar `git status`, `git add`, `git commit` y `git push`;
- comprobar su cambio en GitHub;
- explicar qué ha hecho y qué resultado esperaba.

No utilizaremos todavía ramas, merges, rebase ni Pull Requests.

## 3. Repositorio docente, fork, clon y remoto

Son conceptos distintos:

- **Repositorio docente**: repositorio original publicado por la docente. Contiene el material de partida.
- **Fork del grupo**: copia vinculada al repositorio docente que se crea en GitHub en la cuenta de la **persona responsable del repositorio**. Cada grupo tendrá un solo fork.
- **Clon local**: copia de trabajo que cada integrante descarga en su propio ordenador.
- **Remoto `origin`**: dirección de GitHub asociada al clon. Después de clonar el fork, `origin` debe apuntar al **fork del grupo**, no al repositorio docente.

La persona responsable del repositorio coordina la creación del fork y las invitaciones. No implica mayor capacidad, importancia ni responsabilidad académica que el resto: también debe realizar una tarea de aprendizaje y comprender el código.

## 4. Estructura

```text
.
├── README.md
├── .gitignore
├── src/
│   └── recuento_matia.py
├── datos/
│   ├── README.md
│   └── casos_sinteticos.csv
└── docs/
    ├── COLABORACION_GIT.md
    └── REGISTRO_SESION.md
```

### Archivos que se modificarán el 13 de octubre

Cada integrante editará inicialmente un archivo diferente:

- **Análisis** → `datos/casos_sinteticos.csv`
- **Desarrollo** → `src/recuento_matia.py`
- **Documentación y comprobación** → `docs/REGISTRO_SESION.md`

`README.md`, `datos/README.md`, `.gitignore` y `docs/COLABORACION_GIT.md` sirven inicialmente como referencia.

Las responsabilidades rotarán en sesiones posteriores. Todos deben ejecutar el programa y comprender el código básico.

## 5. Datos sintéticos

`datos/casos_sinteticos.csv` contiene registros inventados. Cada fila representa **una unidad observada** dentro de un caso.

El programa inicial utiliza ese archivo directamente; no existe una segunda lista de datos escondida dentro del código.

Los tres casos de referencia son:

| Caso | Instrumento objetivo | Esperado | Observado | Resultado |
|---|---|---:|---:|---|
| `coincide` | pinza | 2 | 2 | coincide |
| `faltan` | pinza | 2 | 1 | falta 1 |
| `sobran` | pinza | 2 | 3 | sobra 1 |

La descripción exacta de las columnas está en `datos/README.md`.

## 6. Ejecutar el programa

Sitúate siempre en la **raíz del repositorio**, es decir, en la carpeta donde ves `README.md`, `src` y `datos`.

### Windows 11 · Git Bash

Comprueba primero qué comando de Python tienes disponible:

```bash
py -3 --version
python --version
```

Utiliza el que funcione en tu equipo:

```bash
py -3 src/recuento_matia.py
```

o:

```bash
python src/recuento_matia.py
```

### macOS y Linux

```bash
python3 --version
python3 src/recuento_matia.py
```

### Resultado inicial esperado

```text
Caso: coincide
Instrumento objetivo: pinza
Cantidad esperada: 2
Cantidad observada: 2
Resultado: COINCIDE
```

Si el programa no produce ese resultado en el repositorio recién clonado, **no empieces a modificarlo**: comprueba la carpeta desde la que lo ejecutas y pide ayuda.

## 7. Primera actividad del grupo

Trabajaremos por turnos. Antes de cada turno, el integrante correspondiente actualiza su copia con los cambios que ya haya publicado el compañero anterior.

### Turno 1 · Análisis

Edita `datos/casos_sinteticos.csv` y añade al final este caso:

```csv
grupo,G01,tijera,tijera,2
grupo,G02,pinza,tijera,2
grupo,G03,tijera,tijera,2
```

Antes de ejecutar nada, responde:

- ¿qué instrumento se contará?
- ¿cuántas unidades se esperan?
- ¿cuántas deberían observarse?
- ¿qué resultado final esperas?

Resultado razonado: se cuentan **2 tijeras**, se esperan **2** y el resultado debe ser **COINCIDE**.

Después guarda el archivo, prepara el cambio, crea tu commit y publícalo.

### Turno 2 · Desarrollo

Actualiza primero tu copia.

En `src/recuento_matia.py` cambia:

```python
CASO_SELECCIONADO = "coincide"
```

por:

```python
CASO_SELECCIONADO = "grupo"
```

Ejecuta el programa.

Resultado esperado:

```text
Caso: grupo
Instrumento objetivo: tijera
Cantidad esperada: 2
Cantidad observada: 2
Resultado: COINCIDE
```

Explica por qué el registro `G02` no aumenta el contador de tijeras.

Guarda, prepara, crea tu commit y publícalo.

### Turno 3 · Documentación y comprobación

Actualiza primero tu copia y vuelve a ejecutar el programa.

Completa `docs/REGISTRO_SESION.md` con:

- resultado observado;
- una decisión tomada por el grupo;
- una comprobación realizada;
- ayuda de IA utilizada, si la hubo;
- una frase explicando la diferencia entre `git add`, `git commit` y `git push`.

Guarda, prepara, crea tu commit y publícalo.

### Comprobación final

Los tres integrantes hacen una última actualización:

```bash
git pull --ff-only
```

Después ejecutan el programa y comprueban el historial:

```bash
git status
git log --oneline -6
```

El grupo debe poder identificar al menos un commit propio de cada integrante.

## 8. Uso de IA

Se permite utilizar IA para pedir explicaciones, proponer código, revisar errores o ayudar a documentar.

No basta con que el programa se ejecute. Cada integrante debe:

1. registrar para qué utilizó IA;
2. revisar lo que recibió;
3. comprobar el resultado;
4. poder explicar el código o texto que conserva;
5. modificarlo si es necesario.

No se deben incluir contraseñas, tokens, datos personales ni credenciales en prompts, archivos o commits.

## 9. `.gitignore`

El archivo `.gitignore` indica a Git qué archivos locales no interesa incorporar al repositorio, por ejemplo cachés de Python o configuraciones del editor.

`.gitignore` **no borra archivos** y tampoco elimina automáticamente del historial un archivo que ya hubiera sido registrado previamente.

## 10. Siguiente etapa

A partir del 20 de octubre el proyecto avanzará hacia lectura y validación de datos, recuento y reconciliación de cantidades, y gestión de incidencias. Esas funcionalidades todavía no forman parte de este programa inicial.
