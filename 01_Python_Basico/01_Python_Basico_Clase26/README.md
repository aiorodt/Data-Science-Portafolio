# ✅ Clase 26 — Proyecto 4: Gestor de Tareas (To-Do List Avanzado)

## 📘 Introducción
En este proyecto desarrollarás un **Gestor de Tareas (To-Do List)** avanzado, que permitirá agregar, marcar, eliminar y guardar tareas.  
Este ejercicio refuerza la práctica de estructuras de datos, manejo de archivos y organización de funciones, emulando una pequeña aplicación de productividad real.

---

## 🎯 Objetivos de la clase
1. Aplicar estructuras de datos avanzadas (listas y diccionarios).  
2. Modularizar el código con funciones.  
3. Practicar el manejo persistente de archivos.  
4. Implementar un menú de usuario claro y funcional.  
5. Integrar conceptos de validación, filtrado y persistencia de datos.

---

## 🧠 Requisitos previos
- Conocimientos de listas, diccionarios, funciones y archivos.  
- Comprensión de `for`, `while`, `if/else` y manejo de excepciones.  
- Python 3.10+ instalado.

---

## 🧩 Descripción del proyecto
El sistema permitirá:
1. **Agregar** nuevas tareas con nombre, prioridad y estado.  
2. **Marcar** tareas como completadas.  
3. **Eliminar** tareas.  
4. **Mostrar** todas las tareas (pendientes o completadas).  
5. **Guardar y cargar** tareas desde un archivo `.csv` o `.txt`.

---

## 🧱 Estructura sugerida del proyecto

01_Python_Basico_Clase27/
│
├── main.py # Código principal del gestor de tareas
├── tareas.csv # Archivo donde se guardan las tareas
├── README.md # Documentación del proyecto
└── notas.txt # Notas e ideas de ampliación


---

## 🧰 Recomendaciones de desarrollo
- Usa una lista de diccionarios:
  ```python
  tareas = [
      {"nombre": "Estudiar Python", "prioridad": "Alta", "estado": "Pendiente"},
      {"nombre": "Comprar víveres", "prioridad": "Media", "estado": "Completada"}
  ]

- Funciones sugeridas:

- agregar_tarea()

- mostrar_tareas()

- marcar_completada()

- eliminar_tarea()

- guardar_tareas()

- cargar_tareas()

- Guarda las tareas con el módulo csv.

## 🧮 Ejemplo de interacción esperada

--- Gestor de Tareas ---

1. Agregar tarea
2. Mostrar tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Guardar y salir

Selecciona una opción: 1
Nombre de la tarea: Preparar presentación
Prioridad (Alta/Media/Baja): Alta
✅ Tarea agregada correctamente.

## 🚀 Tarea

Crea tu propio archivo main.py con el sistema completo.
Asegúrate de que:

- Las tareas se guarden y carguen correctamente.

- No se pierdan al cerrar el programa.

- Se validen las entradas del usuario.

Sube el proyecto a tu repositorio: 01_Python_Basico_Clase27/

## 📝 Extensiones opcionales

- Ordenar tareas por prioridad.

- Filtrar solo tareas pendientes.

- Mostrar estadísticas de progreso (ej. “3/5 completadas”).

- Agregar la fecha de creación de la tarea (datetime).

## 📋 Requisitos técnicos

- Python 3.10 o superior.

- Módulo csv para persistencia.

- Interfaz por consola (menú en bucle while).

## 🧩 Recursos sugeridos

- Python CSV — documentación oficial

- Guía sobre listas y diccionarios en Python