# AFD - Autómata Finito Determinista

Programa simple que implementa un Autómata Finito Determinista (AFD) para procesar cadenas binarias.

## Requisitos

- Python 3.x
- Terminal Linux

## Cómo usar

### 1. Navegar a la carpeta del programa

Si los archivos están en la carpeta de Descargas:

```bash
cd Downloads/Implementacion-AFD
```

O si están en otra ubicación:

```bash
cd ruta/a/la/carpeta
```

### 2. Ejecutar el programa

```bash
python AFD.py Entrada.txt
```

o

```bash
python3 AFD.py Entrada.txt
```

### 3. Ver los resultados

El programa procesará cada línea del archivo `Entrada.txt` y mostrará si cada cadena es **ACEPTADA** o **NO ACEPTADA**.

## Modificar los datos de entrada

Para probar con nuevas cadenas binarias:

1. Abre el archivo `Entrada.txt` con cualquier editor de texto:
   ```bash
   nano Entrada.txt
   ```
   o
   ```bash
   gedit Entrada.txt
   ```

2. Escribe las cadenas binarias, una por línea

3. Guarda y cierra el archivo

4. Vuelve a ejecutar el programa

## Estructura de archivos

```
Implementacion-AFD/
├── AFD.py          # Programa principal
├── Entrada.txt     # Archivo con las cadenas de entrada
└── README.md       # Este archivo
```

## Ejemplo de uso

```bash
$ cd Downloads/Implementacion-AFD
$ python AFD.py Entrada.txt
ACEPTADO
NO ACEPTADO
ACEPTADO
ACEPTADO
NO ACEPTADO
NO ACEPTADO
ACEPTADO
NO ACEPTADO
ACEPTADO
NO ACEPTADO
```

## Cómo funciona la máquina de estados

El AFD está definido mediante un diccionario de transiciones en Python:

```python
trans = {
    'q1': {'0': 'q2', '1': 'q3'},
    'q2': {'0': 'q2', '1': 'q2'},
    'q3': {'0': 'q3', '1': 'q3'}
}
```

### Explicación de las transiciones:

- **Estado q1 (inicial):**
  - Si lee `0` → transiciona a **q2**
  - Si lee `1` → transiciona a **q3**

- **Estado q2 (aceptación):**
  - Si lee `0` → permanece en **q2**
  - Si lee `1` → permanece en **q2**

- **Estado q3 (rechazo):**
  - Si lee `0` → permanece en **q3**
  - Si lee `1` → permanece en **q3**

### Diagrama de estados:

```
       0        ┌───┐
    ┌────────→  │q2 │  (ACEPTA)
    │           └─┬─┘
    │             │ 0,1 (loop)
┌───┴───┐         ↓
│  q1   │       ┌───┐
│(inicio)│      │q2 │
└───┬───┘       └───┘
    │
    │ 1         ┌───┐
    └────────→  │q3 │  (RECHAZA)
                └─┬─┘
                  │ 0,1 (loop)
                  ↓
                ┌───┐
                │q3 │
                └───┘
```

### Lógica del autómata:

1. Comienza en el estado **q1**
2. Lee el primer símbolo de la cadena
3. Si es `0`, va a **q2** (estado de aceptación) y permanece ahí sin importar qué más lea
4. Si es `1`, va a **q3** (estado de rechazo) y permanece ahí sin importar qué más lea
5. Al final, verifica si está en **q2** (acepta) o no (rechaza)

**En resumen:** El AFD acepta todas las cadenas binarias que **comienzan con 0**.

## Información técnica

- **Estado inicial:** q1
- **Estado de aceptación:** q2
- **Alfabeto:** {0, 1}
- El AFD acepta cadenas que comienzan con `0`
