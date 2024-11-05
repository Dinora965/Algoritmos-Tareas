# A program to reverse the letters of a word

from SimpleStack import *

stack = Stack(100) # Create a stack to hold letters
word = input("Word to reverse: ")

for letter in word: # Loop over letters in word
    if not stack.isFull(): # Push letters on stack if not full
        stack.push(letter)
 
reverse = '' # Build the reversed version
while not stack.isEmpty(): # by popping the stack until empty
    reverse += stack.pop()
print('The reverse of', word, 'is', reverse)

def is_palindrome(sentence):
    stack = Stack(100)  # Crear una pila con capacidad suficiente
    clean_sentence = ''

    # Limpiar la cadena de entrada: eliminar espacios, dígitos, y puntuación, y convertir a minúsculas
    for char in sentence:
        if char.isalpha():  # Incluir solo letras
            clean_sentence += char.lower()

    # Agregar letras a la pila
    for letter in clean_sentence:
        stack.push(letter)

    # Reconstruir la cadena invertida usando la pila
    reverse_sentence = ''
    while not stack.isEmpty():
        reverse_sentence += stack.pop()

    # Comparar la cadena limpia con su versión invertida
    return clean_sentence == reverse_sentence

# Prueba del programa
sentence = "Un hombre, un plan, un canal, Panamá"
if is_palindrome(sentence):
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")