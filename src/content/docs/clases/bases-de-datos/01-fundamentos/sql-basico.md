---
title: SQL Básico
description: Consultas fundamentales de SQL — SELECT, INSERT, UPDATE, DELETE.
---

## ¿Qué es SQL?

**SQL** (Structured Query Language) es el lenguaje estándar para interactuar con bases de datos relacionales. Permite crear, consultar, modificar y eliminar datos.

## Crear una tabla

```sql
CREATE TABLE estudiantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    carrera VARCHAR(100),
    promedio DECIMAL(3,1),
    fecha_ingreso DATE DEFAULT CURRENT_DATE
);
```

## Operaciones CRUD

### CREATE — Insertar datos

```sql
-- Insertar un registro
INSERT INTO estudiantes (nombre, email, carrera, promedio)
VALUES ('Felipe', 'felipe@uni.edu', 'Ing. Software', 8.5);

-- Insertar múltiples registros
INSERT INTO estudiantes (nombre, email, carrera, promedio) VALUES
    ('María', 'maria@uni.edu', 'Ing. Sistemas', 9.2),
    ('Carlos', 'carlos@uni.edu', 'Ing. Software', 7.8),
    ('Ana', 'ana@uni.edu', 'Ing. Datos', 9.0);
```

### READ — Consultar datos

```sql
-- Seleccionar todo
SELECT * FROM estudiantes;

-- Seleccionar columnas específicas
SELECT nombre, carrera, promedio FROM estudiantes;

-- Filtrar con WHERE
SELECT * FROM estudiantes WHERE carrera = 'Ing. Software';

-- Ordenar resultados
SELECT * FROM estudiantes ORDER BY promedio DESC;

-- Limitar resultados
SELECT * FROM estudiantes LIMIT 5;

-- Contar registros
SELECT COUNT(*) AS total FROM estudiantes;

-- Promedio por carrera
SELECT carrera, AVG(promedio) AS promedio_carrera
FROM estudiantes
GROUP BY carrera
HAVING AVG(promedio) > 8.0;
```

### UPDATE — Modificar datos

```sql
-- Actualizar un campo
UPDATE estudiantes
SET promedio = 9.0
WHERE nombre = 'Felipe';

-- Actualizar múltiples campos
UPDATE estudiantes
SET carrera = 'Ing. Datos', promedio = 8.8
WHERE id = 3;
```

### DELETE — Eliminar datos

```sql
-- Eliminar un registro
DELETE FROM estudiantes WHERE id = 4;

-- ⚠️ NUNCA hagas esto sin WHERE
-- DELETE FROM estudiantes;  -- ¡Borra TODO!
```

:::caution[¡Cuidado!]
Siempre usa `WHERE` en `UPDATE` y `DELETE`. Sin la cláusula `WHERE`, la operación afecta a **todos** los registros de la tabla.
:::

## JOINs — Unir tablas

```sql
-- Consultar estudiantes con sus materias
SELECT e.nombre, m.nombre_materia, i.nota
FROM estudiantes e
INNER JOIN inscripciones i ON e.id = i.estudiante_id
INNER JOIN materias m ON i.materia_id = m.id;
```

### Tipos de JOIN

| Tipo | Descripción |
|------|-------------|
| `INNER JOIN` | Solo registros que coinciden en ambas tablas |
| `LEFT JOIN` | Todos los de la izquierda + coincidencias |
| `RIGHT JOIN` | Todos los de la derecha + coincidencias |
| `FULL JOIN` | Todos los registros de ambas tablas |

## Resumen rápido

| Operación | Comando SQL | Descripción |
|-----------|-------------|-------------|
| Crear | `INSERT INTO` | Agregar nuevos registros |
| Leer | `SELECT` | Consultar datos |
| Actualizar | `UPDATE` | Modificar registros existentes |
| Eliminar | `DELETE` | Borrar registros |
