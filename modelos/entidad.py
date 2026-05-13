
"""
===============================================================
CLASE ABSTRACTA ENTIDAD
===============================================================
Esta clase representa una entidad general del sistema.

Se utiliza:
- Abstracción
- Métodos abstractos
===============================================================
"""

# =========================
# IMPORTACIONES
# =========================
from abc import ABC, abstractmethod


# =========================
# CLASE ABSTRACTA
# =========================
class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        """
        Método abstracto obligatorio.
        Todas las clases hijas deben implementarlo.
        """
        pass
