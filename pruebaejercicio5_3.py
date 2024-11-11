from ejercicio5_3 import Deque
dq = Deque()

# Insertar elementos
dq.insertLeft(10)
dq.insertRight(20)
dq.insertLeft(5)
dq.insertRight(25)

# Imprimir la deque
print(dq)  # Salida esperada: 5 <-> 10 <-> 20 <-> 25

# Ver el primer y último elemento
print(dq.peekLeft())  # Salida esperada: 5
print(dq.peekRight())  # Salida esperada: 25

# Eliminar elementos
print(dq.removeLeft())  # Salida esperada: 5
print(dq.removeRight())  # Salida esperada: 25

# Imprimir la deque después de eliminar
print(dq)  # Salida esperada: 10 <-> 20

# Verificar si la deque está vacía
print(dq.isEmpty())  # Salida esperada: False

# Obtener el tamaño de la deque
print(len(dq))  # Salida esperada: 2