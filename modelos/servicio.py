
"""
===============================================================
CLASE ABSTRACTA SERVICIO
===============================================================
Clase base para todos los servicios.

Implementa:
- Abstracción
- Polimorfismo
===============================================================
"""

from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre):

        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        """
        Método obligatorio.
        """
        pass

    @abstractmethod
    def describir(self):
        """
        Método obligatorio.
        """
        pass

    # =========================================
    # MÉTODO "SOBRECARGADO"
    # Python lo maneja mediante parámetros
    # opcionales.
    # =========================================
    def calcular_total(
        self,
        impuesto=0,
        descuento=0
    ):

        total = self.calcular_costo()

        total += total * impuesto

        total -= descuento

        return total
