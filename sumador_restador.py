class binario:
    def __init__(self, num):
        self.b1 = num%10
        self.b2 = (num//10)%10
        self.b3 = (num//100)%10
        self.b4 = (num//1000)%10
        self.c4 = (num//10000)%10
    def __add__(self, other):
        x1, x2, x3, x4 = self.b1, self.b2, self.b3, self.b4
        y1, y2, y3, y4 = other.b1, other.b2, other.b3, other.b4
        
        s1, s2, s3, s4 = 0, 0, 0, 0
        c1, c2, c3, c4 = 0, 0, 0, 0
        if (not x1 and y1) or (x1 and not y1):
            s1 = 1
        if x1 and y1:
            c1 = 1
        if (not x2 and ((not y2 and c1) or (y2 and not c1))) or (x2 and ((not y2 and not c1) or (y2 and c1))):
            s2 = 1
        if (x2 and y2) or (c1 and ((not x2 and y2) or (x2 and not y2))):
            c2 = 1
        if (not x3 and ((not y3 and c2) or (y3 and not c2))) or (x3 and ((not y3 and not c2) or (y3 and c2))):
            s3 = 1
        if (x3 and y3) or (c2 and ((not x3 and y3) or (x3 and not y3))):
            c3 = 1
        if (not x4 and ((not y4 and c3) or (y4 and not c3))) or (x4 and ((not y4 and not c3) or (y4 and c3))):
            s4 = 1
        if (x4 and y4) or (c3 and ((not x4 and y4) or (x4 and not y4))):
            c4 = 1
        return binario(c4*10000+s4*1000 + s3*100 + s2*10 + s1)
    def __sub__(self, other):
        # Complemento a 1 del sustraendo (crear una copia)
        comp_b1 = 1 - other.b1
        comp_b2 = 1 - other.b2
        comp_b3 = 1 - other.b3
        comp_b4 = 1 - other.b4
        # Crear objeto temporal con el complemento a 1
        other_comp = binario(comp_b4*1000 + comp_b3*100 + comp_b2*10 + comp_b1)
        # Sumar 1 al complemento a 1 (complemento a 2)
        other_comp = other_comp + binario(1)
        # Sumar el minuendo y el resultado anterior
        resultado = self + other_comp
        # Descartar el acarreo final (c4) - solo usar los 4 bits menos significativos
        return binario(resultado.b4*1000 + resultado.b3*100 + resultado.b2*10 + resultado.b1)
    def __gt__(self, other):
        if self.c4 > other.c4:
            return True
        elif self.c4 < other.c4:
            return False
        if self.b4 > other.b4:
            return True
        elif self.b4 < other.b4:
            return False
        if self.b3 > other.b3:
            return True
        elif self.b3 < other.b3:
            return False
        if self.b2 > other.b2:
            return True
        elif self.b2 < other.b2:
            return False
        if self.b1 > other.b1:
            return True
        elif self.b1 < other.b1:
            return False
        return False  # Son iguales
    def __str__(self):
        return f"{self.c4}{self.b4}{self.b3}{self.b2}{self.b1}"
def pruebas():
    print("=== PRUEBAS DE SUMA ===")
    a = binario(1010)
    b = binario(101)
    print(f"Suma de {a} + {b} = {a + b} (Esperado: 1111)")
    a = binario(1100)
    b = binario(11)
    print(f"Suma de {a} + {b} = {a + b} (Esperado: 1111)")
    a = binario(1111)
    b = binario(1)
    print(f"Suma de {a} + {b} = {a + b} (Esperado: 10000)")
    
    print("\n=== PRUEBAS DE RESTA (Casos válidos) ===")
    a = binario(1010)
    b = binario(101)
    print(f"Resta de {a} - {b} = {a - b} (Esperado: 0101)")
    a = binario(1100)
    b = binario(11)
    print(f"Resta de {a} - {b} = {a - b} (Esperado: 1001)")
    a = binario(1000)
    b = binario(1)
    print(f"Resta de {a} - {b} = {a - b} (Esperado: 0111)")
    
    print("\n=== PRUEBAS DE RESTA (Casos límite - números iguales) ===")
    a = binario(1010)
    b = binario(1010)
    print(f"Resta de {a} - {b} = {a - b} (Esperado: 0000)")
    a = binario(1111)
    b = binario(1111)
    print(f"Resta de {a} - {b} = {a - b} (Esperado: 0000)")
    
    print("\n=== PRUEBAS DE RESTA (Casos inválidos - minuendo < sustraendo) ===")
    a = binario(101)
    b = binario(1010)
    print(f"Resta de {a} - {b} = {a - b} (INCORRECTO: minuendo menor que sustraendo)")
    a = binario(11)
    b = binario(1100)
    print(f"Resta de {a} - {b} = {a - b} (INCORRECTO: minuendo menor que sustraendo)")

def menu():
    print("1. Ejecutar pruebas")
    print("2. Modo interactivo")
    print("3. Salir")
    return int(input("Seleccione una opción: "))

def es_binario_valido(num_str):
    """Verifica que el número contenga solo dígitos 0 y 1"""
    for digito in num_str:
        if digito not in ['0', '1']:
            return False
    return True

if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == 1:
            pruebas()
        elif opcion == 2:
            num1_str = input("Ingrese el primer número binario (4 dígitos): ")
            num2_str = input("Ingrese el segundo número binario (4 dígitos): ")
            
            # Validar que sean números binarios válidos
            if not es_binario_valido(num1_str) or not es_binario_valido(num2_str):
                print("\n Error: El número contiene dígitos inválidos. Solo se permiten 0 y 1.")
                print("Por favor, intente de nuevo.\n")
                continue
            
            num1 = int(num1_str)
            num2 = int(num2_str)
            a = binario(num1)
            b = binario(num2)

            # Validar que los números sean de 4 dígitos
            if len(num1_str) > 4 or len(num2_str) > 4:
                print("\n  Error: Ambos números deben ser de 4 dígitos. Por favor, intente de nuevo.\n")
                continue

            print(f"Suma de {a} + {b} = {a + b}")
            
            # Validar que el minuendo sea >= sustraendo para la resta
            # Comparar si son iguales o a > b
            son_iguales = (a.c4 == b.c4 and a.b4 == b.b4 and a.b3 == b.b3 and a.b2 == b.b2 and a.b1 == b.b1)
            if a > b or son_iguales:
                print(f"Resta de {a} - {b} = {a - b}")
            else:
                print("\n  Error: El primer número debe ser mayor o igual al segundo para realizar la resta.")
                print("Por favor, intente de nuevo.\n")
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
