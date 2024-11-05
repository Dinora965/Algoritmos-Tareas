from SortArray import Array
array = Array(10)

# Insertar seis elementos
array.insert(10)
array.insert(3)
array.insert(15)
array.insert(7)
array.insert(8)
array.insert(5)
array.insert(20)
array.insert(31)
array.insert(50)
array.insert(85)
# Mostrar el arreglo actual

print("Arreglo antes de ordenar:", array)
array.bubbleSortBidireccional()
print("Arreglo después de ordenar:", array)

# Calcular y mostrar la mediana
print("Mediana del arreglo:", array.median())

