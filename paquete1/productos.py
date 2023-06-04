class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio(self, total, descuento):
        return total * (1 - descuento)