from Rectangulos import Rectangulo

def llenardatos ():
    largo = float (input("Introduce el largo del rectangulo:"))
    ancho = float (input("Introduce el ancho del rectangulo:"))
    return Rectangulo (largo,ancho)

rectangulo = llenardatos()
print ("El Area del Rectangulo es:", rectangulo. getArea())
print ("El perimetro del Rectangulo es:", rectangulo. perimetro())
print ("La Diagonal del Rectangulo es:", rectangulo. diagonal())

Comparar = input ("Deseas comparar dos rectangulo con otro? (si/no):").strip().lower ()

if Comparar == 'si':
    print ("Introduce los datos del primer rectangulo:")
    rectangulo1 = llenardatos()
    print ("Introduce los datos del Segundo rectangulo:")
    rectangulo2 = llenardatos()
    
    rectangulo1.comparar_con(rectangulo2)
else:
 print ("No se realizara ninguna comparacion")
