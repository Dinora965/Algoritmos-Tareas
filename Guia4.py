def esta_en_arreglo(arreglo, numero):

  for elemento in arreglo:
    if elemento == numero:
      return True
  return False

mi_arreglo = [1, 2, 3, 5, 8, 13]
numero_a_buscar = 5

if esta_en_arreglo(mi_arreglo, numero_a_buscar):
  print("El número está en el arreglo")
  
else:
  print("El número no está en el arreglo")