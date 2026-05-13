
"""
===============================================================
PROYECTO: SOFTWARE FJ
AUTOR: ChatGPT
DESCRIPCIÓN:
Sistema integral orientado a objetos desarrollado en Python.
El sistema permite gestionar clientes, servicios y reservas
sin utilizar bases de datos.

Se implementan:
- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo avanzado de excepciones
- Logs de errores
- Modularidad
===============================================================
"""

# =========================
# IMPORTACIÓN DE CLASES
# =========================
from modelos.cliente import Cliente
from modelos.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from modelos.reserva import Reserva

from excepciones.excepciones import ServicioNoDisponibleError
from utils.logger import registrar_error


# =========================
# FUNCIÓN PRINCIPAL
# =========================
def main():
    """
    Función principal del sistema.

    Aquí se crean:
    - Clientes
    - Servicios
    - Reservas

    Además:
    - Se ejecutan validaciones
    - Se manejan excepciones
    - Se registran errores en logs
    """

    try:

        # =========================================
        # CREACIÓN DEL CLIENTE
        # =========================================
        cliente = Cliente(
            nombre="Edward Santiago",
            correo="edward@softwarefj.com",
            documento="123456789"
        )

        # =========================================
        # CREACIÓN DE SERVICIOS
        # =========================================

        # Servicio 1: Reserva de salas
        servicio_sala = ReservaSala(
            horas=4,
            cantidad_personas=12
        )

        # Servicio 2: Alquiler de equipos
        servicio_equipo = AlquilerEquipo(
            dias=3,
            tipo_equipo="Laptop"
        )

        # Servicio 3: Asesoría especializada
        servicio_asesoria = AsesoriaEspecializada(
            horas=5,
            experto="Ingeniería de Software"
        )

        # =========================================
        # CREACIÓN DE RESERVAS
        # =========================================
        reserva1 = Reserva(cliente, servicio_sala)
        reserva2 = Reserva(cliente, servicio_equipo)
        reserva3 = Reserva(cliente, servicio_asesoria)

        # =========================================
        # CONFIRMAR RESERVAS
        # =========================================
        reserva1.confirmar()
        reserva2.confirmar()
        reserva3.confirmar()

        # =========================================
        # MOSTRAR INFORMACIÓN
        # =========================================
        print("\n========= RESERVAS =========")

        for reserva in [reserva1, reserva2, reserva3]:
            print(reserva.mostrar_detalle())

        # =========================================
        # EJEMPLO DE POLIMORFISMO
        # =========================================
        print("\n========= POLIMORFISMO =========")

        servicios = [
            servicio_sala,
            servicio_equipo,
            servicio_asesoria
        ]

        # Cada objeto ejecuta SU PROPIA versión
        # del método describir()
        for servicio in servicios:
            print(servicio.describir())

        # =========================================
        # EJEMPLO DE ERROR PERSONALIZADO
        # =========================================
        if servicio_sala.horas > 10:
            raise ServicioNoDisponibleError(
                "No se permiten reservas superiores a 10 horas"
            )

    # =========================================
    # CAPTURA DE EXCEPCIÓN PERSONALIZADA
    # =========================================
    except ServicioNoDisponibleError as error:
        registrar_error(error)
        print(f"ERROR PERSONALIZADO: {error}")

    # =========================================
    # CAPTURA GENERAL DE ERRORES
    # =========================================
    except Exception as error:
        registrar_error(error)
        print(f"ERROR GENERAL: {error}")

    # =========================================
    # BLOQUE ELSE
    # Se ejecuta si NO hubo errores
    # =========================================
    else:
        print("\nSistema ejecutado correctamente.")

    # =========================================
    # BLOQUE FINALLY
    # Siempre se ejecuta
    # =========================================
    finally:
        print("\nFinalizó la ejecución del sistema.")


# =========================================
# EJECUCIÓN DEL PROGRAMA
# =========================================
if __name__ == "__main__":
    main()
