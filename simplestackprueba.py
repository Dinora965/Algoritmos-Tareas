from SimpleStack import Stack

# Programa de prueba
try:
    stack = Stack(3)  # Crear una pila con un tamaño máximo de 3
    print("Agregando elementos a la pila:")
    stack.push(10)
    print(stack)
    stack.push(20)
    print(stack)
    stack.push(30)
    print(stack)

    # Intentar agregar otro elemento, debería lanzar una excepción
    print("Intentando agregar otro elemento a una pila llena:")
    stack.push(40)  # Esto debería lanzar una excepción
except Exception as e:
    print("Excepción:", e)

try:
    print("\nExtrayendo elementos de la pila:")
    print("Elemento extraído:", stack.pop())
    print(stack)
    print("Elemento extraído:", stack.pop())
    print(stack)
    print("Elemento extraído:", stack.pop())
    print(stack)

    # Intentar extraer otro elemento, debería lanzar una excepción
    print("Intentando extraer un elemento de una pila vacía:")
    stack.pop()  # Esto debería lanzar una excepción
except Exception as e:
    print("Excepción:", e)