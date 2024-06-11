import unittest

import sys
import os

sys.path.append(os.getcwd() + "\\..\\..\\")

from src.main.Inventario import Inventario
from src.main.Producto import Producto

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.inventario = Inventario()

    def test_agregar_producto(self):
        producto1 = Producto("Producto 1", 10)
        producto2 = Producto("Producto 2", 5)

        self.inventario.agregar_producto(producto1)
        self.assertEqual(self.inventario.obtener_cantidad("Producto 1"), 10)

        self.inventario.agregar_producto(producto2)
        self.assertEqual(self.inventario.obtener_cantidad("Producto 2"), 5)

        self.inventario.agregar_producto(producto1)
        self.assertEqual(self.inventario.obtener_cantidad("Producto 1"), 20)

    def test_obtener_cantidad(self):
        producto1 = Producto("Producto 1", 10)
        producto2 = Producto("Producto 2", 5)

        self.inventario.agregar_producto(producto1)
        self.assertEqual(self.inventario.obtener_cantidad("Producto 1"), 10)

        self.inventario.agregar_producto(producto2)
        self.assertEqual(self.inventario.obtener_cantidad("Producto 2"), 5)

        self.assertEqual(self.inventario.obtener_cantidad("Producto 3"), "Producto no encontrado en el inventario")

    def test_eliminar_producto(self):
        producto1 = Producto("Producto 1", 10)
        producto2 = Producto("Producto 2", 5)

        self.inventario.agregar_producto(producto1)
        self.inventario.agregar_producto(producto2)

        self.inventario.eliminar_producto("Producto 1")
        self.assertEqual(self.inventario.obtener_cantidad("Producto 1"), "Producto no encontrado en el inventario")

        self.assertEqual(self.inventario.obtener_cantidad("Producto 2"), 5)

if __name__ == '__main__':
    unittest.main()