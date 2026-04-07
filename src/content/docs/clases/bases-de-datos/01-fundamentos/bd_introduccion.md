---
title: Introducción a Bases de Datos
description: Conceptos fundamentales de bases de datos, modelos y sistemas gestores.
---

## ¿Qué es una Base de Datos?

Una **base de datos** es una colección organizada de datos que se almacenan y acceden de forma electrónica. Permite guardar, consultar, modificar y eliminar información de manera eficiente.

## Tipos de Bases de Datos

### Relacionales (SQL)
Organizan datos en **tablas** relacionadas entre sí:

| SGBD | Descripción | Uso común |
|------|------------|-----------|
| **MySQL** | Open source, muy popular | Aplicaciones web |
| **PostgreSQL** | Avanzado, extensible | Proyectos complejos |
| **SQLite** | Embebido, sin servidor | Apps móviles, prototipos |
| **SQL Server** | Microsoft, empresarial | Corporaciones |

### No Relacionales (NoSQL)
Almacenan datos en formatos flexibles:

| Tipo | Ejemplo | Formato |
|------|---------|---------|
| **Documentos** | MongoDB | JSON/BSON |
| **Clave-Valor** | Redis | Key → Value |
| **Grafos** | Neo4j | Nodos y aristas |
| **Columnar** | Cassandra | Columnas |

## Modelo Relacional

### Conceptos clave

- **Tabla (Relación)**: Estructura que almacena datos en filas y columnas
- **Registro (Fila/Tupla)**: Una entrada de datos
- **Campo (Columna/Atributo)**: Una propiedad del dato
- **Clave Primaria (PK)**: Identifica de forma única cada registro
- **Clave Foránea (FK)**: Relaciona dos tablas entre sí

### Ejemplo de tabla

```
┌─────────────────────────────────────────┐
│              ESTUDIANTES                │
├─────┬──────────┬─────────┬──────────────┤
│ ID  │ Nombre   │ Edad    │ Carrera      │
├─────┼──────────┼─────────┼──────────────┤
│ 1   │ Felipe   │ 21      │ Ing. Software│
│ 2   │ María    │ 22      │ Ing. Sistemas│
│ 3   │ Carlos   │ 20      │ Ing. Software│
└─────┴──────────┴─────────┴──────────────┘
  PK
```

## Normalización

La normalización reduce la **redundancia** de datos:

1. **1FN**: Eliminar grupos repetitivos, valores atómicos
2. **2FN**: Cumplir 1FN + eliminar dependencias parciales
3. **3FN**: Cumplir 2FN + eliminar dependencias transitivas

:::tip[Regla práctica]
_"Cada campo debe depender de la clave, de toda la clave, y nada más que la clave."_
:::
