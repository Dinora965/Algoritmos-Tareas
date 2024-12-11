def verificar_balance(cadena):
  pila = []
  parejas = {'}': '{', ']': '[', ')': '('}

  for char in cadena:
    if char in '({[':
      pila.append(char)
    elif char in '}])':
      if not pila or pila.pop() != parejas[char]:
        return False
  return not pila

print(verificar_balance("()")) 
print(verificar_balance("(){}[]"))  
print(verificar_balance("{[()]}"))  
print(verificar_balance("([)]"))  
print(verificar_balance("("))  