import heapq
from collections import defaultdict

# Clase para el nodo de Huffman
class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

# Función para construir el árbol de Huffman
def construir_arbol_huffman(texto):
    # Contar la frecuencia de cada carácter en el texto
    frecuencia = defaultdict(int)
    for caracter in texto:
        frecuencia[caracter] += 1

    # Crear una cola de prioridad (heap) basada en las frecuencias
    heap = [NodoHuffman(caracter, freq) for caracter, freq in frecuencia.items()]
    heapq.heapify(heap)

    # Construir el árbol de Huffman
    while len(heap) > 1:
        izquierdo = heapq.heappop(heap)
        derecho = heapq.heappop(heap)
        nodo_padre = NodoHuffman(None, izquierdo.frecuencia + derecho.frecuencia)
        nodo_padre.izquierda = izquierdo
        nodo_padre.derecha = derecho
        heapq.heappush(heap, nodo_padre)

    # El único nodo restante es la raíz del árbol
    return heap[0]

# Función para crear la tabla de códigos de Huffman
def crear_tabla_codigos(nodo, prefijo="", tabla_codigos=None):
    if tabla_codigos is None:
        tabla_codigos = {}

    if nodo is not None:
        if nodo.caracter is not None:
            tabla_codigos[nodo.caracter] = prefijo
        crear_tabla_codigos(nodo.izquierda, prefijo + "0", tabla_codigos)
        crear_tabla_codigos(nodo.derecha, prefijo + "1", tabla_codigos)

    return tabla_codigos

# Función para codificar el mensaje en binario
def codificar(texto, tabla_codigos):
    return ''.join(tabla_codigos[caracter] for caracter in texto)

# Función para decodificar el mensaje binario
def decodificar(mensaje_binario, raiz_arbol):
    texto_decodificado = []
    nodo_actual = raiz_arbol
    for bit in mensaje_binario:
        if bit == "0":
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha

        if nodo_actual.caracter is not None:
            texto_decodificado.append(nodo_actual.caracter)
            nodo_actual = raiz_arbol

    return ''.join(texto_decodificado)

# Función para mostrar el árbol de Huffman (para mensajes pequeños)
def mostrar_arbol_huffman(nodo, nivel=0):
    if nodo is not None:
        if nodo.caracter is not None:
            print(" " * nivel + f"{nodo.caracter}: {nodo.frecuencia}")
        else:
            print(" " * nivel + f"Frecuencia: {nodo.frecuencia}")
        mostrar_arbol_huffman(nodo.izquierda, nivel + 2)
        mostrar_arbol_huffman(nodo.derecha, nivel + 2)

# Programa principal
if __name__ == "__main__":
    # Aceptar un mensaje de texto
    mensaje = input("Ingrese un mensaje de texto: ")

    # Crear el árbol de Huffman
    raiz_arbol = construir_arbol_huffman(mensaje)

    # Crear la tabla de códigos
    tabla_codigos = crear_tabla_codigos(raiz_arbol)

    # Codificar el mensaje
    mensaje_codificado = codificar(mensaje, tabla_codigos)

    # Decodificar el mensaje
    mensaje_decodificado = decodificar(mensaje_codificado, raiz_arbol)

    # Mostrar resultados
    print(f"Mensaje original: {mensaje}")
    print(f"Mensaje codificado en binario: {mensaje_codificado}")
    print(f"Mensaje decodificado: {mensaje_decodificado}")
    print(f"Total de bits en el mensaje codificado: {len(mensaje_codificado)} bits")
    print(f"Total de caracteres en el mensaje original: {len(mensaje)} caracteres")

    # Mostrar el árbol de Huffman si el mensaje es corto
    if len(mensaje) <= 20:  # Puede ajustar el límite de longitud del mensaje
        print("\nÁrbol de Huffman:")
        mostrar_arbol_huffman(raiz_arbol)