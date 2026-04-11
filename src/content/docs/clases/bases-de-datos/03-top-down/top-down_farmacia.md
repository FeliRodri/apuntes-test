---
title: "Modelamiento Top-Down: Caso Farmacia"
description: "Resolución paso a paso del modelo relacional para el sistema de gestión de una farmacia utilizando el método Top-Down."
---

Esta sección documenta el análisis de requisitos y la transformación del modelo conceptual al modelo relacional para un sistema de gestión de farmacias, aplicando las reglas formales del diseño **Top-Down**.

## Descripción del Problema

:::note[Contexto del Ejercicio]
Una alta concurrencia de clientes han tenido en el último tiempo las farmacias. En cada farmacia es posible encontrar diversos productos (medicamentos, cuidado para la salud, perfumería, alimenticios); de cada uno se registra nombre, marca, tipo de medida, fecha de vencimiento y stock, además del **precio que cambia en el tiempo**.

En el caso de **medicamentos**, es posible que se necesite una receta médica. Existen medicamentos de marca y **bioequivalentes**, pudiendo ser producidos por laboratorios distintos.

En la venta, es posible acceder a descuentos por **convenios** del cliente. El descuento varía el precio de la venta. Además, pueden haber **promociones especiales** según tipo de producto o forma de pago.
:::

---

## 1. Pasos Utilizados en la Transformación

A partir del análisis del problema, se aplicaron las siguientes reglas de transformación Top-Down:

### Paso 1: Tipos de Entidades Fuertes

Se crearon relaciones independientes para los objetos principales, definiendo sus Claves Primarias (PK).

- `TIPO_PRODUCTO` (PK: id_tipo)
- `LABORATORIO` (PK: id_laboratorio)
- `CLIENTE` (PK: id_cliente)
- `CONVENIO` (PK: id_convenio)
- `FORMA_PAGO` (PK: id_forma_pago)
- `PROMOCION` (PK: id_promocion)
- `VENTA` (PK: id_venta)

### Paso 7: Herencia (Alternativa 1)

Existe una jerarquía donde `PRODUCTO` es la superclase y `MEDICAMENTO` es la subclase.

- Se mantiene la tabla `PRODUCTO` con los atributos generales.
- Se crea la tabla `MEDICAMENTO` con sus atributos propios (receta) y el identificador de la superclase (`id_producto`) como PK/FK.

### Paso 2: Tipos de Entidades Débiles

El "precio que cambia en el tiempo" genera una dependencia histórica.

- Se crea `HISTORIAL_PRECIO`. Su PK es la concatenación de la clave de la entidad fuerte (`id_producto`) y un atributo diferenciador (`fecha_inicio`).

### Paso 4: Asociaciones 1:N

La entidad en el lado de los "muchos" recibe la Clave Foránea (FK) de la entidad "uno":

- `PRODUCTO` recibe `id_tipo`.
- `VENTA` recibe `id_cliente` e `id_forma_pago`.
- `MEDICAMENTO` recibe `id_laboratorio`.

### Paso 5: Asociaciones M:N

Se crearon tablas intermedias para las relaciones de muchos a muchos:

- **Venta - Producto:** Crea `DETALLE_VENTA`.
- **Cliente - Convenio:** Crea `CLIENTE_CONVENIO`.
- **Medicamento (Marca) - Medicamento (Bioequivalente):** Crea `EQUIVALENCIA` (Relación recursiva/reflexiva).

---

## 2. Alternativas No Utilizadas

:::caution[Justificación de diseño]
Para mantener la integridad del modelo, se descartaron los siguientes pasos del apunte oficial:

- **Paso 3 (Asociaciones 1:1):** No presentes en la lógica de negocio.
- **Paso 6 (Asociaciones n-arias):** Los descuentos se resolvieron secuencialmente sin necesidad de relaciones ternarias complejas.
- **Paso 7 (Herencia Alt. 2, 3 y 4):** Descartadas para evitar tablas monolíticas llenas de valores nulos (ej. atributos de medicamentos aplicados erróneamente a un champú).
- **Paso 8 (Categorización):** No existen superclases con identificadores distintos que requieran unificación.
:::

---

## 3. Esquema Relacional Final

El modelo lógico resultante, optimizado para el motor de base de datos, es el siguiente:

| Tabla                | Clave Primaria `{PK}`                  | Claves Foráneas `{FK}` y Atributos Simples                         |
| :------------------- | :------------------------------------- | :----------------------------------------------------------------- |
| **TIPO_PRODUCTO**    | `id_tipo`                              | nombre_tipo                                                        |
| **LABORATORIO**      | `id_laboratorio`                       | nombre                                                             |
| **CLIENTE**          | `id_cliente`                           | rut, nombre                                                        |
| **CONVENIO**         | `id_convenio`                          | descripcion_convenio                                               |
| **FORMA_PAGO**       | `id_forma_pago`                        | tipo_pago                                                          |
| **PRODUCTO**         | `id_producto`                          | nombre, marca, tipo_medida, fecha_vto, stock, `id_tipo` {FK}       |
| **MEDICAMENTO**      | `id_producto` {FK}                     | receta_obligada, receta_retenida, `id_laboratorio` {FK}            |
| **HISTORIAL_PRECIO** | `id_producto` {FK}, `fecha`            | precio_vigente                                                     |
| **EQUIVALENCIA**     | `id_med_marca` {FK}, `id_med_bio` {FK} | _(Unión de medicamentos)_                                          |
| **PROMOCION**        | `id_promocion`                         | porcentaje_dscto, dia_aplica, `id_tipo` {FK}, `id_forma_pago` {FK} |
| **CLIENTE_CONVENIO** | `id_cliente` {FK}, `id_convenio` {FK}  | estado_vigencia                                                    |
| **VENTA**            | `id_venta`                             | fecha, `id_cliente` {FK}, `id_forma_pago` {FK}                     |
| **DETALLE_VENTA**    | `id_venta` {FK}, `id_producto` {FK}    | cantidad, precio_final_aplicado                                    |

:::tip[Buenas Prácticas]
El campo `precio_final_aplicado` en la tabla `DETALLE_VENTA` asegura que, aunque el precio histórico cambie o el convenio expire, el registro contable de la transacción se mantenga inalterable con el valor exacto que el cliente pagó ese día.
:::
