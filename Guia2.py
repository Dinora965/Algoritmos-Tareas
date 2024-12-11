def encontrar_max_min(arreglo):
  if not arreglo:
    raise ValueError("El arreglo está vacío")

  maximo = arreglo[0]
  minimo = arreglo[0]

  for numero in arreglo[1:]:
    if numero > maximo:
      maximo = numero
    elif numero < minimo:
      minimo = numero

  return maximo, minimo

mi_arreglo = [3, 7, 2, 9, 5]
resultado = encontrar_max_min(mi_arreglo)
print("El valor máximo es:", resultado[0])
print("El valor mínimo es:", resultado[1])