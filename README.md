# 💻 Software FJ

## Sistema Integral de Gestión de Clientes, Servicios y Reservas

**Proyecto académico de Programación Orientada a Objetos en Python**

---

## 📌 Descripción del proyecto

**Software FJ** es un sistema desarrollado en Python que permite gestionar clientes, servicios y reservas de manera organizada. Su propósito es facilitar el registro de clientes, la selección de servicios, el cálculo de costos y el procesamiento de reservas.

El proyecto aplica los principios fundamentales de la **Programación Orientada a Objetos (POO)** y mecanismos de manejo de excepciones y registro de eventos.

## 🎯 Objetivo general

Desarrollar un sistema integral que permita administrar clientes, servicios y reservas mediante Python, aplicando conceptos de programación orientada a objetos, validaciones, excepciones personalizadas y registro de eventos.

## ✨ Funcionalidades principales

- 👤 **Gestión de clientes:** registro y validación de nombres, documentos, correos electrónicos y teléfonos.
- 🏢 **Gestión de servicios:** manejo de diferentes tipos de servicios especializados.
- 📅 **Gestión de reservas:** creación, confirmación, cancelación y procesamiento de reservas.
- 💰 **Cálculo de costos:** cálculo de tarifas, descuentos e impuestos.
- ⚠️ **Validaciones y excepciones:** control de datos incorrectos y situaciones no permitidas.
- 📝 **Registro de eventos:** almacenamiento de operaciones y errores en archivos de log.
- 🔄 **Menú interactivo:** navegación por las opciones del sistema desde la consola.

## 🧩 Servicios disponibles

El sistema contempla tres tipos de servicios:

| Servicio                     | Descripción                                          |
| ---------------------------- | ---------------------------------------------------- |
| 🏢 Reserva de salas          | Gestión del alquiler de espacios por horas.          |
| 💻 Alquiler de equipos       | Gestión del alquiler de equipos por cantidad y días. |
| 👨‍💻 Asesorías tecnológicas | Gestión de asesorías según el tiempo contratado.     |

## 🛠️ Tecnologías utilizadas

- 🐍 Python 3
- 🧠 Programación Orientada a Objetos (POO)
- 🧪 Unittest para pruebas automatizadas
- 📂 Módulos y paquetes de Python
- 📝 Logging para el registro de eventos y errores
- 🔗 Git y GitHub para el control de versiones

## 📚 Conceptos de programación aplicados

En el desarrollo del proyecto se implementan los siguientes conceptos:

- **Abstracción:** definición de clases base abstractas.
- **Herencia:** reutilización de atributos y métodos entre clases.
- **Polimorfismo:** implementación especializada de métodos según el tipo de servicio.
- **Encapsulamiento:** protección y acceso controlado a los atributos de las clases.
- **Excepciones personalizadas:** manejo de errores específicos del sistema.
- **Manejo de excepciones:** utilización de `try`, `except`, `else` y `finally`.
- **Encadenamiento de excepciones:** conservación de la causa original de un error.

## 📁 Estructura del proyecto

```text
Software-FJ/
│
├── entidades/
│   ├── __init__.py
│   ├── entidad.py
│   ├── cliente.py
│   └── validaciones.py
│
├── servicios/
│   ├── __init__.py
│   ├── servicio.py
│   ├── servicios_especializados.py
│   └── calculadora_costos.py
│
├── reservas/
│   ├── __init__.py
│   └── reserva.py
│
├── excepciones/
│   ├── __init__.py
│   └── excepciones_personalizadas.py
│
├── utilidades/
│   └── __init__.py
│
├── pruebas/
│   ├── __init__.py
│   └── test_pruebas_sistema.py
│
├── logs/
│   └── sistema.log
│
├── main.py
├── .gitignore
└── README.md
```

## ⚙️ Requisitos para ejecutar el proyecto

Antes de iniciar, asegúrate de tener instalado:

- Python 3.10 o superior (o una versión compatible con el código).
- Visual Studio Code o cualquier editor de código.
- Git (opcional, para clonar el repositorio).

## 🚀 Instalación y ejecución

**1. Clonar el repositorio**

```bash
git clone https://github.com/KarenLore/Software-FJ.git
```

**2. Ingresar a la carpeta del proyecto**

```bash
cd Software-FJ
```

**3. Ejecutar el sistema**

```bash
python main.py
```

El programa mostrará un menú interactivo desde el cual se podrán registrar clientes, consultar servicios, crear reservas y procesar operaciones.

## 🧪 Ejecución de pruebas

El proyecto cuenta con **15 pruebas automatizadas** para verificar el funcionamiento de sus principales componentes y operaciones.

Para ejecutar las pruebas, utiliza el siguiente comando desde la carpeta principal:

```bash
python -m unittest discover -s pruebas -p "test_*.py" -v
```

Las pruebas contemplan:

- Creación y validación de clientes.
- Validación de documentos y correos electrónicos.
- Cálculo de costos de los servicios.
- Creación y confirmación de reservas.
- Cancelación y procesamiento de reservas.
- Manejo de estados no permitidos.
- Validación de excepciones personalizadas.
- Encadenamiento de excepciones.

**Resultado obtenido:** 15 pruebas ejecutadas correctamente.

## 📝 Registro de eventos y errores

El sistema utiliza el módulo `logging` de Python para registrar las operaciones realizadas.

Los registros se almacenan en:

```text
logs/sistema.log
```

Estos registros permiten consultar eventos como la creación, confirmación, cancelación y procesamiento de reservas, además de los errores presentados durante las operaciones.

## 👥 Integrantes del equipo

Proyecto desarrollado colaborativamente por:

- **Ayelmer Jusephe Corzo Barboza**
- **Elidallana Cristancho Caceres**
- **Karen Lorena Cristancho Caceres**

## 🔗 Repositorio del proyecto

Puedes consultar el código fuente y el desarrollo del proyecto en GitHub:

👉 [Software FJ – Repositorio GitHub](https://github.com/KarenLore/Software-FJ)

## 🎓 Contexto académico

- **Curso:** Programación
- **Código del curso:** 213023
- **Actividad:** Fase 4
- **Lenguaje de programación:** Python
- **Enfoque:** Programación Orientada a Objetos

## 📄 Conclusión

El desarrollo de Software FJ permitió aplicar los fundamentos de la programación orientada a objetos en la construcción de una solución práctica para la gestión de clientes, servicios y reservas. Además, permitió fortalecer el trabajo colaborativo, la organización del código, la validación de datos, el manejo de excepciones y la ejecución de pruebas automatizadas.

---

## 💻 SOFTWARE FJ

*Organización, tecnología y soluciones eficientes.*