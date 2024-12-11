class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # ... (los otros métodos)

    def altura(self, nodo):


        if nodo is None:
            return 0
        else:
            altura_izquierda = self.altura(nodo.izquierdo)
            altura_derecha = self.altura(nodo.derecho)
            return 1 + max(altura_izquierda, altura_derecha)