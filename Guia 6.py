class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()

    def peek(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items[-1]


pila = Pila()


pila.push(1)
pila.push(2)
pila.push(3)

print(pila.peek()) 
print(pila.pop())  
print(pila.esta_vacia())  