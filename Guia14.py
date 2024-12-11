from collections import deque

def reorganizar_cola(cola):

    pares = deque()
    impares = deque()

    while cola:
        numero = cola.popleft()
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    cola.extend(pares)
    cola.extend(impares)

    return cola
mi_cola = deque([3, 2, 5, 1, 4, 6])
cola_reorganizada = reorganizar_cola(mi_cola)
print(cola_reorganizada) 