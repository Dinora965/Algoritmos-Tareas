def identity(x): return x  # Función identidad como función de prioridad predeterminada

class PriorityQueue:
    def __init__(self, size, pri=identity):
        self.__maxSize = size  # Tamaño máximo de la cola
        self.__que = []        # Cola como lista dinámica
        self.__pri = pri       # Función para obtener la prioridad del elemento
        self.__nItems = 0      # Número de elementos en la cola

    def insert(self, item):
        if self.isFull():
            raise Exception("Queue overflow")
        self.__que.append(item)  # Inserta el elemento al final de la lista
        self.__nItems += 1
        return True

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        # Encontrar el índice del elemento con mayor prioridad
        max_index = 0
        for i in range(1, self.__nItems):
            if self.__pri(self.__que[i]) > self.__pri(self.__que[max_index]):
                max_index = i
        # Extraer el elemento de mayor prioridad
        max_item = self.__que[max_index]
        del self.__que[max_index]
        self.__nItems -= 1
        return max_item

    def peek(self):
        if self.isEmpty():
            return None
        # Encontrar el elemento con mayor prioridad sin eliminarlo
        max_index = 0
        for i in range(1, self.__nItems):
            if self.__pri(self.__que[i]) > self.__pri(self.__que[max_index]):
                max_index = i
        return self.__que[max_index]

    def isEmpty(self):
        return self.__nItems == 0

    def isFull(self):
        return self.__nItems == self.__maxSize

    def __len__(self):
        return self.__nItems

    def __str__(self):
        # Convertir la cola en una cadena, sin ordenar los elementos
        return "[" + ", ".join(str(item) for item in self.__que) + "]"


# Programa de prueba
def test_priority_queue():
    # Definir una función de prioridad donde valores más altos tienen mayor prioridad
    def priority(item):
        return item

    # Crear una cola de prioridad con tamaño máximo de 5
    pq = PriorityQueue(5, priority)
    
    # Insertar elementos en desorden de prioridad
    pq.insert(10)
    pq.insert(5)
    pq.insert(20)
    pq.insert(15)

    print("Cola de prioridad después de inserciones:", pq)

    # Peek: Ver el elemento de mayor prioridad sin eliminarlo
    print("Elemento con mayor prioridad (peek):", pq.peek())

    # Remover elementos de mayor prioridad y mostrar la cola después de cada remoción
    print("Eliminando elemento con mayor prioridad:", pq.remove())
    print("Cola de prioridad después de eliminación:", pq)

    print("Eliminando elemento con mayor prioridad:", pq.remove())
    print("Cola de prioridad después de eliminación:", pq)

    # Insertar otro elemento y mostrar la cola
    pq.insert(30)
    print("Cola de prioridad después de insertar 30:", pq)

    # Comprobaciones de cola vacía y llena
    print("¿La cola está vacía?", pq.isEmpty())
    print("¿La cola está llena?", pq.isFull())

    # Llenar la cola hasta su capacidad máxima
    pq.insert(25)
    pq.insert(40)
    print("Cola de prioridad al estar llena:", pq)
    print("¿La cola está llena?", pq.isFull())

    # Tratar de insertar un elemento cuando la cola está llena (debe lanzar una excepción)
    try:
        pq.insert(50)
    except Exception as e:
        print("Excepción al intentar insertar en una cola llena:", e)

# Ejecutar las pruebas
test_priority_queue()