class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Agrega un elemento al final de la cola."""
        self.items.append(item)

    def dequeue(self):
        """Elimina y devuelve el elemento al frente de la cola."""
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.items.pop(0)

    def peek(self):
        """Devuelve el elemento al frente de la cola sin eliminarlo."""
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.items[0]

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return self.items == []
cola = Cola()
cola.enqueue(10)
cola.enqueue(5)
cola.enqueue(3)

print(cola.peek())  
print(cola.dequeue())  
print(cola.is_empty())  