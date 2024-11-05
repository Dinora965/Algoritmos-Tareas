# Clase Nodo para la lista enlazada
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

# Clase Pila usando lista enlazada
class Pila:
    def __init__(self):
        self.top = None  # Nodo superior de la pila

    # Método para añadir un elemento a la pila (push)
    def push(self, data):
        nuevo_nodo = Nodo(data)
        nuevo_nodo.next = self.top
        self.top = nuevo_nodo
        print(f"{data} ha sido agregado a la pila.")

    # Método para eliminar un elemento de la pila (pop)
    def pop(self):
        if self.top is None:
            print("La pila está vacía.")
            return None
        data = self.top.data
        self.top = self.top.next
        print(f"{data} ha sido eliminado de la pila.")
        return data

    # Método para ver el elemento en la cima de la pila (peek)
    def peek(self):
        if self.top is None:
            print("La pila está vacía.")
            return None
        return self.top.data

    # Método para verificar si la pila está vacía
    def is_empty(self):
        return self.top is None