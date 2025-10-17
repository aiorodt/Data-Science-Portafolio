# 🎓 Clase 25 — Proyecto 2: Sistema de Registro de Estudiantes

## 📘 Introducción
En esta clase desarrollarás tu **segundo proyecto práctico**, aplicando conceptos de:
- **Listas** y **diccionarios**
- **Manejo de archivos** (`.txt` o `.csv`)
- **Control de flujo** y **funciones**

El propósito es crear un **Sistema de Registro de Estudiantes** capaz de almacenar, consultar y listar información básica de alumnos, guardando los datos de forma persistente en un archivo externo.

---

## 🎯 Objetivos de la clase
1. Practicar la combinación de **listas, diccionarios y archivos**.  
2. Implementar un sistema con **menú interactivo**.  
3. Aplicar la **lectura y escritura de archivos** (`open`, `.write()`, `.readlines()` o `csv.writer`).  
4. Fortalecer el diseño modular usando **funciones**.  
5. Reforzar la lógica de validación de entradas y persistencia de datos.

---

## 🧠 Requisitos previos
Antes de comenzar este proyecto, asegúrate de dominar los siguientes temas:

- Uso de **listas** y **diccionarios**.  
- Estructuras de control (`if`, `for`, `while`).  
- Manejo básico de **archivos de texto o CSV**.  
- Funciones (`def`, `return`) y estructuras de menú interactivas.  
- Validación de datos con `try` / `except`.  

> 💡 Recomendación: repasa las clases 12 a la 21 si necesitas reforzar estructuras de datos y manejo de archivos.

---

## 🧩 Descripción del proyecto
Vas a construir un **Sistema de Registro de Estudiantes** que funcione desde consola y permita:

1. **Registrar** nuevos estudiantes (nombre, edad, curso, calificación, etc.).  
2. **Mostrar** todos los registros guardados.  
3. **Buscar** un estudiante por nombre.  
4. **Guardar y leer** los datos desde un archivo `.csv` o `.txt`.  
5. **Salir** del programa de forma segura.

> 🎯 El sistema debe recordar la información incluso después de cerrar el programa (gracias al archivo externo).

---

## 🧱 Estructura sugerida del proyecto

01_Python_Basico_Clase25/
│
├── main.py # Código principal del sistema
├── estudiantes.csv # Archivo donde se guardarán los datos
├── README.md # Documentación del proyecto
└── notas.txt # (opcional) apuntes, ideas o mejoras

---

## 🧰 Recomendaciones de desarrollo
- Usa un **diccionario por cada estudiante**:  
  ```python
  estudiante = {
      "nombre": "Ana",
      "edad": 20,
      "curso": "Python",
      "nota": 95
  }

- Almacena todos los diccionarios dentro de una lista (lista_estudiantes).

- Crea funciones como:

- agregar_estudiante()

- mostrar_estudiantes()

- buscar_estudiante()

- guardar_en_archivo()

- cargar_desde_archivo()

- Usa un bucle while con un menú principal.

- Guarda los datos usando módulo csv o funciones estándar de archivos (open(), write()).

## 🧮 Ejemplo de interacción esperada

--- Sistema de Registro de Estudiantes ---

1. Agregar estudiante
2. Mostrar todos los estudiantes
3. Buscar estudiante
4. Guardar y salir

Selecciona una opción: 1
Nombre: Juan Pérez
Edad: 22
Curso: Python Básico
Nota: 89

✅ Estudiante registrado correctamente.

¿Deseas continuar? (s/n): s

## 🚀 Tarea

Crea el archivo main.py e implementa el sistema completo siguiendo las recomendaciones anteriores.
Prueba distintas acciones:

- Registrar varios estudiantes.

- Buscar nombres que existan o no existan.

- Verificar que los datos se guardan en el archivo.

- Volver a ejecutar el programa y comprobar que se cargan correctamente.

Guarda todo en tu repositorio de GitHub dentro de: 01_Python_Basico_Clase25/
