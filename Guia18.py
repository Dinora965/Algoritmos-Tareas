class ListaEnlazada:
    # ... (los otros métodos)

    def eliminar_duplicados(self):
        """Elimina los nodos con valores duplicados de la lista."""
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            while siguiente and siguiente.dato == actual.dato:
                siguiente = siguiente.siguiente
            actual.siguiente = siguiente
            actual = siguiente

# Ejemplo de uso:
mi_lista = ListaEnlazada()
mi_lista.agregar_final(10)
mi_lista.agregar_final(20)
mi_lista.agregar_final(20)
mi_lista.agregar_final(30)
mi_lista.agregar_final(30)

mi_lista.eliminar_duplicados()
# Ahora la lista contiene: 10, 20, 30