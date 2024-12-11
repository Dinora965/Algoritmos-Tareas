class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # ... (los otros métodos que ya habíamos definido)

    def invertir(self):
        """Invierte el orden de los nodos de la lista enlazada."""
        anterior = None
        actual = self.cabeza
        siguiente = None

        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente

        self.cabeza = anterior

# Ejemplo de uso:
mi_lista = ListaEnlazada()
mi_lista.agregar_final(10)
mi_lista.agregar_final(20)
mi_lista.agregar_final(30)

mi_lista.invertir()
# Ahora la lista contiene: 30, 20, 10