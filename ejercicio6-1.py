def mult(x, y):
    # Caso base: cuando y es 0, el producto es 0.
    if y == 0:
        return 0
    # Caso recursivo: suma x y veces.
    elif y > 0:
        return x + mult(x, y - 1)
    # Manejar caso negativo para y
    else:
        return -mult(x, -y)

# Programa de prueba para llamar a la función mult()
print(mult(5, 3))  # Salida esperada: 15
print(mult(7, 0))  # Salida esperada: 0
print(mult(-4, 3))  # Salida esperada: -12
print(mult(6, -2))  # Salida esperada: -12
print(mult(-3, -4))  # Salida esperada: 12