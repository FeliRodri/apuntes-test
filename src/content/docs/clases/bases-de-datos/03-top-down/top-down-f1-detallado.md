---
title: Top-Down Model Detallado (Caso F1)
description: Explicación exhaustiva del modelo Top-Down aplicado al Campeonato de Fórmula 1, detallando minuciosamente las reglas de diseño y transformación utilizadas y omitidas.
---

Excelente material analítico de la Universidad Técnica Federico Santa María. Aplicar las reglas formales de transformación dictadas en el documento es la forma correcta de pasar de un modelo conceptual a un modelo relacional (Diseño Lógico) bajo el esquema Top-Down.

A continuación, desglosaremos la solución del Campeonato de Fórmula 1 indicando exactamente qué pasos del apunte se utilizaron y cuáles se omitieron, incluyendo el detalle de las alternativas.

---

## ✅ Pasos UTILIZADOS en el Ejercicio

Para modelar este problema, asumimos un modelo conceptual previo con las entidades principales detectadas en el texto. Las reglas aplicadas son:

### **Paso 1: Tipos de Entidades "fuertes"** 
* **Regla aplicada:** Por cada entidad fuerte, creamos una relación (tabla) que incluya sus atributos simples y escogemos un atributo como Clave Primaria (PK).
* **Entidades detectadas:**
    * `PAIS` (PK: id_pais)
    * `ESCUDERIA` (PK: id_escuderia)
    * `PILOTO` (PK: id_piloto)
    * `AUTOMOVIL` (PK: id_auto)
    * `CIRCUITO` (PK: id_circuito)
    * `CARRERA` (PK: id_carrera)
    * `TEMPORADA` (PK: id_temporada)

### **Paso 4: Asociaciones 1:N** 
* **Regla aplicada:** Identificamos la relación en el lado de los "muchos" (N) e incluimos como Clave Foránea (FK) la clave primaria de la entidad con cardinalidad 1.
* **Aplicación en el problema:**
    * *País (1) - Escudería (N)*: La relación `ESCUDERIA` recibe la FK `id_pais`.
    * *Escudería (1) - Automóvil (N)*: La relación `AUTOMOVIL` recibe la FK `id_escuderia`.
    * *Escudería (1) - Piloto (N)*: La relación `PILOTO` recibe la FK `id_escuderia`. *(Asumiendo el contrato vigente)*.
    * *País (1) - Circuito (N)*: La relación `CIRCUITO` recibe la FK `id_pais`.
    * *Circuito (1) - Carrera (N)*: La relación `CARRERA` recibe la FK `id_circuito`.
    * *Temporada (1) - Carrera (N)*: La relación `CARRERA` recibe la FK `id_temporada`.

### **Paso 6: Asociaciones n-arias ($n\ge3$)**
* **Regla aplicada:** Se crea una nueva relación para representarla, incluyendo como Claves Foráneas las claves primarias de las entidades participantes. La concatenación de estas suele ser la PK.
* **Aplicación en el problema:** El texto indica: *"Estos [automóviles] son asignados a los pilotos para una carrera en particular"*. Esto es una **asociación ternaria** entre Piloto, Automóvil y Carrera.
    * Creamos la relación `PARTICIPACION`.
    * Tendrá las FK: `id_piloto`, `id_auto`, `id_carrera`.

---

## ❌ Pasos y Alternativas NO UTILIZADOS

Dado el alcance de los requisitos del problema de Fórmula 1, las siguientes reglas del documento no fueron necesarias:

* **Paso 2: Tipos de Entidades "débiles"**. No se utilizó porque todas las entidades identificadas poseen un identificador propio independiente de otra entidad. No hubo necesidad de concatenar identificadores para asegurar unicidad.
* **Paso 3: Asociaciones 1:1**. No se detectaron relaciones uno a uno en la descripción.
* **Paso 5: Asociaciones M:N**. No se utilizó de forma directa. *(Nota: Si el "Contrato" se modelara como un historial donde un piloto está en muchas escuderías a lo largo de los años y una escudería tiene muchos pilotos, aplicaría este paso. Para simplificar la temporada actual, usamos el Paso 4).*
* **Paso 8: Categorización (Interfaces)**. No se utilizó porque no hay superclases con identificadores distintos que requieran crear una clave sustituta.

### **Detalle: Paso 7 (Herencia) NO UTILIZADO** 
El problema no menciona ninguna jerarquía de clases (por ejemplo, no se diferencia entre "Pilotos Titulares" y "Pilotos de Prueba", o "Circuitos Callejeros" y "Circuitos Cerrados"). Por ende, **no se utilizó ninguna de sus 4 alternativas**:
1.  **No se usó la Alternativa 1:** La cual mantendría una tabla para la superclase y tablas separadas para cada subclase (incluyendo el identificador de la superclase).
2.  **No se usó la Alternativa 2:** La cual habría eliminado la tabla de la superclase, dejando solo tablas por subclase que contengan todos los atributos heredados.
3.  **No se usó la Alternativa 3:** La cual fusionaría todo en una sola relación global con un atributo discriminador (ej. "Tipo?") para indicar la subclase correspondiente.
4.  **No se usó la Alternativa 4:** Similar a la anterior, la cual fusionaría todo pero usando múltiples atributos de tipo booleano para definir a qué subclase pertenece el registro.

---

## Resultado Final (Esquema Relacional)

Aplicando estrictamente los pasos 1, 4 y 6, el modelo resultante es:

* **PAIS** (`id_pais` {PK}, nombre_pais)
* **TEMPORADA** (`id_temporada` {PK}, año)
* **ESCUDERIA** (`id_escuderia` {PK}, nombre, `id_pais` {FK})
* **PILOTO** (`id_piloto` {PK}, nombre, `id_escuderia` {FK})
* **AUTOMOVIL** (`id_auto` {PK}, modelo, disponible_tecnicamente, `id_escuderia` {FK})
* **CIRCUITO** (`id_circuito` {PK}, nombre, en_reparaciones, `id_pais` {FK})
* **CARRERA** (`id_carrera` {PK}, fecha, `id_circuito` {FK}, `id_temporada` {FK})
* **PARTICIPACION** (`id_piloto` {PK}{FK}, `id_carrera` {PK}{FK}, `id_auto` {FK})
