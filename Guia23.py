class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # ... (otros métodos)

    def contar_hojas(self, nodo):
        """Cuenta la cantidad de nodos hoja en el árbol.

        Args:
            nodo: El nodo desde el cual se iniciará el conteo.

        Returns:
            La cantidad de nodos hoja en el subárbol.
        """

        if nodo is None:
            return 0
        elif nodo.izquierdo is None and nodo.derecho is None:
            return 1
        else:
            return self.contar_hojas(nodo.izquierdo) + self.contar_hojas(nodo.derecho)