class BinarySearchTree(object):  # Árbol binario de búsqueda con claves duplicadas

   class __Node(object):  # Clase Nodo
      def __init__(self, clave, dato, izquierda=None, derecha=None):
         self.clave = clave
         self.dato = dato
         self.hijoIzquierdo = izquierda
         self.hijoDerecho = derecha

      def __str__(self):  # Representación como cadena para depuración
         return "{" + str(self.clave) + ", " + str(self.dato) + "}"

   def __init__(self):  # Inicializar el árbol
      self.__raiz = None
   
   def estaVacio(self):  # Verificar si el árbol está vacío
      return self.__raiz is None

   def raiz(self):  # Obtener la clave y el dato del nodo raíz
      if self.estaVacio():
         raise Exception("No hay nodo raíz en un árbol vacío")
      return self.__raiz.clave, self.__raiz.dato

   def __buscar(self, objetivo, masProfundo=True): 
      # Buscar el nodo más profundo o superficial con una clave
      pila = [(self.__raiz, None)]  # Pila con nodos y sus padres
      resultado = None
      padreResultado = None

      while pila:
         actual, padre = pila.pop()
         if actual:
            if actual.clave == objetivo:  # Nodo con clave coincidente
               if masProfundo:  # Guardar el nodo más profundo
                  resultado = actual
                  padreResultado = padre
               else:  # Guardar el nodo más superficial
                  if resultado is None:  # Solo actualizar en el primer hallazgo
                     resultado = actual
                     padreResultado = padre
            pila.append((actual.hijoIzquierdo, actual))
            pila.append((actual.hijoDerecho, actual))

      return resultado, padreResultado

   def buscar(self, objetivo, masProfundo=True): 
      # Buscar una clave y devolver el dato asociado
      nodo, _ = self.__buscar(objetivo, masProfundo=masProfundo)
      return nodo.dato if nodo else None

   def insertar(self, clave, dato):  
      if self.__raiz is None:  
         self.__raiz = self.__Node(clave, dato)
         return True

      # Encontrar el nodo más profundo con la misma clave o el padre para insertar
      nodo, padre = self.__buscar(clave, masProfundo=True)

      if nodo:  # Si la clave ya existe, insertar como hijo izquierdo del más profundo
         nuevoNodo = self.__Node(clave, dato)
         if nodo.hijoIzquierdo is None:  # Insertar directamente como hijo izquierdo
            nodo.hijoIzquierdo = nuevoNodo
         else:  # Empujar el subárbol izquierdo existente hacia abajo
            nuevoNodo.hijoIzquierdo = nodo.hijoIzquierdo
            nodo.hijoIzquierdo = nuevoNodo
      else:  # Insertar como una nueva clave
         nuevoNodo = self.__Node(clave, dato)
         if clave < padre.clave:
            padre.hijoIzquierdo = nuevoNodo
         else:
            padre.hijoDerecho = nuevoNodo
      return True

   def eliminar(self, objetivo): 
      # Eliminar el nodo más profundo con una clave coincidente
      nodo, padre = self.__buscar(objetivo, masProfundo=True)
      if nodo is None:  # Si no se encuentra la clave
         return None

      # Determinar el nodo de reemplazo
      if nodo.hijoIzquierdo and nodo.hijoDerecho:
         # Promover el sucesor como reemplazo
         self.__promoverSucesor(nodo)
      elif nodo.hijoIzquierdo or nodo.hijoDerecho:
         # Promover el único hijo
         hijo = nodo.hijoIzquierdo if nodo.hijoIzquierdo else nodo.hijoDerecho
         if padre is None:  # Si el nodo es la raíz
            self.__raiz = hijo
         elif padre.hijoIzquierdo is nodo:
            padre.hijoIzquierdo = hijo
         else:
            padre.hijoDerecho = hijo
      else:  # Nodo hoja
         if padre is None:  # Si el nodo es la raíz
            self.__raiz = None
         elif padre.hijoIzquierdo is nodo:
            padre.hijoIzquierdo = None
         else:
            padre.hijoDerecho = None

      return nodo.dato  # Devolver el dato del nodo eliminado

   def __promoverSucesor(self, nodo): 
      # Promover el sucesor al eliminar nodos con dos hijos
      sucesor = nodo.hijoDerecho
      padre = nodo
      while sucesor.hijoIzquierdo:
         padre = sucesor
         sucesor = sucesor.hijoIzquierdo

      nodo.clave = sucesor.clave
      nodo.dato = sucesor.dato
      if padre.hijoIzquierdo is sucesor:
         padre.hijoIzquierdo = sucesor.hijoDerecho
      else:
         padre.hijoDerecho = sucesor.hijoDerecho

   def imprimir(self):  # Imprimir la estructura del árbol
      self.__imprimirArbol(self.__raiz, "RAÍZ:   ", "")

   def __imprimirArbol(self, nodo, tipoNodo, sangria, nivel=4):
      if nodo:
         self.__imprimirArbol(nodo.hijoDerecho, "DERECHA:  ", sangria + " " * nivel, nivel)
         print(sangria + tipoNodo, nodo)
         self.__imprimirArbol(nodo.hijoIzquierdo, "IZQUIERDA: ", sangria + " " * nivel, nivel)

