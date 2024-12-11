def calcular(expresion):
  pila = []
  for token in expresion:
    if isinstance(token, (int, float)):
      pila.append(token)
    else:
      operando2 = pila.pop()
      operando1 = pila.pop()
      if token == '+':
        resultado = operando1 + operando2
      elif token == '-':
        resultado = operando1 - operando2
      elif token == '*':
        resultado = operando1 * operando2
      elif token == '/':
        resultado = operando1 / operando2
      pila.append(resultado)

  return pila.pop()

expresion = [2, 3, '+', 5, '*', 2, '-']
resultado = calcular(expresion)
print(resultado) 