
# SOFTWARE FJ
## Sistema Integral de Gestión de Clientes, Servicios y Reservas

### 1. Descripción del proyecto

Software FJ es un sistema desarrollado en Python que permite gestionar
clientes, servicios y reservas mediante programación orientada a objetos.

El sistema permite registrar clientes, administrar diferentes tipos
de servicios, crear reservas, confirmar o cancelar operaciones y
calcular los costos correspondientes.

### 2. Objetivo general

Desarrollar un sistema integral de gestión de clientes, servicios
y reservas aplicando los principios de programación orientada a
objetos y el manejo de excepciones en Python.

### 3. Objetivos específicos

- Aplicar abstracción, herencia, encapsulamiento y polimorfismo.
- Implementar clases para gestionar clientes y servicios.
- Crear un sistema de reservas con diferentes estados.
- Implementar excepciones personalizadas.
- Utilizar estructuras try, except, else y finally.
- Registrar eventos y errores del sistema.
- Realizar pruebas de operaciones válidas e inválidas.

### 4. Tecnologías utilizadas

- Lenguaje de programación: Python.
- Entorno de desarrollo: Visual Studio Code.
- Control de versiones: Git.
- Repositorio colaborativo: GitHub.
- Programación orientada a objetos.

### 5. Estructura del proyecto

Software-FJ/
│
├── entidades/
│   ├── entidad.py
│   ├── cliente.py
│   └── validaciones.py
│
├── servicios/
│   ├── servicio.py
│   ├── servicios_especializados.py
│   └── calculadora_costos.py
│
├── reservas/
│   └── reserva.py
│
├── excepciones/
│   └── excepciones_personalizadas.py
│
├── utilidades/
│
├── pruebas/
│
├── logs/
│
├── main.py
└── README.md

### 6. Funcionalidades principales

- Registro y validación de clientes.
- Gestión de reservas de salas.
- Gestión de alquiler de equipos.
- Administración de asesorías.
- Cálculo de costos, impuestos y descuentos.
- Confirmación y cancelación de reservas.
- Procesamiento de reservas.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores.

### 7. Programación orientada a objetos

El proyecto aplica los siguientes conceptos:

**Abstracción:** mediante las clases abstractas Entidad y Servicio.

**Herencia:** las clases especializadas heredan de Servicio y Cliente
hereda de Entidad.

**Polimorfismo:** los diferentes servicios implementan su propio
método calcular_costo().

**Encapsulamiento:** los atributos se protegen mediante atributos
privados por convención y propiedades.

### 8. Manejo de excepciones

El sistema implementa excepciones personalizadas para controlar
situaciones como datos inválidos, servicios incorrectos, estados
inadecuados y errores durante el procesamiento de reservas.

Se utilizan las estructuras try, except, else y finally,
además del encadenamiento de excepciones.

### 9. Integrantes

- Ayelmer Jusephe Corzo Barboza.
- Elidallana Cristancho Caceres.
- Karen Lorena Cristancho Caceres.

### 10. Ejecución del proyecto

Para ejecutar el sistema, se debe contar con Python 3 instalado.

Desde la terminal, ubicarse en la carpeta principal del proyecto
y ejecutar:

python main.py

### 11. Repositorio

GitHub:
https://github.com/KarenLore/Software-FJ

### 12. Conclusiones

El desarrollo del proyecto permite aplicar los fundamentos de
programación orientada a objetos mediante la construcción de un
sistema de gestión.

También permite fortalecer el manejo de excepciones para controlar
errores, validar operaciones y mantener un registro de los eventos
del sistema.

### 13. Referencias

Python Software Foundation. (s. f.). Python documentation.
https://docs.python.org/3/

Git. (s. f.). Git documentation.
https://git-scm.com/doc