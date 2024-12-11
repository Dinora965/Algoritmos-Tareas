class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # ... (otros métodos de la lista enlazada)

    def combinar_listas_ordenadas(self, lista1, lista2):
        nueva_lista = ListaEnlazada()
        nodo1 = lista1.cabeza
        nodo2 = lista2.cabeza

        while nodo1 and nodo2:
            if nodo1.dato <= nodo2.dato:
                nueva_lista.agregar_final(nodo1.dato)
                nodo1 = nodo1.siguiente
            else:
                nueva_lista.agregar_final(nodo2.dato)
                nodo2 = nodo2.siguiente

        # Agregar los nodos restantes de la lista que no se haya terminado
        while nodo1:
            nueva_lista.agregar_final(nodo1.dato)
            nodo1 = nodo1.siguiente

        while nodo2:
            nueva_lista.agregar_final(nodo2.dato)
            nodo2 = nodo2.siguiente

        return nueva_lista