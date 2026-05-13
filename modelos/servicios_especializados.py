
"""
===============================================================
SERVICIOS ESPECIALIZADOS
===============================================================
En este archivo se implementan:

- Herencia
- Polimorfismo
- Sobrescritura de métodos
===============================================================
"""

from modelos.servicio import Servicio


# ===========================================================
# SERVICIO: RESERVA DE SALAS
# ===========================================================
class ReservaSala(Servicio):

    def __init__(self, horas, cantidad_personas):

        super().__init__("Reserva de Sala")

        self.horas = horas
        self.cantidad_personas = cantidad_personas

    def calcular_costo(self):

        return self.horas * 50000

    def describir(self):

        return (
            f"[Sala] "
            f"{self.horas} horas | "
            f"{self.cantidad_personas} personas"
        )


# ===========================================================
# SERVICIO: ALQUILER DE EQUIPOS
# ===========================================================
class AlquilerEquipo(Servicio):

    def __init__(self, dias, tipo_equipo):

        super().__init__("Alquiler de Equipo")

        self.dias = dias
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self):

        return self.dias * 80000

    def describir(self):

        return (
            f"[Equipo] "
            f"{self.tipo_equipo} por "
            f"{self.dias} días"
        )


# ===========================================================
# SERVICIO: ASESORÍA ESPECIALIZADA
# ===========================================================
class AsesoriaEspecializada(Servicio):

    def __init__(self, horas, experto):

        super().__init__("Asesoría Especializada")

        self.horas = horas
        self.experto = experto

    def calcular_costo(self):

        return self.horas * 120000

    def describir(self):

        return (
            f"[Asesoría] "
            f"{self.experto} por "
            f"{self.horas} horas"
        )
