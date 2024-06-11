class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.nombre in self.productos:
            self.productos[producto.nombre].cantidad += producto.cantidad
        else:
            self.productos[producto.nombre] = producto

    def obtener_cantidad(self, nombre_producto):
        if nombre_producto in self.productos:
            return self.productos[nombre_producto].cantidad
        else:
            return 'Producto no encontrado en el inventario'

    def eliminar_producto(self, nombre_producto):
        if nombre_producto in self.productos:
            del self.productos[nombre_producto]
        else:
            return 'Producto no encontrado en el inventario'