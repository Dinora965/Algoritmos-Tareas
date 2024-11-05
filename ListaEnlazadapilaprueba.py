from ListaEnlazadapila import Nodo, Pila

pila = Pila()
pila.push(10)
pila.push(20)
pila.push(30)

print("Elemento en la cima de la pila:", pila.peek())

pila.pop()
pila.pop()

print("¿La pila está vacía?", pila.is_empty())