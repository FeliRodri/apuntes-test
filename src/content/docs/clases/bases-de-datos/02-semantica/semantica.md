---
title: Clase Semántica
description: Semántica de las Bases de Datos
---

## Semántica de los Datos

### ¿Qué es la Semántica de los Datos?
Se refiere al significado de las relaciones que tienen los datos entre sí. La explicación de estas semánticas se realizará utilizando la notación del diagrama de clases UML.

### Notaciones Comunes para la Semántica
Existen diversas notaciones para representar la semántica de los datos:
*   Diagrama de Bachmann
*   Diagramas Entidad-Relación (E-R): incluye el modelo básico y sus extensiones.
*   Diagrama de Clases (UML)

:::tip[Ejemplo de Clase (STACK)]
```
Clase STACK
datos : Array
tope : Integer
push(nro)
pop() : Integer
largo() : Integer
```
:::

### Atributos en Diagramas de Clases
La sintaxis general para definir atributos es: `visibilidad nombre : tipo = valor_inicial{propiedad}`

*   **Visibilidad**:
    *   `+`: pública
    *   `#`: protegida
    *   `-`: privada
*   **Propiedad**:
    *   `{unique}`
    *   `{not null}`
    *   ...

### Cardinalidad (Multiplicidad)
Se refiere al número de entidades con que otra entidad se relaciona.

*   **1:1 (Uno a Uno)**: Sucede cuando una entidad `X` se relaciona solo con otra entidad, bajo una determinada asociación, y esta última solo lo hace con `X`.
    *   _Ejemplo_: Empleado (1) - Conyuge (1)
*   **1:N (Uno a Muchos)**: Se presenta cuando una entidad `X` se relaciona con varias entidades, bajo una determinada asociación, pero cada una de estas solo lo hace con `X`.
    *   _Ejemplo_: Persona (*) - Automóvil (1)
*   **M:N (Muchos a Muchos)**: Ocurre cuando una entidad `X` se relaciona con varias entidades, bajo una determinada asociación, y cada una de estas, a su vez, se relaciona con `X` y, probablemente, con otras entidades más del mismo tipo de `X`.
    *   _Ejemplo_: Curso (*) - Alumno (*)

### Obligatoriedad (Opcionalidad)
Es una propiedad adicional de las asociaciones que indica si la participación de una entidad en la relación es obligatoria u opcional.

*   _Ejemplo 1: Empleado - Conyuge_
    *   Empleado (0..1) - Conyuge (1)
*   _Ejemplo 2: Persona - Automóvil_
    *   Persona (*) - Automóvil (1)
*   _Ejemplo 3: Curso - Alumno_
    *   Curso (1..*) - Alumno (1..*)

### Nombres y Roles en Asociaciones
Las asociaciones pueden llevar nombres y las entidades participantes pueden tener roles específicos.
*   _Ejemplo_: `Trabajador` **trabaja para** `Organización`
    *   Roles: `empleado` (para Trabajador), `empleador` (para Organización)

### Clases de Asociación
Una asociación puede tener atributos o comportamientos propios, lo que la convierte en una clase de asociación.
*   _Ejemplo_: Entre `Trabajador` y `Organización` existe una clase de asociación llamada `Contrato`.

### Grado de una Asociación
Se define como el número de tipos o clases de entidades que participan en una asociación.

*   **Unaria**: Una asociación que solo considera un tipo de entidad que se relaciona consigo mismo.
    *   _Ejemplo_: `Cargo` (un cargo puede ser superior o inferior a otro cargo del mismo tipo).
*   **Binaria**: Una relación conformada por dos tipos de entidades entre sí.
    *   _Ejemplo_: `Persona` (*) - `Automóvil` (1)
*   **Ternaria**: Una relación constituida por tres tipos de entidades.
    *   _Ejemplo_: `Producto` (1..*) - `Bodega` (1..*) - `Pedido` (1..*)

### Dependencia Existencial
Se refiere al hecho de que la ocurrencia de una entidad depende de la presencia de otra entidad.
*   Un objeto no puede existir sin que previamente exista otro (ej.: una Orden de Cliente no puede existir si dicho Cliente aún no existe).
*   Un objeto no puede existir si el que le da sentido es eliminado (ej.: si un Cliente es borrado, deben eliminarse todas las Órdenes de Cliente asociadas).

### Beneficios de la Dependencia Existencial
*   Garantiza la integridad referencial.
*   Facilita el acceso a la entidad dependiente.
*   Se implementa a través de claves foráneas.
*   Se manifiesta en claves primarias compuestas en "tipos de entidades débiles".

### Tiempo en Bases de Datos
Se refiere a la variación del contenido de una base de datos con respecto al tiempo.

*   **Estampilla de Tiempo**: Atributo que se incluye dentro de la descripción de una entidad para indicar el momento o intervalo de validez de los valores almacenados.
    *   _Ejemplos_: Fecha de Pago (para validez inmediata, retroactiva, futura), Fecha de Contrato.
*   **Restricciones de Inserción y Retención**:
    *   **Inserción**: Instante del tiempo en que el dato puede ser ingresado a la base de datos (antes o después de la presencia de otro dato relacionado).
    *   **Retención**: Período de tiempo en el cual tiene sentido registrar una relación.

### Unicidad
Asociado con la presencia única (o exclusiva) de un dato, objeto o relación.

*   **Unicidad por Identificador**: Un atributo que identifica de forma única una entidad.
    *   _Ejemplo_: `Persona` con `RUT {ID}` (Identificador).
*   **Exclusividad**: Mutua exclusión entre relaciones o asociaciones.
    *   _Ejemplo_: `Persona` (1..*) o `Empresa` (1..*) `Automóvil` (1) `{OR}` (exclusividad entre Persona y Empresa para poseer un automóvil).

### Herencia
Permite ver un conjunto de entidades con propiedades similares (atributos, operaciones) como un mismo tipo de entidades.

*   **Conceptos Asociados**:
    *   **Supertipo (clase)**: El tipo de entidad más general.
    *   **Subtipo (clase)**: Un subconjunto de un supertipo que ha sido dividido. Reusa las propiedades definidas en el supertipo del cual se origina.
    *   Relación del tipo "es un(a)".

*   **Propiedades de la Herencia**:
    *   **Cobertura**: Si todas las entidades del supertipo pueden ser clasificadas por, al menos, uno de los subtipos, la jerarquía de herencia tiene **cobertura completa (total, exhaustiva)**.
        *   _Ejemplo_: `Persona <<abstract>>` -> `Alumno`, `Profesor`, `Administrativo`.
    *   **Exclusividad**: Si una entidad solo puede pertenecer a uno de los subtipos a la vez, la jerarquía de herencia es **exclusiva**.
        *   _Ejemplo_: Si un alumno _puede ser_ profesor al mismo tiempo, es herencia _no exclusiva_. Si ya _no puede seguir siendo_ alumno, es herencia _exclusiva_.
    *   **Dinamicidad**: Si una entidad está asociada a uno de los subtipos y en otro momento a otro(s) subtipo(s), la jerarquía de herencia es **dinámica**.
        *   _Ejemplo_: Si un alumno pasa a ser profesor, la herencia es _dinámica_. Si nunca será el caso, herencia _no dinámica (o estática)_.

*   **Sugerencia para Diseño de Herencia**: Se sugiere unir todas las subclases obtenidas a partir de un mismo criterio hacia la superclase en cuestión.

*   **Herencia Múltiple**: Concepto donde una clase puede heredar de múltiples superclases. (A -> C, B -> C).

### Agregación
Es una colección de entidades, normalmente, de diferentes tipos.

*   **Conceptos Asociados**:
    *   **Objeto compuesto**: El que agrupa la colección.
    *   **Objeto componente**: Contenido en el objeto compuesto.
    *   Relación del tipo "(con)tiene".
*   _Ejemplos_: Cuerpo humano, computador, automóvil.

*   **Tipos de Agregación**:
    *   Compuesta (Composición): Una relación más fuerte donde el componente no puede existir sin el compuesto.
    *   Simple: Una relación más débil donde los componentes pueden existir independientemente del compuesto.

### Categorización (Interfaces)
Modela una relación de clases que tienen diferentes tipos de datos.

*   _Ejemplo_: Una `Persona` o una `Empresa` puede ser `Dueño` (rol) de una `Propiedad`.
*   **Interfaces: Ejemplo de Dependencia**:
    *   Un `Ornitorrinco` puede implementar las características de `Mamífero <<interface>>` y `Oviparo <<interface>>`.

## Conceptos Adicionales

### Restricciones a Nivel de Relaciones
Restricciones que se aplican sobre las relaciones entre entidades.

*   _Ejemplo_: `Factura` - `Detalle` `{ordenado}` (indica que los detalles de una factura están ordenados).
*   _Ejemplo_: `Persona` (1..*) `Automóvil` (1) `Empresa` (1..*) `{OR}` (Una persona o una empresa puede poseer un automóvil, pero no ambas simultáneamente para el mismo automóvil).