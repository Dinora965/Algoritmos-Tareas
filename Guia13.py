
class ColaCircular:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("La cola está llena")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("La cola está vacía")
            return
        item = self.items[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return item
    
cola = ColaCircular(5)
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
print(cola.dequeue()) 
cola.enqueue(4)
cola.enqueue(5)
cola.enqueue(6)  
print(cola.items)  