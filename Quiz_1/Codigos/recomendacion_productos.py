import networkx as nx

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.historial_compras = []
    
    def agregar_compra(self, producto):
        self.historial_compras.append(producto)
    
    def obtener_historial(self):
        return self.historial_compras
    
    def __repr__(self):
        return f"Usuario({self.id}, {self.nombre})"

class SistemaRecomendacion:
    def __init__(self):
        self.grafo = nx.Graph()
        self.usuarios = {}
    
    def registrar_usuario(self, id_usuario, nombre):
        if id_usuario not in self.usuarios:
            self.usuarios[id_usuario] = Usuario(id_usuario, nombre)
            return True
        return False
    
    def agregar_producto(self, producto):
        if producto not in self.grafo:
            self.grafo.add_node(producto)
    
    def registrar_compra(self, id_usuario, producto):
        if id_usuario not in self.usuarios:
            print(f"Error: Usuario {id_usuario} no registrado")
            return False
        
        usuario = self.usuarios[id_usuario]
        self.agregar_producto(producto)
        
        for prod_previo in usuario.obtener_historial():
            if self.grafo.has_edge(prod_previo, producto):
                self.grafo[prod_previo][producto]["weight"] += 1
            else:
                self.grafo.add_edge(prod_previo, producto, weight=1)
        
        usuario.agregar_compra(producto)
        return True
    
    def obtener_recomendaciones(self, id_usuario, max_recomendaciones=5):
        if id_usuario not in self.usuarios:
            return []
        
        usuario = self.usuarios[id_usuario]
        productos_usuario = set(usuario.obtener_historial())
        
        if not productos_usuario:
            return []
        
        candidatos = {}
        
        for producto in productos_usuario:
            for vecino in self.grafo.neighbors(producto):
                if vecino not in productos_usuario:
                    peso = self.grafo[producto][vecino]["weight"]
                    if vecino in candidatos:
                        candidatos[vecino] += peso
                    else:
                        candidatos[vecino] = peso
        
        recomendaciones = sorted(candidatos.items(), key=lambda x: x[1], reverse=True)
        return recomendaciones[:max_recomendaciones]
    
    def mostrar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            print(f"\n{usuario}")
            print(f"Historial de compras: {usuario.obtener_historial()}")
        else:
            print(f"Usuario {id_usuario} no encontrado")
    
    def mostrar_todos_usuarios(self):
        print("\nUsuarios registrados:")
        if self.usuarios:
            for usuario in self.usuarios.values():
                print(f"  - {usuario}: {len(usuario.obtener_historial())} compras")
        else:
            print("  No hay usuarios registrados")
    
    def mostrar_grafo(self):
        print("\nProductos en el sistema:", list(self.grafo.nodes()))
        print("\nRelaciones (producto1, producto2, peso):")
        if self.grafo.edges():
            for u, v, data in self.grafo.edges(data=True):
                print(f"  ({u}, {v}): {data['weight']} usuarios")
        else:
            print("  No hay relaciones aun")
    
    def obtener_peso_relacion(self, prod1, prod2):
        if self.grafo.has_edge(prod1, prod2):
            return self.grafo[prod1][prod2]["weight"]
        return 0

def ejecutar_ejemplos(sistema):
    print("\n--- Ejecutando ejemplos ---\n")
    
    sistema.registrar_usuario("u1", "Juan")
    sistema.registrar_usuario("u2", "Maria")
    sistema.registrar_usuario("u3", "Carlos")
    
    print("Usuarios registrados: Juan, Maria, Carlos")
    
    print("\n--- Compras de Juan ---")
    sistema.registrar_compra("u1", "a")
    print("Juan compra: a")
    
    sistema.registrar_compra("u1", "c")
    print("Juan compra: c")
    print(f"Peso (a,c): {sistema.obtener_peso_relacion('a', 'c')}")
    
    sistema.registrar_compra("u1", "d")
    print("Juan compra: d")
    print(f"Peso (a,d): {sistema.obtener_peso_relacion('a', 'd')}")
    print(f"Peso (c,d): {sistema.obtener_peso_relacion('c', 'd')}")
    
    print("\n--- Compras de Maria ---")
    sistema.registrar_compra("u2", "a")
    print("Maria compra: a")
    
    sistema.registrar_compra("u2", "b")
    print("Maria compra: b")
    print(f"Peso (a,b): {sistema.obtener_peso_relacion('a', 'b')}")
    
    sistema.mostrar_grafo()
    
    print("\n--- Recomendaciones para Maria ---")
    recomendaciones = sistema.obtener_recomendaciones("u2")
    if recomendaciones:
        print("Productos recomendados:")
        for i, (producto, peso) in enumerate(recomendaciones, 1):
            print(f"  {i}. Producto {producto} (peso acumulado: {peso})")
    else:
        print("No hay recomendaciones disponibles")
    
    print("\n--- Compras de Carlos ---")
    sistema.registrar_compra("u3", "b")
    sistema.registrar_compra("u3", "c")
    sistema.registrar_compra("u3", "d")
    print("Carlos compra: b, c, d")
    
    sistema.mostrar_grafo()
    
    print("\n--- Recomendaciones actualizadas para Maria ---")
    recomendaciones = sistema.obtener_recomendaciones("u2")
    if recomendaciones:
        print("Productos recomendados:")
        for i, (producto, peso) in enumerate(recomendaciones, 1):
            print(f"  {i}. Producto {producto} (peso acumulado: {peso})")

def modo_interactivo(sistema):
    print("\n--- Modo interactivo ---\n")
    
    while True:
        print("\n1. Registrar usuario")
        print("2. Registrar compra")
        print("3. Ver recomendaciones")
        print("4. Mostrar usuario")
        print("5. Mostrar todos los usuarios")
        print("6. Mostrar grafo de productos")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            id_usuario = input("Ingrese ID del usuario: ")
            nombre = input("Ingrese nombre del usuario: ")
            if sistema.registrar_usuario(id_usuario, nombre):
                print(f"Usuario {nombre} registrado exitosamente")
            else:
                print("El usuario ya existe")
        
        elif opcion == "2":
            id_usuario = input("Ingrese ID del usuario: ")
            producto = input("Ingrese nombre del producto: ")
            if sistema.registrar_compra(id_usuario, producto):
                print(f"Compra registrada: {producto}")
        
        elif opcion == "3":
            id_usuario = input("Ingrese ID del usuario: ")
            recomendaciones = sistema.obtener_recomendaciones(id_usuario)
            if recomendaciones:
                print("\nProductos recomendados:")
                for i, (producto, peso) in enumerate(recomendaciones, 1):
                    print(f"  {i}. {producto} (peso: {peso})")
            else:
                print("No hay recomendaciones disponibles")
        
        elif opcion == "4":
            id_usuario = input("Ingrese ID del usuario: ")
            sistema.mostrar_usuario(id_usuario)
        
        elif opcion == "5":
            sistema.mostrar_todos_usuarios()
        
        elif opcion == "6":
            sistema.mostrar_grafo()
        
        elif opcion == "7":
            break
        
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    sistema = SistemaRecomendacion()
    
    print("Sistema de Recomendacion de Productos")
    print("=" * 40)
    
    while True:
        print("\nMenu principal:")
        print("1. Ejecutar ejemplos")
        print("2. Modo interactivo")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            ejecutar_ejemplos(sistema)
        elif opcion == "2":
            modo_interactivo(sistema)
        elif opcion == "3":
            print("\nCerrando sistema...")
            break
        else:
            print("Opcion no valida")
