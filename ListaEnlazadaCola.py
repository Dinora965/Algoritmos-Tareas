# Clase Nodo para la lista enlazada
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

# Clase Cola usando lista enlazada
class Cola:
    def __init__(self):
        self.front = self.rear = None  # Nodo frontal y trasero de la cola

    # Método para añadir un elemento a la cola (enqueue)
    def enqueue(self, data):
        nuevo_nodo = Nodo(data)
        if self.rear is None:
            self.front = self.rear = nuevo_nodo
            print(f"{data} ha sido agregado a la cola.")
            return
        self.rear.next = nuevo_nodo
        self.rear = nuevo_nodo
        print(f"{data} ha sido agregado a la cola.")

    # Método para eliminar un elemento de la cola (dequeue)
    def dequeue(self):
        if self.front is None:
            print("La cola está vacía.")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"{data} ha sido eliminado de la cola.")
        return data

    # Método para ver el elemento en el frente de la cola
    def peek(self):
        if self.front is None:
            print("La cola está vacía.")
            return None
        return self.front.data

    # Método para verificar si la cola está vacía
    def is_empty(self):
        return self.front is None