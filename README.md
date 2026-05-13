


El sistema permite gestionar:

- Clientes
- Servicios
- Reservas

SIN utilizar bases de datos.

Toda la información se maneja mediante:

- Objetos
- Listas
- Manejo de archivos
- Logs

---

# Objetivos del Proyecto

El proyecto implementa:

##  Abstracción

Se implementa mediante:

- Clase abstracta `Entidad`
- Clase abstracta `Servicio`

Uso:

```python
from abc import ABC, abstractmethod
```

---

##  Herencia

Las clases:

- ReservaSala
- AlquilerEquipo
- AsesoriaEspecializada

heredan de:

```python
class Servicio(ABC)
```

---

## Polimorfismo

Cada servicio implementa su propia versión de:

```python
describir()
calcular_costo()
```

---

## Encapsulación

La clase Cliente utiliza atributos privados:

```python
self.__nombre
self.__correo
```

y utiliza:

- Getters
- Setters
- Validaciones

---

## Manejo avanzado de excepciones

El sistema implementa:

- try
- except
- else
- finally
- Excepciones personalizadas

---

## Logs de errores

Todos los errores se registran en:

```
logs/errores.log
```

mediante:

```python
import logging
```

---

# Estructura del Proyecto

```
software_fj/
│
├── main.py
│
├── modelos/
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── servicios_especializados.py
│   └── reserva.py
│
├── excepciones/
│   └── excepciones.py
│
├── utils/
│   └── logger.py
│
└── logs/
    └── errores.log
```

---

# Requisitos

- Python 3.10 o superior
- Visual Studio Code

---

# Cómo ejecutar el proyecto

## 1. Abrir Visual Studio Code

Abrir la carpeta:

```
software_fj
```

---

## 2. Ejecutar el sistema

En la terminal:

```bash
python main.py
```

---

# Resultado esperado

El sistema:

- Crea clientes
- Gestiona servicios
- Procesa reservas
- Calcula costos
- Maneja errores
- Registra logs
- Mantiene estabilidad

---

# Características especiales del proyecto

## Diseño modular

El sistema está dividido en módulos independientes.

## Código completamente comentado

Todo el proyecto contiene comentarios explicativos.

## Arquitectura escalable

Es fácil agregar nuevos servicios o funcionalidades.

## Sin bases de datos

Se cumple la condición del proyecto:
manejo únicamente mediante objetos y archivos.

---

# Autor

Proyecto académico desarrollado en Python.
