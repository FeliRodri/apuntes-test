---
title: Clase introduccion a la estadistica
description: Estadistica Aplicada 01
---

## Introducción a la Estadística

### Definición y Reseña Histórica

La estadística es la ciencia del estado. Comprende un conjunto de conceptos y técnicas para la recopilación, presentación e interpretación de la información, con el fin de aportar al análisis de datos y al proceso de toma de decisiones.

Su desarrollo fue impulsado por:
*   La demanda de gobiernos, empresas e instituciones para recopilar información.
*   El desarrollo de las matemáticas en la teoría de la probabilidad.

Desde civilizaciones antiguas como las Egipcias, Griegas y Romanas, ya existían prácticas de recolección de datos con fines impositivos y militares. Durante la Edad Media, las instituciones eclesiásticas registraban datos de nacimientos, muertes y matrimonios.

### Objetivos de la Estadística

La estadística se divide en dos ramas principales:

*   **Estadística Descriptiva**:
    *   Objetivo: Describir cuantitativamente una serie de personas, lugares o cosas.
    *   Métodos: Implican recopilación, presentación y caracterización de un conjunto de datos.
*   **Inferencia Estadística**:
    *   Objetivo: Obtener conclusiones acerca de un grupo grande de personas, lugares o cosas, a partir de la observación de solo una pequeña parte del conjunto total.
    *   Fundamento: Teoría de probabilidades.

## Conceptos Fundamentales

### Población o Universo

*   Conjunto de individuos o elementos a los que se les puede observar o medir una característica o atributo.
*   Es todo conjunto de elementos, finito o infinito, definido por una o más características que todos sus componentes poseen.

### Muestra

*   Proporción de la población que se considera para el análisis.
*   Conjunto de elementos o individuos que reúne aproximadamente las características de la población importantes para una investigación.

### Parámetro

*   Variable que representa a una familia de elementos.
*   Medidas o datos que se obtienen para describir una característica de una población determinada.

### Estadístico, Estadígrafo o Estimación

*   Datos o medidas que se obtienen sobre una muestra y que sirven como estimación de los parámetros poblacionales.

:::tip[En Resumen]
*   **Estadística Descriptiva**: Describir cuantitativamente.
*   **Inferencia Estadística**: Creación de modelos matemáticos para la toma de decisiones.
*   **Población**: El todo.
*   **Muestra**: Una parte del todo.
*   **Parámetro**: Medida de la población.
*   **Estadístico/Estimador**: Medida de la muestra, usada para estimar el parámetro.
:::

## Variables Estadísticas y su Clasificación

### Definiciones

*   **Variable**: Característica de las unidades que interesa estudiar en una investigación científica.
*   **Variable Aleatoria**: Si los valores numéricos que asume una variable provienen de factores fortuitos y no se pueden predecir exactamente con anticipación.

Representación:
*   Variables aleatorias: Letras mayúsculas (X, Y, Z).
*   Realización de la variable aleatoria (valores específicos): Letras minúsculas (x, y, z).
    *   Ej: Si X tiene 6 valores, se denotan como x1, x2, x3, x4, x5, x6.

### Tipos de Datos y Variables Aleatorias

Las variables aleatorias proporcionan dos clases de datos:

*   **Datos Cualitativos**: Producen respuestas categóricas (miden cualidades).
    *   **Nominales**: Los datos se agrupan sin ninguna jerarquía. No tienen orden inherente.
        *   Ej: Nombres de personas, raza, grupos sanguíneos, estado civil.
    *   **Ordinales**: Las categorías o valores poseen un orden, secuencia o progresión natural. A pesar del orden jerárquico, no es posible obtener una valoración numérica lógica entre dos valores.
        *   Ej: Grados de desnutrición, respuesta a un tratamiento, nivel socioeconómico.
*   **Datos Cuantitativos**: Entregan respuestas numéricas.
    *   **Discretas**: Respuestas numéricas producto de un proceso de conteo. Asumen un conjunto finito o infinito numerable de valores.
    *   **Continuas**: Respuestas numéricas producto de un proceso de medición. Asumen valores de un conjunto infinito no numerable.

:::note
Tanto las variables discretas como las continuas pueden agruparse en intervalos. Sin embargo, estrictamente, solo las variables continuas pueden ser objeto de categorización mediante intervalos.
:::

## Medidas Descriptivas

### Medidas de Tendencia Central

Nos indican hacia dónde tienden a agruparse los datos.

*   **Moda**:
    *   Valor que aparece con mayor frecuencia en un conjunto de datos.
    *   Puede ser unimodal, bimodal o multimodal.
*   **Media Aritmética o Promedio** ($\bar{X}$):
    *   Representa un "punto de equilibrio" del conjunto de datos.
    *   Fórmula:
        $$ \bar{X} = \frac{\sum_{i=1}^{n} x_i}{n} $$
    *   Propiedades:
        *   Promedio de un conjunto de observaciones sumando una constante ($k$):
            $$ \overline{X+k} = \bar{X} + k $$
        *   Promedio de un conjunto de observaciones multiplicando por una constante ($k$):
            $$ \overline{kX} = k\bar{X} $$
*   **Mediana (Md)**:
    *   Corresponde al valor central del conjunto de datos una vez que estos han sido ordenados.

### Medidas de Dispersión

Nos indican el grado de variabilidad en torno a un valor central.

*   **Varianza ($s^2$)**:
    *   "Promedio" de las distancias cuadráticas entre cada observación con respecto a su media.
    *   Fórmula:
        $$ s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{X})^2}{n - 1} $$
*   **Desviación Estándar ($s$)**:
    *   Raíz cuadrada de la varianza. Es el promedio de distancias de cada observación con respecto a la media.
    *   Fórmula:
        $$ s = \sqrt{s^2} $$
*   **Rango ($R$)**:
    *   Diferencia entre el mayor y el menor valor del conjunto de datos.
    *   Fórmula:
        $$ R = X_{\text{max}} - X_{\text{min}} $$
*   **Coeficiente de Variación ($C.V.$)**:
    *   Medida relativa de dispersión; mide la dispersión de los datos en torno a la media.
    *   Fórmula:
        $$ C.V. = \left( \frac{s}{\bar{X}} \right) \cdot 100\% $$
    *   **Nota**: A menor valor de $C.V.$, más homogénea es la distribución de los datos.

### Medidas de Posición

Útiles para resumir propiedades de grandes cantidades de datos cuantitativos. Se les denomina cuantiles.

*   **Percentiles ($P_p$)**:
    *   Dividen un conjunto ordenado de observaciones en cien partes.
    *   El percentil `p` corresponde al valor que deja bajo sí el `p%` del total de observaciones y sobre sí el `(100 - p)%`.
    *   Fórmula para la posición: $$ \text{Posición} = \frac{p \cdot n}{100} $$ (donde $p$ es el percentil deseado, y $n$ el número total de observaciones).
    *   Obs.: $0 < p < 100$.
*   **Deciles ($D_p$)**:
    *   Dividen un conjunto ordenado de observaciones en diez partes.
    *   El decil `p` corresponde al valor que deja bajo sí el `p%` del total de observaciones y sobre sí el `(100 - p)%`.
    *   Fórmula para la posición: $$ \text{Posición} = \frac{p \cdot n}{10} $$
    *   Obs.: $0 < p < 10$.
*   **Quintiles ($Q_p$)**:
    *   Dividen un conjunto ordenado de observaciones en cinco partes.
    *   El quintil `p` corresponde al valor que deja bajo sí el `p%` del total de observaciones y sobre sí el `(100 - p)%`.
    *   Fórmula para la posición: $$ \text{Posición} = \frac{p \cdot n}{5} $$
    *   Obs.: $0 < p < 5$.
*   **Cuartiles ($C_p$)**:
    *   Dividen un conjunto ordenado de observaciones en cuatro partes.
    *   El cuartil `p` corresponde al valor que deja bajo sí el `p%` del total de observaciones y sobre sí el `(100 - p)%`.
    *   Fórmula para la posición: $$ \text{Posición} = \frac{p \cdot n}{4} $$
    *   Obs.: $0 < p < 4$.

:::tip[Relaciones Importantes]
La Mediana ($Md$) es equivalente al Percentil 50 ($P_{50}$), al Decil 5 ($D_5$) y al Cuartil 2 ($C_2$).
:::

## Correlación

Mide el grado de asociación LINEAL entre dos variables.

*   Puede ser **negativa o decreciente**: Cuando una variable aumenta, la otra tiende a disminuir.
*   Puede ser **positiva o creciente**: Cuando una variable aumenta, la otra también tiende a aumentar.

La correlación se relaciona con la "pendiente" de una "recta" asociada a los datos, indicando si esta pendiente es negativa o positiva.

El coeficiente de correlación siempre estará entre -1 y 1.

*   Una correlación de 1 significa una alta correlación positiva entre las variables.
*   Una correlación cercana a -1 significa una alta correlación negativa.
*   Una correlación cercana a 0 significa poca o ninguna relación lineal.

### Estimación de la Correlación Poblacional

Así como la media poblacional es un parámetro estimado por el promedio muestral ($\bar{X}$), la correlación poblacional (ρ) es un parámetro que tiene un estimador puntual para una muestra, denotado por `r`.

### Ejemplo de Aplicación

Un profesor de Estadística desea determinar la relación entre las calificaciones de un examen final y un proyecto. Se toma una muestra aleatoria de calificaciones. El objetivo es hallar e interpretar el coeficiente de correlación entre estas dos variables.

:::tip[Tarea]
**En parejas:**
1.  Seleccionar al menos dos variables asociadas a la enfermedad COVID-19 que consideren lógicamente relacionadas.
2.  Recopilar al menos 30 pares de valores o períodos de información para estas variables.
3.  **Definir los tipos de variables** seleccionadas.
4.  **Calcular**: Moda, Media, Mediana para cada variable. Desviación Estándar, Varianza, Coeficiente de Variación para cada variable. Percentiles para cada variable.
5.  **Calcular el coeficiente de correlación** entre las dos variables. (Se puede usar Excel para los cálculos).
6.  Realizar una **interpretación** detallada de todos los resultados obtenidos.

**Evaluación:** 30% numérico (cálculos); 70% interpretación.
:::

## Recursos Adicionales

*   **Población y Muestra**: [https://www.youtube.com/watch?v=gl9EEbT7viM](https://www.youtube.com/watch?v=gl9EEbT7viM)
*   **Parámetro versus Muestra**: [https://www.youtube.com/watch?v=nh7KWBGWwrI](https://www.youtube.com/watch?v=nh7KWBGWwrI)
*   **Tipos de Variables**:
    *   [https://www.youtube.com/watch?v=Tb3sgUSd2SQ](https://www.youtube.com/watch?v=Tb3sgUSd2SQ)
    *   [https://www.youtube.com/watch?v=sQ08tqf-rXU](https://www.youtube.com/watch?v=sQ08tqf-rXU)
*   **Medidas de Tendencia Central**: [https://www.youtube.com/watch?v=jiceVfALmV0](https://www.youtube.com/watch?v=jiceVfALmV0)
*   **Medidas de Dispersión**: [https://www.youtube.com/watch?v=oZRaDwnpXkY](https://www.youtube.com/watch?v=oZRaDwnpXkY)
*   **Correlación Lineal**: [https://www.youtube.com/watch?v=1o_qbkzYyVk](https://www.youtube.com/watch?v=1o_qbkzYyVk)