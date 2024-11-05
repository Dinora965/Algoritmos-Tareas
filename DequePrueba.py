from DequeD import Deque
deque = Deque(5)

# Inserciones en ambos extremos
deque.insertRight(1)
deque.insertRight(2)
deque.insertLeft(3)
deque.insertLeft(4)

print("Deque después de inserciones:", deque)  # Muestra el contenido actual del deque

# Verificar los extremos
print("Extremo izquierdo:", deque.peekLeft())
print("Extremo derecho:", deque.peekRight())

# Eliminaciones de ambos extremos
print("Eliminar desde la izquierda:", deque.removeLeft())
print("Eliminar desde la derecha:", deque.removeRight())
print("Deque después de eliminaciones:", deque)