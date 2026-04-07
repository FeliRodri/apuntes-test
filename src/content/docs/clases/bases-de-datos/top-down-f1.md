---
title: Top-Down Model (Caso F1)
description: Análisis de requisitos mediante el enfoque Top-Down para el sistema de gestión de campeonatos de F1.
---

Esta sección documenta el análisis de requisitos mediante el enfoque **Top-Down** para el sistema de gestión de campeonatos de F1.

## Consulta Original

> **Ejercicio Propuesto: Campeonato de Fórmula 1**
> En un campeonato mundial de carreras de fórmula 1, es posible identificar los siguientes hechos y eventos:
>
> Los pilotos firman contratos para correr durante una temporada en los autos de una escudería. Por ésta pueden firmar contrato varios pilotos. La escudería debe tener al menos un piloto y debe pertenecer a un país; notar que cada país puede tener varias escuderías.
> Los automóviles deben estar inscritos en una escudería para poder participar. Estos son asignados a los pilotos para una carrera en particular, dependiendo si están disponibles técnicamente. Un piloto puede usar sólo un automóvil durante una carrera. La participación de un piloto en una carrera exige que se le tenga asignado un automóvil.
> En una temporada se realizan muchas carreras en circuitos existentes en los distintos países. En un mismo circuito pueden desarrollarse varias carreras (en una misma o distintas temporadas). Además, un circuito puede estar en reparaciones y no tener carreras programadas.

---

## Análisis Top-Down

El modelado **Top-Down** descompone el problema desde las definiciones globales hacia los detalles técnicos. A continuación, se detallan las capas del modelo:

## 1. Entidades Principales (Sustantivos)

Las piezas de información fundamentales identificadas en el caso son:

- **País**: Entidad geográfica de origen.
- **Escudería**: Organización deportiva.
- **Piloto**: Profesional que compite.
- **Automóvil**: Activo técnico de la escudería.
- **Circuito**: Ubicación física de la carrera.
- **Carrera**: Evento específico en una temporada.

## 2. Reglas de Negocio y Cardinalidad

A partir del texto, establecemos las restricciones del modelo:

### Jerarquía Organizacional

- **País - Escudería**: Relación $1:N$. Un país puede tener múltiples escuderías, pero una escudería pertenece a un solo país.
- **Escudería - Piloto**: Relación $1:N$. Una escudería debe tener al menos un piloto ($1..*$).

### Operación de Carrera

- **Circuito - Carrera**: Relación $1:N$ opcional. Un circuito puede albergar muchas carreras o ninguna (si está en reparación).
- **Piloto - Auto - Carrera**: Se identifica una **relación ternaria**. La asignación del auto al piloto es única por cada carrera específica.

## 3. Propuesta de Esquema Lógico

Para implementar este modelo, las tablas quedarían relacionadas de la siguiente manera:

| Entidad           | Atributos Clave (Ejemplos)           | Relación (FK)       |
| :---------------- | :----------------------------------- | :------------------ |
| **Pais**          | `id_pais`, `nombre`                  | -                   |
| **Escuderia**     | `id_escuderia`, `nombre`             | `id_pais`           |
| **Piloto**        | `id_piloto`, `nombre`                | `id_escuderia`      |
| **Automovil**     | `id_auto`, `modelo`                  | `id_escuderia`      |
| **Circuito**      | `id_circuito`, `nombre`              | `id_pais`           |
| **Carrera**       | `id_carrera`, `fecha`, `temporada`   | `id_circuito`       |
| **Participacion** | `id_piloto`, `id_carrera`, `id_auto` | _(Clave compuesta)_ |

---

:::tip[Punto clave del método Top-Down]
Nota que en este análisis priorizamos la **lógica del negocio** (quién pertenece a quién) antes de definir si un campo es de tipo texto o numérico. Esto asegura que el modelo final refleje fielmente la realidad del Campeonato de F1.
:::
