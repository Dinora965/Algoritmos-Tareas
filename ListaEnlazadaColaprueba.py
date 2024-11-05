from ListaEnlazadaCola import Nodo,Cola
cola = Cola()
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)

print("Elemento en el frente de la cola:", cola.peek())

cola.dequeue()
cola.dequeue()

print("¿La cola está vacía?", cola.is_empty())