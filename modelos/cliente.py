
"""
===============================================================
CLASE CLIENTE
===============================================================
Esta clase representa a los clientes del sistema.

Se implementa:
- Encapsulación
- Validaciones
- Herencia
===============================================================
"""

from modelos.entidad import Entidad


class Cliente(Entidad):

    def __init__(self, nombre, correo, documento):

        # =========================================
        # ATRIBUTOS PRIVADOS
        # Encapsulación mediante doble guión bajo
        # =========================================
        self.__nombre = None
        self.__correo = None
        self.__documento = None

        # =========================================
        # USO DE SETTERS PARA VALIDAR
        # =========================================
        self.nombre = nombre
        self.correo = correo
        self.documento = documento

    # =========================================
    # GETTERS Y SETTERS
    # =========================================

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if len(valor.strip()) < 3:
            raise ValueError(
                "El nombre debe tener mínimo 3 caracteres"
            )

        self.__nombre = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        if "@" not in valor:
            raise ValueError("Correo inválido")

        self.__correo = valor

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):

        if not valor.isdigit():
            raise ValueError(
                "El documento debe contener solo números"
            )

        self.__documento = valor

    # =========================================
    # MÉTODO HEREDADO
    # =========================================
    def mostrar_info(self):

        return (
            f"Cliente: {self.nombre} | "
            f"Correo: {self.correo}"
        )
