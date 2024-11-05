import math
class Rectangulo ():
  def __init__ (self,largo,ancho):
      self._ancho = ancho
      self._largo = largo
      
  def getArea (self):
        return self._ancho * self._largo
      
  def perimetro (self):
    return 2 * self._ancho + self._largo
  
  def diagonal (self):
    return math.sqrt (self._ancho ** 2 + self._largo **2)
    
  def comparar_con (self, otro):
    
    if self.getArea () > otro.getArea():
      print("El rectangulo1 tiene un area mayor que el rectangulo 2")
    elif self.getArea () < otro.getArea():
      print("El rectangulo2 tiene un area mayor que el rectangulo 1")
    else:
      print ("Ambos rectangulos tinen la misma area")
      
    if self.perimetro () > otro.perimetro():
      print("El rectangulo1 tiene un perimetro mayor que el rectangulo 2")
    elif self.perimetro () < otro.perimetro():
      print("El rectangulo2 tiene un perimetro mayor que el rectangulo 1")
    else:
      print ("Ambos rectangulos tinen el mismo perimetro")
      
    if self.diagonal () > otro.diagonal():
      print("El rectangulo1 tiene una diagonal mayor que el rectangulo 2")
    elif self.diagonal () < otro.diagonal():
      print("El rectangulo2 tiene una diagonal mayor que el rectangulo 1")
    else:
      print ("Ambos rectangulos tinen la misma diagonal") 