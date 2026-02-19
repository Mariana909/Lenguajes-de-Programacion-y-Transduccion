# Actividad: Flex & Bison - Capítulo 1

## Estructura del repositorio

```
├── ejemplo1.l       # Contador de palabras en Flex
├── ejemplo2.l       # Traductor inglés-americano
├── ejemplo3.l       # Reconocedor de tokens (imprime tokens)
├── ejemplo4.l       # Reconocedor de tokens con valores
├── ejemplo5.y       # Calculadora con Bison (parser)
├── ejemplo6.l       # Scanner para la calculadora (usa ejemplo5.tab.h)
├── ejercicio1.y     # Pregunta 1: calculadora acepta líneas vacías/comentarios
├── ejercicio2.l     # Pregunta 2: scanner de calculadora hex-decimal
├── ejercicio2.y     # Pregunta 2: parser de calculadora hex-decimal
├── ejercicio3.l     # Pregunta 3: scanner con operadores bit a bit
├── ejercicio3.y     # Pregunta 3: parser con operadores bit a bit
├── ejercicio6.c     # Pregunta 6: contador de palabras manual en C
├── entrada.txt      # Archivo de texto de prueba para ejercicio6 y ejemplos
└── entrada3.txt     # Archivo de texto con expresiones para ejercicio3
```

---

## Requisitos

- **Flex** (`flex`)
- **Bison** (`bison`)
- **GCC** (`gcc`)
- Sistema operativo: Linux (probado en Zorin OS)

---

## Compilación y ejecución

### ejemplo1.l — Contador de palabras
```bash
flex ejemplo1.l
gcc lex.yy.c -o ejemplo1 -lfl
./ejemplo1 < entrada.txt
```

### ejemplo2.l — Traductor inglés-americano
```bash
flex ejemplo2.l
gcc lex.yy.c -o ejemplo2 -lfl
./ejemplo2 < entrada.txt
```

### ejemplo3.l — Reconocedor de tokens
```bash
flex ejemplo3.l
gcc lex.yy.c -o ejemplo3 -lfl
./ejemplo3 < entrada.txt
```

### ejemplo4.l — Reconocedor de tokens con valores
```bash
flex ejemplo4.l
gcc lex.yy.c -o ejemplo4 -lfl
./ejemplo4 < entrada.txt
```

### ejemplo5.y + ejemplo6.l — Calculadora completa
```bash
bison -d ejemplo5.y
flex ejemplo6.l
gcc ejemplo5.tab.c lex.yy.c -o ejemplo5 -lfl
./ejemplo5
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

### Ejercicio 2 — Calculadora hexadecimal-decimal (Pregunta 2)
```bash
bison -d ejercicio2.y
flex ejercicio2.l
gcc ejercicio2.tab.c lex.yy.c -o ejercicio2 -lfl
./ejercicio2
```

### Ejercicio 3 — Calculadora con operadores bit a bit (Pregunta 3)
```bash
bison -d ejercicio3.y
flex ejercicio3.l
gcc ejercicio3.tab.c lex.yy.c -o ejercicio3 -lfl

# Opción 1: con archivo de entrada directamente
./ejercicio3 entrada3.txt

# Opción 2: con redireccionamiento
./ejercicio3 < entrada3.txt
```

### Ejercicio 6 — Contador de palabras en C (Pregunta 6)
```bash
gcc ejercicio6.c -o ejercicio6
./ejercicio6 < entrada.txt
```

---

## Notas

- Para los ejemplos y el ejercicio 6 se usa **redireccionamiento** (`< archivo.txt`) ya que leen desde `stdin`.
- El ejercicio 3 permite pasar el archivo directamente como argumento al ejecutable gracias a la variable `yyin` de Flex, por lo que admite ambas formas de entrada.
