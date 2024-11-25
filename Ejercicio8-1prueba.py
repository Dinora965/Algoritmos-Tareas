# Automated tests for the modified BinarySearchTree class

from EjercicioOchoUno import *

# Crear un árbol de búsqueda binario
theTree = BinarySearchTree()
print('Se creó un árbol de búsqueda binario vacío.')

# Claves para insertar
keys = [44, 27, 33, 65, 57, 49, 55, 83, 71, 86, 27]

count = 0
for key in keys:
   print('Insertando la clave', key, 'en el árbol retorna',
         theTree.insertar(key, count))
   count += 1

print('Se creó un árbol de búsqueda binario con', theTree.nodos(),
      'nodos en', theTree.niveles(), 'niveles.')
theTree.imprimir()

# Obtener la raíz del árbol
root_data, root_key = theTree.raiz()
print('El nodo raíz del árbol tiene clave:', root_key, 'y dato:', root_data)

# Buscar claves específicas
dkeys = [keys[i] for i in range(0, len(keys), 3)] + [37, 40]
for key in dkeys:
   print('Buscar la clave', key, 'retorna', theTree.buscar(key))

# Eliminar claves específicas
for key in dkeys:
   print('Eliminar la clave', key, 'retorna', theTree.eliminar(key))

print('El árbol de búsqueda binario ahora contiene',
      theTree.nodos(), 'nodos en', theTree.niveles(), 'niveles.')
theTree.imprimir()

# Obtener el nodo raíz después de las eliminaciones
root_data, root_key = theTree.raiz()
print('El nodo raíz del árbol ahora tiene clave:', root_key, 'y dato:', root_data)

# Obtener el nodo mínimo
min_data, min_key = theTree.nodoMinimo()
print('La clave mínima es', min_key, 'con dato', min_data)

# Obtener el nodo máximo
max_data, max_key = theTree.nodoMaximo()
print('La clave máxima es', max_key, 'con dato', max_data)

# Recorridos en el árbol
print('Prueba de recorrido en orden (in-order) usando la función imprimir:')
theTree.recorrerInOrden()

for func in (theTree.generador_recursivo, theTree.generador):
   print('Usando un generador {}recursivo para recorridos.'.format(
      '' if func == theTree.generador_recursivo else 'no-'))
   for order in ['pre', 'in', 'post']:
      print(' Recorriendo el árbol en orden', order)
      for key, data in func(order):
         print(' {' + str(key) + ', ' + str(data) + '}', end='')
      print()
   print(' Verificando excepción para un tipo de recorrido desconocido:')
   try:
      for item in func('orden inválido'):
         print(' Inesperadamente produjo:', item)
   except ValueError as e:
      print(' Recibido error esperado:', e)

# Árbol con datos aleatorios
from random import *
random_tree = BinarySearchTree()
seed(3.14159)
for key, data in theTree.generador('pre'):
   random_tree.insertar(key, randrange(1000))
print('Árbol con las mismas claves pero con datos aleatorios:')
random_tree.imprimir(indentBy=2)

# Calcular el promedio de los datos y mostrar nodos por debajo del promedio
total, count = 0, 0
for key, data in random_tree.generador('pre'):
   total += data
   count += 1
average = total / count
below_average = []
for key, data in random_tree.generador('in'):
   if data <= average:
      below_average.append((key, data))
print('Elementos del árbol con datos menores o iguales al promedio', average,
      'son:', below_average)

# Comparación con una comprensión de listas
below_average2 = [
   (key, data) for key, data in random_tree.generador('in')
   if data <= average]
print('La comprensión de listas',
      '' if below_average == below_average2 else 'no',
      'coincide.')