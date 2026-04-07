---
title: Clase Fundamentos
description: Fundamentos de Bases de Datos
---

## Bases de Datos

:::note[Profesor]
José Luis MartíLara
:::

### Introducción a las Bases de Datos

### Conceptos Básicos asociados a las Bases de Datos

*   **Base de Datos**: Conjunto integrado de archivos (datos) relacionados entre sí.
*   **Dato**: Hecho relacionado con personas, objetos, lugares, eventos u otras entidades del mundo real.
    *   **Características**:
        *   Cualitativo (descriptivo) o cuantitativo
        *   Interno o externo
        *   Histórico o predictivo
*   **Información**: Datos organizados, preparados y/o formateados de una forma adecuada para la toma de decisiones u otras actividades de la organización.
    *   **Flujo**: Datos -> Información
    *   **Sistema de Información**: Utiliza archivos o bases de datos para transformar datos en información.
*   **Archivo**: Conjunto de datos relacionados entre sí, al compartir una misma estructura y/o comportamiento similar.

### Enfoques de Gestión de Datos

#### Enfoque de Archivos (Pasado)

*   **Descripción**: Las organizaciones desarrollaban sus sistemas de información de forma aislada, creando "islas de datos".
*   **Ejemplo Conceptual**:
    *   Programa Facturación usa Archivo Clientes, Archivo Facturas.
    *   Programa Compras usa Archivo Proveedores, Archivo Inventario Materiales.
    *   Programa Cuentas Por Pagar usa Archivo Proveedor, Archivo Cuentas Pagadas.
    *   Programa Ventas usa Archivo Clientes, Archivo Inventario Productos.
    *   Programa Sueldos usa Archivo Empleados.
*   **Desventajas**:
    *   Subutilización del espacio en disco
    *   Dependencia de los datos
    *   Baja productividad del desarrollador
    *   Falta de estandarización
    *   Inconsistencia de los datos (resultados)
    *   Problemas con el cliente

#### Enfoque de Bases de Datos (Actual)

*   **Descripción**: Visión centralizada y única de los datos.
*   **Características/Ventajas**:
    *   Minimización de la redundancia
    *   Independencia de los datos
    *   Estandarización
    *   Compartición de datos
    *   Seguridad de datos
    *   ...
*   **Ejemplo Conceptual**: Un conjunto de archivos (Clientes, Cuentas Pagadas, Empleados, Inventario, Proveedor, Factura, Balance, Estadísticas Ventas) son gestionados de forma integrada.

#### Componentes del Enfoque de Bases de Datos

1.  **Usuarios**: Personas con requisitos de información que realizan operaciones de ingreso, modificación, eliminación, consulta y mantención de la base de datos.
    *   Usuario Final
    *   Desarrollador de Aplicaciones
    *   Diseñador de la Base de Datos
    *   Administrador de Bases de Datos (DBA)
    *   Administrador de Datos (Arquitecto)
2.  **Sistema Administrador de Bases de Datos (SABD)**: Software que permite crear y mantener una o más bases de datos.
    *   También conocido como motor o servidor de datos.
    *   **Funciones Principales**:
        *   **Definición de Datos (DD)**: Sentencias para crear, modificar o eliminar la estructura de la base de datos.
            ```sql
            CREATE TABLE ...
            ALTER TABLE ...
            DROP TABLE ...
            ```
        *   **Manipulación de Datos (DM)**: Sentencias para insertar, actualizar o eliminar datos.
            ```sql
            INSERT INTO ...
            UPDATE ...
            DELETE FROM ...
            ```
        *   **Control de Datos (DC)**: Sentencias para otorgar o revocar permisos.
            ```sql
            GRANT ...
            REVOKE ...
            ```
3.  **Interfaz de Usuario**: Forma en que el SABD permite la interacción con la base de datos.
4.  **Base de Datos**:
    *   Conjunto de datos operacionales, almacenados en el computador y accesados por distintas aplicaciones.
    *   Lugar físico donde están almacenados los datos.
5.  **Diccionario de Datos**: Es una base de datos que guarda una descripción de los datos, como su tipo, largo, propietario, tamaño de los registros, etc.
6.  **Administrador de la Base de Datos (DBA)**: Persona o grupo de personas encargadas de dirigir y controlar el recurso dato.
    *   **Funciones**:
        *   Definición de la base de datos y/o archivos a usar (junto con el analista y usuario).
        *   Selección de la estructura de almacenamiento y la estrategia de recuperación.
        *   Definición de los distintos tipos de acceso y su mantención.
        *   Definición de la estrategia de respaldo a usar, implementarla y controlarla.
        *   Preocuparse del desempeño de la base de datos y afinarlo.
        *   Proveer de capacitación, entrenamiento y apoyo a las consultas de los usuarios.
    *   **Responsabilidad**: Las bases de datos físicas.
7.  **Administrador de Datos (Arquitecto)**: Responsable de desarrollar y administrar las normas, procedimientos, prácticas y planes para la definición, organización, protección y utilización eficiente de los datos dentro de la organización, incluyendo todos los datos, estén o no en la base de datos.

### Proceso de Diseño de Bases de Datos

:::note[Objetivo General]
Realizar una serie de pasos que van desde la recolección de información hasta el diseño e implementación de los archivos y sus organizaciones para almacenar los datos.
:::

#### Etapa 1: Recolección y Análisis de Requisitos

*   **Objetivo**: Identificar las necesidades de información de los usuarios.
*   **Pasos**:
    *   Identificación de las áreas de aplicación y grupos de usuarios. Elección de participantes principales.
    *   Análisis y estudio de la documentación existente en las actuales aplicaciones. Considerar manuales de políticas, formas, reportes y diagramas organizacionales.
    *   Estudio del actual ambiente operativo y uso de la información. Incluye un análisis de los tipos de transacciones y sus frecuencias, y del flujo de información en el sistema.
    *   Obtención de respuestas de cuestionarios de los potenciales usuarios. Identificación de prioridades.
    *   Formalización de Requisitos.

#### Etapa 2: Diseño Conceptual

*   **Objetivo**: Construir un esquema conceptual que represente los datos necesarios para el sistema de información, **independiente del motor de datos a utilizar**.
*   **El modelo conceptual sirve como**:
    *   Medio de comunicación entre usuarios y especialistas (expresivo, simple, mínimo, formal, diagramático).
    *   Mecanismo para validar el entendimiento alcanzado del problema por parte del especialista.
    *   Descripción estable del contenido.
*   **Ejemplo**: Un modelo que muestra entidades como `Factura`, `Cliente`, `Producto` y sus relaciones (`tiene`, `considera`) con atributos clave (ID) y relaciones de cardinalidad.

#### Etapa 3: Elección de Software

*   **Objetivo**: Seleccionar el tipo de software que mejor se adecúe a las necesidades del sistema a construir.
*   **Criterios a considerar**:
    *   **Costos**: Adquisición de hardware y software; operación y mantención del sistema; migración.
    *   Requisitos del sistema: funcionales y no funcionales.
    *   Estructuración de los datos.

#### Etapa 4: Diseño Lógico

*   **Objetivo**: Generar un esquema basado en el modelo de datos soportado por el software escogido.
*   **Pasos**:
    *   Transformación independiente del sistema a un modelo relacional, orientado a objetos u otro.
    *   Conversión de los esquemas a un software de bases de datos específico.
*   **Ejemplo**: Transformar el modelo conceptual (con relaciones explícitas) a un modelo relacional donde las relaciones se representan mediante claves foráneas (FK). Por ejemplo, `RUT-Cliente {FK}` en la tabla `Factura`.

#### Etapa 5: Diseño Físico

*   **Objetivo**: Escoger las estructuras de almacenamiento y métodos de acceso, además de la ubicación de los archivos de bases de datos, para obtener un buen rendimiento de las distintas aplicaciones que interactúan con la base de datos.
*   **Criterios a considerar**:
    *   **Tiempo de Respuesta**: Tiempo que transcurre desde el ingreso de la transacción hasta el recibo de su respuesta.
    *   **Rendimiento del Sistema**: Número promedio de transacciones que pueden ser procesadas por minuto.
    *   **Utilización del espacio en disco**: Cantidad de memoria ocupada por los archivos e índices.
*   **Estructuras de almacenamiento**:
    *   Secuenciales (desordenados, ordenados)
    *   Directo (hashing estático o con expansión dinámica)
    *   De tipo Árbol (B-Tree)
*   **Índices**:
    *   Dinámicos (hashing con expansión dinámica, de tipo Árbol B o B+)
    *   Bitmap

#### Etapa 6: Implementación de la Base de Datos

*   **Objetivo**: Codificación de sentencias para la definición y la manipulación de la base de datos, para crear los archivos y su poblamiento.
*   **Ejemplos de sentencias**:
    ```sql
    SELECT rut, nombre FROM alumno;
    SELECT * FROM alumno WHERE carrera='INF';
    ```