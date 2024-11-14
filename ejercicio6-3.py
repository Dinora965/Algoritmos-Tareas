def power(x, y):
    # Caso base 1: cualquier número elevado a la potencia 0 es 1.
    if y == 0:
        return 1
    # Caso base 2: cualquier número elevado a la potencia 1 es el mismo número.
    elif y == 1:
        return x
    # Caso de recursión para exponentes positivos.
    elif y > 1:
        return x * power(x, y - 1)
    # Caso de recursión para exponentes negativos.
    else:
        return 1 / power(x, -y)

# Programa de prueba para llamar a la función power()
print(power(2, 3))   
print(power(5, 0))   
print(power(7, 1))   
print(power(2, -2))  
print(power(-3, 3))  
print(power(4, -1))  