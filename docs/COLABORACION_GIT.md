# Colaboración Git · sesión inicial de MatIA

## 1. Modelo de trabajo

- Existe un **repositorio docente** con el material de partida.
- Cada grupo crea **un único fork**.
- El fork pertenece a la cuenta de la **persona responsable del repositorio**.
- Los otros dos integrantes son invitados como colaboradores del fork.
- Cada integrante trabaja con su propia cuenta de GitHub y su propia copia local.

La persona responsable coordina el fork y las invitaciones, pero también realizará uno de los tres turnos de aprendizaje.

## 2. Después de clonar NO inicialices nada

`git clone` ya:

- crea la carpeta local;
- descarga los archivos;
- descarga el historial;
- crea la carpeta interna `.git`;
- configura un remoto llamado `origin`.

Por eso, dentro de este clon **no ejecutes**:

```text
git init
git remote add origin ...
```

Comprueba en su lugar:

```bash
# CONSULTA. Muestra el estado de la copia local.
git status

# CONSULTA. Muestra a qué URL apunta origin.
git remote -v

# CONSULTA. Muestra los últimos commits que ya venían con el repositorio.
git log --oneline -5
```

`origin` debe apuntar al fork del grupo.

## 3. Configura la identidad del autor

Hazlo **dentro del clon de MatIA**.

```bash
# MODIFICA configuración local de este repositorio.
# Sustituye el texto por tu nombre real.
git config user.name "Nombre Apellidos"

# MODIFICA configuración local de este repositorio.
# Usa un correo asociado a tu cuenta de GitHub o tu dirección noreply de GitHub.
git config user.email "correo-asociado-a-github"

# CONSULTA la identidad efectiva.
git config --get user.name
git config --get user.email
```

Estos comandos indican quién firma el commit como autor. **No inician sesión en GitHub**.

La autenticación con GitHub es un proceso distinto y será necesaria para publicar (`push`) en un repositorio en el que tengas permiso de escritura.

## 4. Antes de cada turno

Sitúate en la raíz del clon.

```bash
# CONSULTA dónde estás.
pwd

# CONSULTA si tienes modificaciones pendientes.
git status

# DESCARGA e integra los commits remotos solamente si tu rama puede
# avanzar de forma directa. Si no puede, el comando se detiene.
git pull --ff-only

# CONSULTA de nuevo el estado.
git status
```

Continúa solo si entiendes el resultado y no tienes cambios pendientes inesperados.

`git pull --ff-only` reduce el riesgo de crear una fusión accidental, pero **no garantiza por sí solo que nunca vaya a existir un conflicto**.

## 5. Guardar, preparar, registrar y publicar no son lo mismo

1. **Guardar en el editor**: cambia el archivo de tu ordenador.
2. **`git add`**: selecciona cambios para el próximo commit.
3. **`git commit`**: crea una versión en el historial **local**.
4. **`git push`**: envía commits locales al repositorio remoto.

Ejemplo:

```bash
# CONSULTA qué archivos han cambiado.
git status

# CONSULTA el contenido modificado que todavía no está preparado.
git diff

# MODIFICA el área de preparación de Git.
# Sustituye RUTA_DEL_ARCHIVO por el archivo que te corresponde.
git add RUTA_DEL_ARCHIVO

# CONSULTA qué cambios están preparados.
git status
git diff --staged

# MODIFICA el historial LOCAL creando un commit.
git commit -m "Describe de forma breve el cambio"

# CONSULTA el historial local.
git log --oneline -3

# PUBLICA en el remoto los commits que aún no estaban allí.
git push
```

El primer `git push` del alumnado **no crea el proyecto desde cero**. El fork ya contiene los commits docentes; el push añade los primeros commits propios del grupo sobre ese historial.

## 6. Turnos para el 13 de octubre

### Turno 1 · Análisis
Archivo: `datos/casos_sinteticos.csv`

Antes:
```bash
git pull --ff-only
git status
```

Después de editar y guardar:
```bash
git status
git diff
git add datos/casos_sinteticos.csv
git status
git commit -m "Añade caso sintético del grupo"
git push
```

Avisa a los otros dos integrantes cuando GitHub muestre el commit.

### Turno 2 · Desarrollo
Archivo: `src/recuento_matia.py`

Antes:
```bash
git pull --ff-only
git status
```

Después:
```bash
git status
git diff
git add src/recuento_matia.py
git status
git commit -m "Ejecuta el recuento con el caso del grupo"
git push
```

Avisa al tercer integrante.

### Turno 3 · Documentación y comprobación
Archivo: `docs/REGISTRO_SESION.md`

Antes:
```bash
git pull --ff-only
git status
```

Después:
```bash
git status
git diff
git add docs/REGISTRO_SESION.md
git status
git commit -m "Documenta pruebas y decisiones de la sesión"
git push
```

## 7. Si algo no encaja

Detente y pide ayuda si:

- `git push` es rechazado;
- `git pull --ff-only` indica que no puede hacer un avance directo;
- aparecen cambios que no reconoces;
- `origin` no apunta al fork del grupo;
- Git indica que el historial ha divergido.

En esta primera sesión **no** utilices comandos para forzar un push, reescribir historial o descartar trabajo como solución rápida.

## 8. Autenticación

### Windows 11 con Git Bash
La instalación actual de Git for Windows incluye Git Credential Manager. En la primera operación que necesite permisos de escritura, normalmente se abrirá un inicio de sesión en el navegador. Sigue ese proceso con **tu propia cuenta**.

### macOS y Linux
Para HTTPS, GitHub recomienda GitHub CLI o Git Credential Manager para gestionar las credenciales. Si ya tienes SSH configurado correctamente, también puede utilizarse, pero no lo configuraremos durante esta sesión.

### Regla común
- `user.name` y `user.email` no son el inicio de sesión.
- La contraseña de la cuenta de GitHub no se utiliza como contraseña de Git por HTTPS.
- No escribas tokens, contraseñas ni credenciales en archivos del proyecto.
- No publiques secretos en commits.
