
"""
===============================================================
CLASE RESERVA
===============================================================
Integra:
- Cliente
- Servicio
- Estado
- Confirmación
- Cancelación
===============================================================
"""


class Reserva:

    def __init__(self, cliente, servicio):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    # =========================================
    # CONFIRMAR RESERVA
    # =========================================
    def confirmar(self):

        self.estado = "Confirmada"

    # =========================================
    # CANCELAR RESERVA
    # =========================================
    def cancelar(self):

        self.estado = "Cancelada"

    # =========================================
    # MOSTRAR INFORMACIÓN
    # =========================================
    def mostrar_detalle(self):

        return (
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Costo: ${self.servicio.calcular_costo()} | "
            f"Estado: {self.estado}"
        )
