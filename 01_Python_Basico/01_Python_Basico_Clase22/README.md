# 🧾 Sistema de Gestión de Inventario (Clase 22)

## 📘 Descripción General
Este proyecto implementa un **sistema básico de gestión de inventario** usando Python.  
Permite **agregar, visualizar, buscar y guardar productos** en un archivo `.csv`,  
aplicando los conceptos de **manejo de archivos** vistos en la Clase 21.

El sistema es totalmente interactivo y funciona desde la consola.  
Los productos se almacenan en el archivo `inventario.csv`, lo que permite que la información se conserve incluso después de cerrar el programa.

---

## 🎯 Objetivos de Aprendizaje

- Comprender cómo **leer y escribir archivos `.csv`** en Python.  
- Usar el módulo integrado **`csv`** para gestionar datos estructurados.  
- Aplicar **funciones** para separar la lógica del programa.  
- Diseñar un sistema persistente que **almacene información de forma permanente**.  
- Practicar la **validación de datos** y el **manejo de errores**.

---

## 🧩 Estructura del Proyecto


01_Python_Basico_Clase22/
│
├── main.py # Código principal del sistema de inventario
├── inventario.csv # Archivo donde se guardan los productos
├── README.md # Guía y documentación del proyecto
└── notas.txt # (opcional) apuntes o ideas adicionales


---

## 🚀 Cómo ejecutar el programa

1. Abre una terminal en la carpeta del proyecto:
   ```bash
   cd 01_Python_Basico_Clase22

2. Ejecuta el siguiente comando:
python main.py

3. Aparecerá un menú interactivo en la consola.
Desde allí podrás:

- Agregar un nuevo producto.

- Ver todos los productos registrados.

- Buscar un producto por nombre.

- Guardar y salir del programa.

## 💡 Ejemplo de Ejecución

====================================
  Sistema de Gestión de Inventario
====================================
1. Agregar producto
2. Ver productos
3. Buscar producto
4. Salir
Seleccione una opción: 1

Nombre del producto: Teclado
Precio: 25
Cantidad: 10
✅ Producto agregado correctamente.

Seleccione una opción: 2
📦 Inventario actual:
-------------------------
Teclado | Precio: 25 | Cantidad: 10
-------------------------

## ⚙️ Tecnologías Utilizadas

- Python 3.x

- Módulo csv para manejo de archivos estructurados

- Lectura y escritura de archivos con open() y with

- Uso de funciones para modularizar el código

## 🧠 Conceptos Aplicados

- Persistencia de datos con archivos .csv

- Separación lógica de funciones (agregar_producto, ver_inventario, buscar_producto)

- Estructuras de datos (listas y diccionarios)

- Bucles y condicionales (for, if)

- Manejo de excepciones con try / except

## ✍️ Autor

Proyecto desarrollado por Alejandro
como parte del curso Python Básico - Clase 22: Manejo de Archivos con Proyecto Práctico.

