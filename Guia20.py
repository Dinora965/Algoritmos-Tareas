class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        nuevo_nodo = NodoArbol(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            nodo_actual = self.raiz
            while True:
                if dato < nodo_actual.dato:
                    if nodo_actual.izquierdo is None:
                        nodo_actual.izquierdo = nuevo_nodo
                        break
                    else:
                        nodo_actual = nodo_actual.izquierdo
                else:
                    if nodo_actual.derecho is None:
                        nodo_actual.derecho = nuevo_nodo
                        break
                    else:
                        nodo_actual = nodo_actual.derecho

    def inorder(self, nodo):
        if nodo:
            self.inorder(nodo.izquierdo)
            print(nodo.dato, end=" ")
            self.inorder(nodo.derecho)

    def buscar(self, dato):
        nodo_actual = self.raiz
        while nodo_actual:
            if dato == nodo_actual.dato:
                return True
            elif dato < nodo_actual.dato:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho
        return False

# Ejemplo de uso:
arbol = ArbolBinario()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Recorrido en orden:")
arbol.inorder(arbol.raiz)
print("\n¿Existe el número 40? ", arbol.buscar(40))