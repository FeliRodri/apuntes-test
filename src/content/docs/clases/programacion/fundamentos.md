---
title: Fundamentos de Programación
description: Conceptos básicos de programación — variables, tipos de datos, estructuras de control.
---

## Variables y Tipos de Datos

Una **variable** es un espacio en memoria que almacena un valor. En Python, no necesitas declarar el tipo:

```python
# Tipos de datos básicos
nombre = "Felipe"        # str  - Cadena de texto
edad = 21                # int  - Número entero
promedio = 8.5            # float - Número decimal
activo = True             # bool - Verdadero/Falso
```

### Tipos de datos principales

| Tipo | Ejemplo | Descripción |
|------|---------|-------------|
| `str` | `"Hola"` | Cadenas de texto |
| `int` | `42` | Números enteros |
| `float` | `3.14` | Números decimales |
| `bool` | `True` / `False` | Valores lógicos |
| `list` | `[1, 2, 3]` | Listas (mutables) |
| `tuple` | `(1, 2, 3)` | Tuplas (inmutables) |
| `dict` | `{"key": "val"}` | Diccionarios |

## Estructuras de Control

### Condicionales

```python
nota = 85

if nota >= 90:
    print("Excelente - A")
elif nota >= 80:
    print("Muy bien - B")
elif nota >= 70:
    print("Bien - C")
else:
    print("Necesitas mejorar")
```

### Ciclo `for`

```python
# Iterar sobre una lista
materias = ["Programación", "Matemáticas", "Física"]

for materia in materias:
    print(f"Cursando: {materia}")

# Iterar con range
for i in range(1, 6):
    print(f"Iteración {i}")
```

### Ciclo `while`

```python
contador = 0

while contador < 5:
    print(f"Contando: {contador}")
    contador += 1
```

## Funciones

Las funciones permiten **reutilizar código**:

```python
def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas."""
    return sum(notas) / len(notas)

# Uso
mis_notas = [85, 90, 78, 92]
resultado = calcular_promedio(mis_notas)
print(f"Promedio: {resultado}")  # Promedio: 86.25
```

:::tip[Buena práctica]
Siempre documenta tus funciones con **docstrings** para que otros (y tú en el futuro) entiendan qué hacen.
:::
