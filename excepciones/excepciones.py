
"""
===============================================================
EXCEPCIONES PERSONALIZADAS
===============================================================
Aquí se crean errores personalizados
para el sistema.
===============================================================
"""


class ServicioNoDisponibleError(Exception):
    """
    Error personalizado para servicios
    no disponibles.
    """
    pass


class ReservaInvalidaError(Exception):
    """
    Error personalizado para reservas inválidas.
    """
    pass
