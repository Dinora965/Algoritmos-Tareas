from collections import deque

class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # ... (otros métodos)

    def recorrer_por_niveles(self):
        """Recorre el árbol binario por niveles."""
        if self.raiz is None:
            return

        cola = deque([self.raiz])

        while cola:
            nodo_actual = cola.popleft()
            print(nodo_actual.dato, end=" ")

            if nodo_actual.izquierdo:
                cola.append(nodo_actual.izquierdo)

            if nodo_actual.derecho:
                cola.append(nodo_actual.derecho)