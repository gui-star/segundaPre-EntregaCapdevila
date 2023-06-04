from paquete1 import productos
from paquete1 import cliente
from paquete1.productos import Producto
from paquete1.cliente import Cliente

producto1 = Producto("Pantalón", 5400)
producto2 = Producto("Camisa", 3500)

cliente1 = Cliente("Juan", "juan@example.com", "Calle Principal 123")
cliente1.agregar_al_carrito(producto1)
cliente1.agregar_al_carrito(producto2)
cliente1.realizar_compra()