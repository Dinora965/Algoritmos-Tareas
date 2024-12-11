def invertir_arreglo(arreglo):
  
  invertido = []
  for i in range(len(arreglo) - 1, -1, -1):
    invertido.append(arreglo[i])

  return invertido

mi_arreglo = [1, 2, 3, 4, 5]
arreglo_invertido = invertir_arreglo(mi_arreglo)
print(arreglo_invertido)  