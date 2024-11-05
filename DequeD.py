class Deque:
    def __init__(self, max_size):
        self.__deque = [None] * max_size  # Almacenamiento del deque en un arreglo de tamaño fijo
        self.__max_size = max_size  # Tamaño máximo del deque
        self.__left = 0  # Índice para el lado izquierdo
        self.__right = -1  # Índice para el lado derecho
        self.__size = 0  # Contador de elementos en el deque

    def insertLeft(self, item):
        if self.isFull():
            raise Exception("No se puede insertar a la izquierda: el deque está lleno")
        # Mover el índice izquierdo hacia atrás (con wraparound)
        self.__left = (self.__left - 1 + self.__max_size) % self.__max_size
        self.__deque[self.__left] = item
        self.__size += 1

    def insertRight(self, item):
        if self.isFull():
            raise Exception("No se puede insertar a la derecha: el deque está lleno")
        # Mover el índice derecho hacia adelante (con wraparound)
        self.__right = (self.__right + 1) % self.__max_size
        self.__deque[self.__right] = item
        self.__size += 1

    def removeLeft(self):
        if self.isEmpty():
            raise Exception("No se puede eliminar de la izquierda: el deque está vacío")
        item = self.__deque[self.__left]
        self.__deque[self.__left] = None  # Eliminar la referencia del elemento
        self.__left = (self.__left + 1) % self.__max_size  # Mover el índice izquierdo hacia adelante
        self.__size -= 1
        return item

    def removeRight(self):
        if self.isEmpty():
            raise Exception("No se puede eliminar de la derecha: el deque está vacío")
        item = self.__deque[self.__right]
        self.__deque[self.__right] = None  # Eliminar la referencia del elemento
        self.__right = (self.__right - 1 + self.__max_size) % self.__max_size  # Mover el índice derecho hacia atrás
        self.__size -= 1
        return item

    def peekLeft(self):
        if self.isEmpty():
            return None
        return self.__deque[self.__left]

    def peekRight(self):
        if self.isEmpty():
            return None
        return self.__deque[self.__right]

    def isEmpty(self):
        return self.__size == 0

    def isFull(self):
        return self.__size == self.__max_size

    def __len__(self):
        return self.__size

    def __str__(self):
        # Recorrer desde left a right considerando el wraparound
        if self.isEmpty():
            return "[]"
        result = []
        index = self.__left
        for _ in range(self.__size):
            result.append(self.__deque[index])
            index = (index + 1) % self.__max_size
        return str(result)
    
    
    