def eliminar_duplicados(arreglo):

  conjunto = set(arreglo)
  lista_unica = list(conjunto)

  return lista_unica

mi_arreglo = [1, 2, 3, 2, 1, 5, 6, 6]
resultado = eliminar_duplicados(mi_arreglo)
print(resultado)  