import random

class Array:
    def __init__(self, maxSize):
        self.__a = [None] * maxSize
        self.nItems = 0

    def insert(self, item):
        if self.nItems < len(self.__a):
            self.__a[self.nItems] = item
            self.nItems += 1
        else:
            print("Error: Array is full.")

    def pop(self):
        if self.nItems > 0:
            self.nItems -= 1
            return self.__a[self.nItems]
        return None

class Stack:
    def __init__(self, maxSize):
        self.array = Array(maxSize)

    def push(self, item):
        self.array.insert(item)

    def pop(self):
        return self.array.pop()

    def is_empty(self):
        return self.array.nItems == 0

class Queue:
    def __init__(self, maxSize):
        self.array = Array(maxSize)
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        self.array.insert(item)

    def dequeue(self):
        if not self.is_empty():
            item = self.array.__a[self.front]
            self.front = (self.front + 1) % len(self.array.__a)
            self.array.nItems -= 1
            return item
        return None

    def is_empty(self):
        return self.array.nItems == 0

def count_and_sum_numbers(container):
    cuentaPar = 0
    cuentaImpar = 0
    sumaPar = 0
    sumaImpar = 0

    while not container.is_empty():
        numberPop = container.pop() if isinstance(container, Stack) else container.dequeue()
        if numberPop is not None:
            if numberPop % 2 == 0:
                cuentaPar += 1
                sumaPar += numberPop
            else:
                cuentaImpar += 1
                sumaImpar += numberPop

    return cuentaPar, sumaPar, cuentaImpar, sumaImpar

def main():
    maxSize = 100  # Tamaño máximo
    print("Elija una opción:")
    print("1. Pila (Stack)")
    print("2. Cola (Queue)")
    
    option = input("Ingrese 1 o 2: ")
    
    if option == '1':
        container = Stack(maxSize)
        print("Seleccionaste Pila (Stack).")
    elif option == '2':
        container = Queue(maxSize)
        print("Seleccionaste Cola (Queue).")
    else:
        print("Opción no válida.")
        return

    # Insertar números aleatorios entre 0 y 100 en la estructura seleccionada
    for _ in range(maxSize):
        random_number = random.randint(0, 100)  # Generar un número aleatorio entre 0 y 100
        if isinstance(container, Stack):
            container.push(random_number)
        else:
            container.enqueue(random_number)

    # Contar y sumar números pares e impares
    cuentaPar, sumaPar, cuentaImpar, sumaImpar = count_and_sum_numbers(container)

    print("La cuenta de números impares es: %s y su suma es: %s" % (cuentaImpar, sumaImpar))
    print("La cuenta de números pares es: %s y su suma es: %s" % (cuentaPar, sumaPar))

if __name__ == "__main__":
    main()