
class Cliente:
    def __init__(self, nombre, email, direccion):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.carrito = []
    def __str__(self):
        return f"Cliente: {self.nombre}\nEmail: {self.email}\nDirección: {self.direccion}"
    
    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)
        print(f"{producto.nombre} ha sido agregado al carrito.")

    def realizar_compra(self):
        if len(self.carrito) > 0:
            total = 0
            for producto in self.carrito:
                total += producto.precio
            descuento = 0.1  # Ejemplo de descuento del 10%
            precio_final = producto.calcular_precio(total, descuento)
            print(f"Compra realizada. Gracias por su compra, {self.nombre}! Los productos serán enviados a {self.direccion} y nos estaremos contactando a {self.email}")
            print(f"Precio final: {precio_final}")
            self.carrito = []
        else:
            print("El carrito está vacío. Agregue productos antes de realizar la compra.")

