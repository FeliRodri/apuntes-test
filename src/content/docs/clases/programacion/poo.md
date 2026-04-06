---
title: Programación Orientada a Objetos
description: Clases, objetos, herencia, polimorfismo y encapsulamiento.
---

## ¿Qué es la POO?

La **Programación Orientada a Objetos** es un paradigma que organiza el código en **objetos** que contienen datos (atributos) y comportamiento (métodos).

### Pilares de la POO

1. **Encapsulamiento** — Ocultar datos internos
2. **Herencia** — Reutilizar código de una clase padre
3. **Polimorfismo** — Mismo método, diferente comportamiento
4. **Abstracción** — Simplificar la complejidad

## Clases y Objetos

```python
class Estudiante:
    """Representa a un estudiante universitario."""

    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        self.materias = []
        self.__promedio = 0.0  # atributo privado

    def inscribir_materia(self, materia):
        """Inscribe al estudiante en una materia."""
        self.materias.append(materia)
        print(f"{self.nombre} inscrito en {materia}")

    def mostrar_info(self):
        """Muestra la información del estudiante."""
        print(f"Nombre: {self.nombre}")
        print(f"Carrera: {self.carrera}")
        print(f"Materias: {', '.join(self.materias)}")

# Crear un objeto
felipe = Estudiante("Felipe", "Ingeniería en Software")
felipe.inscribir_materia("Programación")
felipe.inscribir_materia("Base de Datos")
felipe.mostrar_info()
```

## Herencia

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre}"

class Profesor(Persona):
    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self.departamento = departamento

    def saludar(self):  # Polimorfismo
        return f"Hola, soy el Prof. {self.nombre} del depto. de {self.departamento}"

class Alumno(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula

    def saludar(self):  # Polimorfismo
        return f"Hola, soy {self.nombre}, matrícula: {self.matricula}"
```

## Diagrama de Clases

```
┌──────────────┐
│   Persona    │
├──────────────┤
│ - nombre     │
│ - edad       │
├──────────────┤
│ + saludar()  │
└──────┬───────┘
       │
  ┌────┴────┐
  │         │
┌─▼──────┐ ┌▼────────┐
│Profesor│ │ Alumno  │
├────────┤ ├─────────┤
│- depto │ │-matríc. │
├────────┤ ├─────────┤
│+saludar│ │+saludar │
└────────┘ └─────────┘
```

:::note[Recuerda]
La herencia permite **reutilizar** código, pero no abuses de ella. Prefiere la **composición** sobre la herencia cuando sea posible.
:::
