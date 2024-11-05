# SimpleStack.py
# Implementar una estructura de datos de Pila utilizando una lista de Python
class Stack(object):
    def __init__(self, max):  # Constructor
        self.__stackList = [None] * max  # La pila almacenada como una lista
        self.__top = -1  # Sin elementos inicialmente
        self.__max = max  # Tamaño máximo de la pila

    def push(self, item):  # Insertar elemento en la parte superior de la pila
        if self.isFull():
            raise Exception("No se puede empujar: La pila está llena")
        self.__top += 1  # Avanzar el puntero
        self.__stackList[self.__top] = item  # Almacenar el elemento

    def pop(self):  # Eliminar el elemento superior de la pila
        if self.isEmpty():
            raise Exception("No se puede extraer: La pila está vacía")
        top = self.__stackList[self.__top]  # Elemento superior
        self.__stackList[self.__top] = None  # Eliminar la referencia del elemento
        self.__top -= 1  # Disminuir el puntero
        return top  # Retornar el elemento superior

    def peek(self):  # Retornar el elemento superior
        if not self.isEmpty():  # Si la pila no está vacía
            return self.__stackList[self.__top]  # Retornar el elemento superior
        else:
            return None

    def isEmpty(self):  # Verificar si la pila está vacía
        return self.__top < 0

    def isFull(self):  # Verificar si la pila está llena
        return self.__top >= self.__max - 1

    def __len__(self):  # Retornar el número de elementos en la pila
        return self.__top + 1

    def __str__(self):  # Convertir la pila a cadena
        ans = "["  # Comenzar con corchete izquierdo
        for i in range(self.__top + 1):  # Recorrer los elementos actuales
            if len(ans) > 1:  # Excepto junto al corchete izquierdo,
                ans += ", "  # separar elementos con una coma
            ans += str(self.__stackList[i])  # Agregar la forma en cadena del elemento
        ans += "]"  # Cerrar con corchete derecho
        return ans