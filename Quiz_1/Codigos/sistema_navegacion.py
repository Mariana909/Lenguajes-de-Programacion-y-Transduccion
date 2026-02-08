class Nodo:
    def __init__(self, dato, sig, prev=None):
        self.dato = dato
        self.sig = sig
        self.prev = prev

class ListaDoble:
    def __init__(self, cabeza):
        self.cabeza = cabeza

    def insertar(self, nueva_pag, pag_actual):
        nuevo_nodo = Nodo(nueva_pag, None, pag_actual)
        if pag_actual.sig is not None:
            pag_actual.sig.prev = None 
        pag_actual.sig = nuevo_nodo
        return nuevo_nodo

    def eliminar(self):
        if self.cabeza.sig is None:
            return
        self.cabeza.sig = None

class Navegador:
    def __init__(self, navegador):
        self.pagina_principal = navegador
        self.pag_actual = navegador
        self.historial = ListaDoble(navegador)
    
    def siguiente_pagina(self):
        if self.pag_actual.sig is not None:
            self.pag_actual = self.pag_actual.sig
            return True
        return False
    
    def anterior_pagina(self):
        if self.pag_actual.prev is not None:
            self.pag_actual = self.pag_actual.prev
            return True
        return False
    
    def cargar_pagina(self, nueva_pagina):
        if self.pag_actual is self.pagina_principal:
            self.historial.eliminar()
        
        nuevo_nodo = self.historial.insertar(nueva_pagina, self.pag_actual)
        self.pag_actual = nuevo_nodo

def ejecutar_ejemplos(navegador, url_principales, nodos_principales, url_secundarias):
    print("\n--- Ejecutando ejemplos ---\n")
    
    print(f"Pagina actual: {navegador.pag_actual.dato}")
    
    print(f"\nCargando: {url_secundarias[0][0]}")
    navegador.cargar_pagina(url_secundarias[0][0])
    print(f"Pagina actual: {navegador.pag_actual.dato}")
    
    print(f"\nCargando: {url_secundarias[0][1]}")
    navegador.cargar_pagina(url_secundarias[0][1])
    print(f"Pagina actual: {navegador.pag_actual.dato}")
    
    print("\nRetrocediendo...")
    navegador.anterior_pagina()
    print(f"Pagina actual: {navegador.pag_actual.dato}")
    
    print("\nAvanzando...")
    navegador.siguiente_pagina()
    print(f"Pagina actual: {navegador.pag_actual.dato}")

def modo_interactivo(navegador):
    print("\n--- Modo interactivo ---\n")
    
    while True:
        print(f"\nPagina actual: {navegador.pag_actual.dato}")
        print("\n1. Cargar nueva pagina")
        print("2. Ir a pagina anterior")
        print("3. Ir a pagina siguiente")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            url = input("Ingrese la URL: ")
            navegador.cargar_pagina(url)
        elif opcion == "2":
            if not navegador.anterior_pagina():
                print("No hay pagina anterior")
        elif opcion == "3":
            if not navegador.siguiente_pagina():
                print("No hay pagina siguiente")
        elif opcion == "4":
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    url_principales=["www.google.com","www.youtube.com","www.facebook.com","www.wikipedia.org","www.amazon.com"]
    nodos_principales=[]
    for url in url_principales:
        nodo=Nodo(url,None)
        nodos_principales.append(nodo)
    url_secundarias = [["mail.google.com","maps.google.com","drive.google.com"],
                       ["music.youtube.com","gaming.youtube.com"], 
                       ["messenger.com","instagram.com"],
                       ["wiktionary.org","wikibooks.org"],
                       ["primevideo.com","audible.com"]]
    navegador = Navegador(nodos_principales[0])
    
    print("Simulador de Navegador Web")
    print("=" * 30)
    
    while True:
        print("\nMenu principal:")
        print("1. Ejecutar ejemplos")
        print("2. Modo interactivo")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            ejecutar_ejemplos(navegador, url_principales, nodos_principales, url_secundarias)
        elif opcion == "2":
            modo_interactivo(navegador)
        elif opcion == "3":
            print("\nCerrando navegador...")
            break
        else:
            print("Opcion no valida")
