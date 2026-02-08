# Calculadora Binaria - Sumador y Restador

## ¿Qué es este programa?

Este es un programa que te permite **sumar y restar números binarios**. 

### ¿Qué son los números binarios?

Los números binarios son números que solo usan dos dígitos: **0** y **1**. Son la forma en que las computadoras "piensan" internamente. Por ejemplo:
- El número binario `1010` equivale al número 10 en decimal (el sistema que usamos normalmente)
- El número binario `101` equivale al número 5 en decimal
- El número binario `1111` equivale al número 15 en decimal

Este programa trabaja con números binarios de **4 dígitos** (también puede manejar hasta 5 dígitos en algunos casos).

---

## ¿Qué necesitas para usar este programa?

### Requisitos:
1. **Ubuntu** (o cualquier sistema Linux)
2. **Python 3** instalado (Ubuntu generalmente lo trae instalado)
3. El archivo `sumador_restador.py`

---

## Cómo ejecutar el programa

### Paso 1: Abrir la Terminal

1. Presiona las teclas **Ctrl + Alt + T** al mismo tiempo
2. Se abrirá una ventana negra con texto blanco (esta es la Terminal)

### Paso 2: Navegar a la carpeta donde está el archivo

Si guardaste el archivo en tu carpeta de Descargas, escribe:

```bash
cd ~/Descargas
```

Si está en otro lugar, cambia `Descargas` por el nombre de la carpeta correcta. Por ejemplo:
- Para Documentos: `cd ~/Documentos`
- Para Escritorio: `cd ~/Escritorio`

### Paso 3: Ejecutar el programa

Escribe el siguiente comando y presiona Enter:

```bash
python3 sumador_restador.py
```

---

## Cómo usar el programa

Una vez que ejecutes el programa, verás un **menú con 3 opciones**:

```
1. Ejecutar pruebas
2. Modo interactivo
3. Salir
Seleccione una opción:
```

### Opción 1: Ejecutar pruebas

Esta opción ejecuta ejemplos automáticos para que veas cómo funciona el programa. Mostrará:
- Ejemplos de **sumas** de números binarios
- Ejemplos de **restas** válidas
- Ejemplos de restas con números iguales
- Ejemplos de restas inválidas (cuando intentas restar un número mayor de uno menor)

Solo presiona `1` y luego Enter para verlo en acción.

### Opción 2: Modo interactivo

Esta opción te permite **ingresar tus propios números binarios** para sumarlos y restarlos.

**Instrucciones:**
1. Presiona `2` y luego Enter
2. El programa te pedirá el primer número binario (escríbelo usando solo 0s y 1s)
3. Luego te pedirá el segundo número binario
4. El programa mostrará:
   - El resultado de la **suma**
   - El resultado de la **resta** (solo si el primer número es mayor o igual al segundo)

**Ejemplo de uso:**

```
Ingrese el primer número binario (4 dígitos): 1010
Ingrese el segundo número binario (4 dígitos): 101
Suma de 01010 + 00101 = 01111
Resta de 01010 - 00101 = 00101
```

### Opción 3: Salir

Presiona `3` y luego Enter para cerrar el programa.

---

## Reglas importantes

### 1. Solo números de 4 dígitos
- Correcto: `1010`, `0101`, `1111`, `0001`
- Incorrecto: `10101` (5 dígitos), `10` (2 dígitos)

### 2. Solo usa 0 y 1
- Correcto: `1010`, `0101`
- Incorrecto: `1234`, `abcd`

### 3. Para restar, el primer número debe ser mayor o igual al segundo
- Correcto: `1010 - 0101` (10 - 5 = 5 en decimal)
- Incorrecto: `0101 - 1010` (5 - 10 = negativo, no permitido)

---

## Ejemplos prácticos

### Ejemplo 1: Suma básica
```
Primer número: 1010  (10 en decimal)
Segundo número: 0101  (5 en decimal)
Resultado: 01111  (15 en decimal)
```

### Ejemplo 2: Suma con acarreo
```
Primer número: 1111  (15 en decimal)
Segundo número: 0001  (1 en decimal)
Resultado: 10000  (16 en decimal - ¡nota el quinto dígito!)
```

### Ejemplo 3: Resta básica
```
Primer número: 1100  (12 en decimal)
Segundo número: 0011  (3 en decimal)
Resultado: 1001  (9 en decimal)
```

### Ejemplo 4: Resta que da cero
```
Primer número: 1010  (10 en decimal)
Segundo número: 1010  (10 en decimal)
Resultado: 0000  (0 en decimal)
```

---

## Solución de problemas

### Problema: "python3: command not found"
**Solución:** Necesitas instalar Python 3. Ejecuta:
```bash
sudo apt update
sudo apt install python3
```

### Problema: "No such file or directory"
**Solución:** Estás en la carpeta equivocada. Asegúrate de estar en la carpeta donde guardaste el archivo usando el comando `cd`.

### Problema: El programa no hace nada al presionar Enter
**Solución:** Verifica que hayas escrito solo números (1, 2 o 3) cuando el programa te pida una opción.

### Problema: "Error: Ambos números deben ser de 4 dígitos"
**Solución:** Asegúrate de escribir exactamente 4 dígitos. Si tu número es más corto, añade ceros al inicio:
- En lugar de `101`, escribe `0101`
- En lugar de `1`, escribe `0001`

---

## ¿Cómo funciona internamente? (explicación simple)

El programa simula cómo funcionan los circuitos digitales dentro de una computadora:

1. **Suma:** El programa suma bit por bit (dígito por dígito) de derecha a izquierda, llevando el "acarreo" cuando 1+1=10 (en binario)

2. **Resta:** Usa el método del "complemento a 2", que es la técnica que usan las computadoras reales para restar:
   - Invierte todos los bits del número a restar (complemento a 1)
   - Le suma 1 al resultado
   - Suma este resultado al primer número
   - Descarta el bit extra que sobra

---

## Información técnica

- **Lenguaje:** Python 3
- **Tipo:** Programa de línea de comandos (Terminal)
- **Funcionalidad:** Suma y resta de números binarios de 4 bits usando lógica booleana
- **Método de resta:** Complemento a 2

---

## Notas finales

Este programa es **educativo** y está diseñado para:
- Entender cómo funcionan las operaciones binarias
- Aprender sobre aritmética digital
- Ver cómo las computadoras realizan cálculos básicos

¡Diviértete explorando el mundo binario!

---

## ¿Necesitas ayuda?

Si tienes problemas ejecutando el programa:
1. Verifica que estés en la carpeta correcta usando el comando `pwd` (muestra tu ubicación actual)
2. Verifica que el archivo exista usando el comando `ls` (lista los archivos en la carpeta)
3. Asegúrate de tener permisos para ejecutar el archivo

Para dar permisos de ejecución (si es necesario):
```bash
chmod +x sumador_restador.py
```
