def invertir_cadena_con_pila(cadena):

  pila = []
  for caracter in cadena:
    pila.append(caracter)

  cadena_invertida = ""
  while pila:
    cadena_invertida += pila.pop()

  return cadena_invertida

cadena_original = "Hola, mundo!"
cadena_invertida = invertir_cadena_con_pila(cadena_original)
print(cadena_invertida)  