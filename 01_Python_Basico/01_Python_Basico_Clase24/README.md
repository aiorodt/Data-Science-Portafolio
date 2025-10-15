# 🧮 Clase 24 — Proyecto: Calculadora Interactiva

## 📘 Introducción
En esta clase comenzarás la primera práctica del módulo **7. Ejercicios Prácticos**, aplicando todo lo aprendido sobre:
- Variables y operadores  
- Condicionales  
- Bucles  
- Funciones  
- Entrada y salida de datos  

El objetivo es construir una **calculadora interactiva** que funcione desde la consola y permita realizar operaciones matemáticas básicas, usando una estructura organizada con funciones.

---

## 🎯 Objetivos de la clase
1. Implementar un programa interactivo con menú.
2. Aplicar el uso de **funciones** para modularizar el código.
3. Practicar la **validación de entradas** y el control de errores.
4. Fortalecer el manejo de estructuras de control (`if`, `while`, etc.).

---

## 🧠 Requisitos previos
Antes de comenzar este proyecto, asegúrate de dominar los siguientes temas:

- Uso de **variables** y tipos de datos (`int`, `float`, `str`).
- Conocimiento de **operadores aritméticos** y **lógicos**.
- Manejo de **condicionales** (`if`, `elif`, `else`).
- Uso de **bucles** (`while`, `for`).
- Definición y uso de **funciones** (`def`).
- Captura de datos con `input()` y salida con `print()`.

> 💡 Si alguno de estos temas aún no te resulta claro, repasa las clases previas antes de continuar.

---

## 🧩 Descripción del proyecto
Vas a desarrollar una **calculadora interactiva por consola** que cumpla con las siguientes características:

1. Mostrar un **menú principal** con opciones como:
   - Sumar
   - Restar
   - Multiplicar
   - Dividir
   - Salir del programa  
2. Solicitar al usuario los números necesarios para cada operación.  
3. Realizar el cálculo usando **funciones** independientes (`def sumar(a,b):`, `def restar(a,b):`, etc.).  
4. Manejar errores (por ejemplo, división entre cero o entrada no válida).  
5. Continuar ejecutándose hasta que el usuario elija salir.

---

## 🧱 Estructura sugerida del proyecto

01_Python_Basico_Clase24/
│
├── main.py # Código principal del programa
├── README.md # Instrucciones del proyecto
└── notas.txt # (opcional) apuntes personales o ideas
---

## 🧰 Recomendaciones de desarrollo
- Crea una función llamada `menu()` que muestre las opciones al usuario.  
- Usa un bucle `while True` para mantener el programa en ejecución.  
- Emplea `try-except` para capturar errores de tipo de datos o división entre cero.  
- Muestra mensajes claros al usuario en cada paso.  
- Utiliza `return` dentro de tus funciones matemáticas.

---

## 🧮 Ejemplo de interacción esperada

--- Calculadora Interactiva ---

1. Sumar

2. Restar

3. Multiplicar

4. Dividir

5. Salir

Selecciona una opción: 1
Ingresa el primer número: 10
Ingresa el segundo número: 5
Resultado: 15

¿Deseas continuar? (s/n): s


---
## 🚀 Tarea
Desarrolla el archivo `main.py` aplicando todas las recomendaciones anteriores.  
Cuando finalices, prueba distintos casos:

- Ingresar letras en lugar de números.  
- Dividir entre cero.  
- Repetir operaciones.  
- Salir del programa correctamente.  

Guarda tu progreso en GitHub dentro de la carpeta: 01_Python_Basico_Clase24/


