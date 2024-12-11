class ColaBanco:
    def __init__(self):
        self.cola = []

    def agregar_cliente(self, numero_cliente):
        self.cola.append(numero_cliente)
        print(f"Cliente {numero_cliente} agregado a la cola.")

    def atender_cliente(self):
        if not self.cola:
            print("No hay clientes en la cola.")
            return
        cliente_atendido = self.cola.pop(0)
        print(f"Atendiendo al cliente {cliente_atendido}.")

    def ver_cola(self):
        print("Cola actual:", self.cola)

# Ejemplo de uso:
banco = ColaBanco()
banco.agregar_cliente(1)
banco.agregar_cliente(3)
banco.agregar_cliente(2)
banco.ver_cola()

banco.atender_cliente()
banco.ver_cola()

banco.atender_cliente()
banco.ver_cliente()
