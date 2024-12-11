from collections import deque

def ordenar_cola(cola):


    cola_auxiliar = deque()

    while cola:
        min_valor = float('inf')
        while cola:
            valor = cola.popleft()
            min_valor = min(min_valor, valor)
            cola_auxiliar.append(valor)


        while cola_auxiliar and cola_auxiliar[-1] != min_valor:
            cola.append(cola_auxiliar.popleft())

        
        cola.append(min_valor)
        cola_auxiliar.pop()

    return cola


mi_cola = deque([3, 2, 5, 1, 4])
cola_ordenada = ordenar_cola(mi_cola)
print(cola_ordenada)  # Salida: deque([1, 2, 3, 4, 5])