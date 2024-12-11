class HistorialNavegacion:
    def __init__(self):
        self.historial = []

    def visitar_pagina(self, pagina):
        self.historial.append(pagina)

    def ir_atras(self):
        if not self.historial:
            print("No hay páginas anteriores en el historial.")
            return
        return self.historial.pop()

historial = HistorialNavegacion()
historial.visitar_pagina("https://www.facebook.com")
historial.visitar_pagina("https://www.google.com")
historial.visitar_pagina("https://www.youtube.com")

print("Página actual:", historial.historial[-1])

print("Regresando a la página anterior...")
pagina_anterior = historial.ir_atras()
print("Página actual:", pagina_anterior)