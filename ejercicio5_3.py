class Nodo:
    def __init__(self, data=None):
        self.data = data  # Dato del nodo
        self.next = None  # Apunta al siguiente nodo
        self.prev = None  # Apunta al nodo anterior

class Deque:
    def __init__(self):
        self.front = None  # Apunta al inicio de la deque
        self.rear = None   # Apunta al final de la deque
        self.size = 0      # Tamaño de la deque

    def isEmpty(self):
        """Verifica si la deque está vacía."""
        return self.size == 0

    def insertLeft(self, item):
        """Inserta un elemento al principio (izquierda) de la deque."""
        nuevo_nodo = Nodo(item)
        if self.isEmpty():
            self.front = self.rear = nuevo_nodo
        else:
            nuevo_nodo.next = self.front  # Apunta al nodo actual en el frente
            self.front.prev = nuevo_nodo  # Apunta el nodo anterior al nuevo nodo
            self.front = nuevo_nodo       # Mueve el puntero del frente al nuevo nodo
        self.size += 1

    def insertRight(self, item):
        """Inserta un elemento al final (derecha) de la deque."""
        nuevo_nodo = Nodo(item)
        if self.isEmpty():
            self.front = self.rear = nuevo_nodo
        else:
            nuevo_nodo.prev = self.rear  # Apunta al nodo actual en el final
            self.rear.next = nuevo_nodo  # Apunta el nodo siguiente al nuevo nodo
            self.rear = nuevo_nodo       # Mueve el puntero del final al nuevo nodo
        self.size += 1

    def removeLeft(self):
        """Elimina un elemento del principio (izquierda) de la deque."""
        if self.isEmpty():
            raise IndexError("removeLeft desde una deque vacía")
        dato = self.front.data
        if self.front == self.rear:  # Solo hay un elemento en la deque
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return dato

    def removeRight(self):
        """Elimina un elemento del final (derecha) de la deque."""
        if self.isEmpty():
            raise IndexError("removeRight desde una deque vacía")
        dato = self.rear.data
        if self.front == self.rear:  # Solo hay un elemento en la deque
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return dato

    def peekLeft(self):
        """Devuelve el elemento en el principio (izquierda) sin eliminarlo."""
        if self.isEmpty():
            raise IndexError("peekLeft desde una deque vacía")
        return self.front.data

    def peekRight(self):
        """Devuelve el elemento en el final (derecha) sin eliminarlo."""
        if self.isEmpty():
            raise IndexError("peekRight desde una deque vacía")
        return self.rear.data

    def __len__(self):
        """Devuelve el tamaño de la deque."""
        return self.size

    def __str__(self):
        """Devuelve una representación en cadena de la deque."""
        elementos = []
        actual = self.front
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
        return " <-> ".join(elementos)  # Representación de lista enlazada doble