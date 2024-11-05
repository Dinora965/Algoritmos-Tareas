def bubbleSort(self): # Sort comparing adjacent vals
 for last in range(self.__nItems-1, 0, -1): # and bubble up
    for inner in range(last): # inner loopgoes up to last
        if self.__a[inner] > self.__a[inner+1]: # If itemless
            self.swap(inner, inner+1) # than adjacentitem, swap
            
def bubbleSortBidireccional(self):
    izquierda = 0                      # Inicio de la porción no ordenada
    derecha = self.__nItems - 1        # Fin de la porción no ordenada

    while izquierda < derecha:
        # Recorrido de izquierda a derecha para mover el elemento más grande al final
        for i in range(izquierda, derecha):
            if self.__a[i] > self.__a[i + 1]:  # Comparar elementos adyacentes
                self.swap(i, i + 1)            # Intercambiar si están fuera de orden

        # Después de este recorrido, el elemento más grande está en su posición final, así que movemos 'derecha' hacia adentro
        derecha -= 1

        # Recorrido de derecha a izquierda para mover el elemento más pequeño al inicio
        for i in range(derecha, izquierda, -1):
            if self.__a[i] < self.__a[i - 1]:  # Comparar elementos adyacentes
                self.swap(i, i - 1)            # Intercambiar si están fuera de orden

        # Después de este recorrido, el elemento más pequeño está en su posición final, así que movemos 'izquierda' hacia adentro
        izquierda += 1
        
        
    array = Array(6)
    array.insert(10)
    array.insert(3)
    array.insert(15)
    array.insert(7)
    array.insert(8)
    array.insert(5)

    print("Arreglo antes de ordenar:", array)
    array.bubbleSortBidireccional()
    print("Arreglo después de ordenar:", array)