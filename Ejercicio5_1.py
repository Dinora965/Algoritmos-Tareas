class LinkedList(object):
    # Una lista enlazada de elementos de datos

    def __iter__(self):
        """Iterador para recorrer la lista enlazada."""
        link = self.getFirst()  # Empezar con el primer enlace
        while link is not None:  # Seguir hasta que no haya más enlaces
            yield link  # Devolver el enlace actual
            link = link.getNext()  # Pasar al siguiente enlace

    def traverse(self, func=print):
        """Aplicar una función a todos los elementos de la lista."""
        for link in self:  # Usar el iterador para recorrer la lista
            func(link.getData())  # Aplicar la función al dato

    def __len__(self):
        """Devolver la longitud de la lista."""
        return sum(1 for _ in self)  # Contar los elementos usando el iterador

    def __str__(self):
        """Devolver una representación en cadena de la lista."""
        result = "["  # Envolver la lista en corchetes
        first = True
        for link in self:  # Usar el iterador para recorrer la lista
            if not first:
                result += " > "  # Separar los enlaces con " > "
            result += str(link)  # Añadir la versión en cadena del enlace
            first = False
        return result + "]"  # Cerrar la lista con corchetes