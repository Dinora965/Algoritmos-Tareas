class Array(object):
    def __init__(self, initialSize):                 # Constructor     
        self.__a = [None] * initialSize              # La matriz almacenada como lista
        self.nItems = 0                              # No hay elementos en la matriz inicialmente

    def insert(self, item):                          # Insertar elemento al final
        if self.nItems < len(self.__a):              # Asegurarse de que la matriz no esté llena
            self.__a[self.nItems] = item             # El elemento va al final actual      
            self.nItems += 1                         # Incrementar el número de elementos
        else:
            raise IndexError("Array is full")

    def search(self, item):                          # Buscar entre los elementos actuales
        for j in range(self.nItems):                 # Si se encuentra,
            if self.__a[j] == item:                  # devolver el elemento
                return self.__a[j]
        return None                                  # Si no se encuentra -> None                   

    def delete(self, item):                          # Eliminar la primera ocurrencia         
        for j in range(self.nItems):                 # de un elemento
            if self.__a[j] == item:                  # Elemento encontrado
                # Mover los elementos hacia la izquierda
                for k in range(j, self.nItems - 1):
                    self.__a[k] = self.__a[k + 1]
                self.__a[self.nItems - 1] = None     # Limpiar el último elemento
                self.nItems -= 1                     # Un elemento menos en la matriz
                return True                          # Devolver éxito
        return False                                 # No se encontró el elemento

    def traverse(self, function=print):              # Recorrer todos los elementos
        for j in range(self.nItems):                 # y aplicar una función
            function(self.__a[j])

    def getMaxNum(self):                             # Encontrar el valor numérico más alto
        max_num = None
        for j in range(self.nItems):
            if isinstance(self.__a[j], (int, float)):  # Verificar si el elemento es un número
                if max_num is None or self.__a[j] > max_num:
                    max_num = self.__a[j]
        return max_num

def getAverageNum(self):  # Calcular el promedio de los valores numéricos
    suma = 0
    cuenta= 0
    for j in range(self.nItems):
        if isinstance(self.__a[j], (int, float)):  # Verificar si el elemento es un número
            suma += self.__a[j]
            cuenta += 1
    return suma / cuenta if cuenta > 0 else None  # Evitar división por cero

maxSize = 10  # Tamaño máximo de la matriz

# Caso 1: Matriz con números y cadenas
arr1 = Array(maxSize)
arr1.insert(77)
arr1.insert(99)
arr1.insert("foo")
arr1.insert("bar")
arr1.insert(44)
arr1.insert(55)
arr1.insert(12.34)
arr1.insert(0)
arr1.insert("baz")
arr1.insert(-17)

print("La matriz 1 contiene:", arr1.nItems, "elementos")
arr1.traverse()
print("El número máximo en la matriz 1 es:", arr1.getMaxNum())  # Debe devolver 99

# Caso 2: Matriz sin números
arr2 = Array(maxSize)
arr2.insert("Camisa")
arr2.insert("Libreta")
arr2.insert("Rojo")
arr2.insert("Lapiz")

print("\nLa matriz 2 contiene:", arr2.nItems, "elementos")
arr2.traverse()
print("El número máximo en la matriz 2 es:", arr2.getMaxNum())  # Debe devolver None

# Caso 3: Matriz con solo ceros
arr3 = Array(maxSize)
arr3.insert(0)
arr3.insert(0.0)

print("\nLa matriz 3 contiene:", arr3.nItems, "elementos")
arr3.traverse()
print("El número máximo en la matriz 3 es:", arr3.getMaxNum())  # Debe devolver 0