
"""
===============================================================
LOGGER DEL SISTEMA
===============================================================
Archivo encargado de registrar
errores y eventos.
===============================================================
"""

import logging

# =========================================
# CONFIGURACIÓN DEL LOGGER
# =========================================
logging.basicConfig(
    filename="logs/errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# =========================================
# FUNCIÓN PARA REGISTRAR ERRORES
# =========================================
def registrar_error(error):

    logging.error(str(error))
