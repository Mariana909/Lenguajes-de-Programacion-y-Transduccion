class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.es_fin_palabra = False
        self.palabra_completa = None

class Trie:
    def __init__(self):
        self.raiz = NodoTrie()
    
    def insertar(self, palabra):
        nodo_actual = self.raiz
        
        for caracter in palabra.lower():
            if caracter not in nodo_actual.hijos:
                nodo_actual.hijos[caracter] = NodoTrie()
            nodo_actual = nodo_actual.hijos[caracter]
        
        if nodo_actual.es_fin_palabra:
            return False
        
        nodo_actual.es_fin_palabra = True
        nodo_actual.palabra_completa = palabra.lower()
        return True
    
    def buscar_prefijo(self, prefijo):
        nodo_actual = self.raiz
        
        for caracter in prefijo.lower():
            if caracter not in nodo_actual.hijos:
                return None
            nodo_actual = nodo_actual.hijos[caracter]
        
        return nodo_actual
    
    def obtener_sugerencias(self, prefijo, max_sugerencias=10):
        nodo_prefijo = self.buscar_prefijo(prefijo)
        
        if nodo_prefijo is None:
            return []
        
        sugerencias = []
        self._recolectar_palabras(nodo_prefijo, sugerencias)
        
        return sugerencias[:max_sugerencias]
    
    def _recolectar_palabras(self, nodo, sugerencias):
        if nodo.es_fin_palabra:
            sugerencias.append(nodo.palabra_completa)
        
        for hijo in nodo.hijos.values():
            self._recolectar_palabras(hijo, sugerencias)
    
    def mostrar_todas_palabras(self):
        palabras = []
        self._recolectar_palabras(self.raiz, palabras)
        return palabras

def ejecutar_ejemplos():
    print("\n--- Ejecutando ejemplos ---\n")
    
    trie = Trie()
    
    palabras = ["casa", "carro", "carta", "cascada", "perro", "persona", "personal", "python", "programar"]
    
    print("Insertando palabras:")
    for palabra in palabras:
        trie.insertar(palabra)
        print(f"  - {palabra}")
    
    print("\n--- Pruebas de autocompletado ---")
    
    prefijos = ["ca", "per", "pro", "py", "x"]
    
    for prefijo in prefijos:
        sugerencias = trie.obtener_sugerencias(prefijo)
        print(f"\nPrefijo '{prefijo}':")
        if sugerencias:
            print(f"  Sugerencias: {sugerencias}")
        else:
            print("  No se encontraron sugerencias")
    
    print("\n--- Intentando agregar palabra duplicada ---")
    if trie.insertar("casa"):
        print("  'casa' agregada")
    else:
        print("  'casa' ya existe en el Trie")

def modo_interactivo():
    print("\n--- Modo interactivo ---\n")
    
    trie = Trie()
    
    while True:
        print("\n1. Agregar palabra")
        print("2. Buscar sugerencias")
        print("3. Mostrar todas las palabras")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            palabra = input("Ingrese la palabra: ")
            if trie.insertar(palabra):
                print(f"Palabra '{palabra}' agregada")
            else:
                print(f"La palabra '{palabra}' ya existe")
        
        elif opcion == "2":
            prefijo = input("Ingrese el prefijo: ")
            max_sugerencias = input("Maximo de sugerencias (Enter para 10): ")
            max_sugerencias = int(max_sugerencias) if max_sugerencias else 10
            
            sugerencias = trie.obtener_sugerencias(prefijo, max_sugerencias)
            
            if sugerencias:
                print(f"\nSugerencias para '{prefijo}':")
                for i, sugerencia in enumerate(sugerencias, 1):
                    print(f"  {i}. {sugerencia}")
            else:
                print("No se encontraron sugerencias")
        
        elif opcion == "3":
            palabras = trie.mostrar_todas_palabras()
            if palabras:
                print("\nPalabras en el Trie:")
                for i, palabra in enumerate(palabras, 1):
                    print(f"  {i}. {palabra}")
            else:
                print("No hay palabras en el Trie")
        
        elif opcion == "4":
            break
        
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    print("Sistema de Autocompletado con Trie")
    print("=" * 40)
    
    while True:
        print("\nMenu principal:")
        print("1. Ejecutar ejemplos")
        print("2. Modo interactivo")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            ejecutar_ejemplos()
        elif opcion == "2":
            modo_interactivo()
        elif opcion == "3":
            print("\nCerrando sistema...")
            break
        else:
            print("Opcion no valida")