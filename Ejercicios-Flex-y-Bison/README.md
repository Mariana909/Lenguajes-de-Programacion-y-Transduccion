# Actividad: Flex & Bison - Capítulo 1

## Estructura del repositorio

```
├── ejemplo1.l           # Contador de palabras en Flex
├── ejemplo2.l           # Traductor inglés-americano
├── ejemplo3.l           # Reconocedor de tokens (imprime tokens)
├── ejemplo4.l           # Reconocedor de tokens con valores
├── ejemplo5.y           # Calculadora con Bison (parser)
├── ejemplo6.l           # Scanner para la calculadora (usa ejemplo5.tab.h)
├── ejercicio1.y         # Pregunta 1: calculadora acepta líneas vacías/comentarios
├── ejercicio2.l         # Pregunta 2: scanner de calculadora hex-decimal
├── ejercicio2.y         # Pregunta 2: parser de calculadora hex-decimal
├── ejercicio3.l         # Pregunta 3: scanner con operadores bit a bit
├── ejercicio3.y         # Pregunta 3: parser con operadores bit a bit
├── ejercicio6.c         # Pregunta 6: contador de palabras manual en C
├── entrada.txt          # Texto largo de prueba para ejercicio6 y ejemplos
├── entrada3.txt         # Expresiones de prueba para ejercicio3
└── Mejoras-Ejercicio3/  # Versión mejorada del ejercicio 3 (ver sección abajo)
    ├── ejercicio3.l
    └── ejercicio3.y
```

---

## Requisitos

- **Flex** (`flex`)
- **Bison** (`bison`)
- **GCC** (`gcc`)
- Sistema operativo: Linux (probado en Zorin OS)

### Instalación

```bash
sudo apt update
sudo apt install flex bison gcc
```

---

## Compilación y ejecución

### ejemplo1.l — Contador de palabras
```bash
flex ejemplo1.l
gcc lex.yy.c -o ejemplo1 -lfl
./ejemplo1 < entrada.txt
```
Ejemplo de entrada:
```
Hello world
This is a test
```
Ejemplo de salida:
```
       2       6      28
```

---

### ejemplo2.l — Traductor inglés-americano
```bash
flex ejemplo2.l
gcc lex.yy.c -o ejemplo2 -lfl
./ejemplo2
```
Ejemplo de entrada:
```
I love the colour of this flavour
```
Ejemplo de salida:
```
I love the color of this flavor
```

---

### ejemplo3.l — Reconocedor de tokens
```bash
flex ejemplo3.l
gcc lex.yy.c -o ejemplo3 -lfl
./ejemplo3 
```
Ejemplo de entrada:
```
3 + 5
```
Ejemplo de salida:
```
NUMBER 3
PLUS
NUMBER 5
NEWLINE
```

---

### ejemplo4.l — Reconocedor de tokens con valores
```bash
flex ejemplo4.l
gcc lex.yy.c -o ejemplo4 -lfl
./ejemplo4
```
Ejemplo de entrada:
```
3 + 5
```
Ejemplo de salida:
```
258 = 3
259
258 = 5
264
```

---

### ejemplo5.y + ejemplo6.l — Calculadora completa
```bash
bison -d ejemplo5.y
flex ejemplo6.l
gcc ejemplo5.tab.c lex.yy.c -o ejemplo5 -lfl
./ejemplo5
```
Ejemplo de entrada:
```
3 + 5
10 * 2
```
Ejemplo de salida:
```
= 8
= 20
```

---

## Ejercicios

### Ejercicio 1 — Calculadora acepta líneas vacías (Pregunta 1)
```bash
bison -d ejercicio1.y
flex ejemplo6.l
gcc ejercicio1.tab.c lex.yy.c -o ejercicio1 -lfl
./ejercicio1
```
Ejemplo de entrada:
```
3 + 5

10 * 2
```
Ejemplo de salida:
```
= 8
= 20
```
> A diferencia del ejemplo original, la línea vacía no genera error.

---

### Ejercicio 2 — Calculadora hexadecimal-decimal (Pregunta 2)
```bash
bison -d ejercicio2.y
flex ejercicio2.l
gcc ejercicio2.tab.c lex.yy.c -o ejercicio2 -lfl
./ejercicio2
```
Ejemplo de entrada:
```
0xFF + 1
10 + 5
0xAB - 0x0B
```
Ejemplo de salida:
```
= 256 (0x100)
= 15 (0xF)
= 160 (0xA0)
```

---

### Ejercicio 3 — Calculadora con operadores bit a bit (Pregunta 3)
```bash
bison -d ejercicio3.y
flex ejercicio3.l
gcc ejercicio3.tab.c lex.yy.c -o ejercicio3 -lfl
```
Para este ejercicio el archivo puede pasarse **directamente como argumento** o usando redireccionamiento:
```bash
# Opción 1: argumento directo (exclusivo de este ejercicio)
./ejercicio3 entrada3.txt

# Opción 2: redireccionamiento (igual que los demás)
./ejercicio3 < entrada3.txt
```
Ejemplo de entrada:
```
5 & 3
0xFF | 0x0F
~5 & 0xFF
(3 + 4) << 2
|10 - 15|
```
Ejemplo de salida:
```
= 1 (0x1)
= 255 (0xFF)
= 250 (0xFA)
= 28 (0x1C)
= 5 (0x5)
```

---

### Mejoras-Ejercicio3 — Versión extendida del Ejercicio 3

La carpeta `Mejoras-Ejercicio3/` contiene una versión mejorada del ejercicio 3 que procesa correctamente **todas** las entradas de `entrada3.txt`, incluyendo casos que la versión original no manejaba.

#### Mejoras implementadas

- **Resta unaria** (`-5`, `|-5|`): se agregó la regla `SUB term` en el parser para soportar números negativos como operandos.
- **Valor absoluto anidado** (`||expr||`): se resolvió la ambigüedad del token `|` introduciendo tres tokens dedicados en el lexer: `ABS_OPEN`, `ABS_CLOSE` y `OR`. El lexer usa la variable `expect_operand` para determinar en contexto si un `|` abre un valor absoluto, lo cierra, o es un OR lógico.
- **Líneas con texto inválido** (`0b styled: 15 & 6`): se agregó una regla en el lexer para ignorar líneas que comiencen con un número seguido de texto no hexadecimal, en lugar de colapsar con un error de sintaxis.

#### Compilación y ejecución

```bash
cd Mejoras-Ejercicio3
bison -d ejercicio3.y
flex ejercicio3.l
gcc ejercicio3.tab.c lex.yy.c -o ejercicio3 -lfl

# Con archivo como argumento
./ejercicio3 ../entrada3.txt

# Con redireccionamiento
./ejercicio3 < ../entrada3.txt
```

Ejemplo de entradas adicionales que ahora funcionan:
```
|-5|
||10 - 15| + 3|
||5| - |3||
```
Ejemplo de salida:
```
= 5 (0x5)
= 8 (0x8)
= 2 (0x2)
```

---

### Ejercicio 6 — Contador de palabras en C (Pregunta 6)
```bash
gcc ejercicio6.c -o ejercicio6
./ejercicio6 < entrada.txt
```
Ejemplo de entrada:
```
Hello world
This is a test
```
Ejemplo de salida:
```
       2       6      28
```
> Se usa redireccionamiento (`< entrada.txt`) ya que el programa lee desde `stdin`.

#### Comparación de velocidad con ejemplo1 (Flex)

La pregunta 6 pide comparar si la versión en C es más rápida que la versión en Flex. Para medirlo se usa el comando `time` desde la terminal:

```bash
time ./ejercicio6 < entrada.txt
time ./ejemplo1 < entrada.txt
```

La salida de `time` tiene tres valores: **real** es el tiempo total transcurrido (el más relevante), **user** es el tiempo de CPU del proceso y **sys** el tiempo usado por el sistema operativo.

<img width="642" height="338" alt="ejercicio6" src="https://github.com/user-attachments/assets/da01ac11-2e9c-45a1-a243-0f8d66e00149" />


La versión en C suele ser ligeramente más rápida porque evita el overhead de las funciones generadas automáticamente por Flex, aunque en la práctica la diferencia es mínima para archivos pequeños.

---

## Notas

- Todos los programas usan **redireccionamiento** (`< archivo.txt`) para recibir la entrada, excepto el ejercicio 3 que adicionalmente permite pasar el archivo como argumento directo gracias al uso de la variable `yyin` de Flex.
- Los archivos `entrada.txt` y `entrada3.txt` incluidos en el repositorio sirven como entradas de prueba para facilitar la ejecución y toma de capturas.
- La carpeta `Mejoras-Ejercicio3/` es independiente del ejercicio 3 original y puede compilarse y ejecutarse por separado.
