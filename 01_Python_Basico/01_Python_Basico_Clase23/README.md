# 🧾 Clase 23 — Sistema de Inventario Avanzado

## 🎯 Objetivo
En esta clase aprenderás a **modularizar** un programa grande, **refactorizar** código repetido en funciones reutilizables y **mejorar la robustez** del sistema de inventario mediante el uso de excepciones y validaciones.

---

## 🧠 Conceptos Clave

### 1️⃣ Modularización
Dividir el código en funciones que realicen tareas específicas.  
Ventajas:
- Reutilización de código.
- Facilidad para depurar errores.
- Mejora de la organización y legibilidad.

### 2️⃣ Manejo de Excepciones
Usar `try`, `except` y `finally` para manejar errores durante la ejecución, evitando que el programa se detenga bruscamente.

python
try:
    valor = int(input("Ingresa un número: "))
except ValueError:
    print("❌ Error: Debes ingresar un número entero.")

### 3️⃣ Operaciones comunes con archivos CSV

- Lectura: csv.DictReader() → convierte cada fila en un diccionario.

- Escritura: csv.DictWriter() → escribe filas con encabezados.

## 🧩 Funcionalidades Nuevas del Sistema

| Función                | Descripción                                            |
| ---------------------- | ------------------------------------------------------ |
| `agregar_producto()`   | Agrega un nuevo producto al inventario.                |
| `mostrar_inventario()` | Muestra todos los productos del archivo.               |
| `buscar_producto()`    | Permite buscar un producto por nombre.                 |
| `editar_producto()`    | Edita precio o cantidad de un producto existente.      |
| `eliminar_producto()`  | Elimina un producto del inventario.                    |
| `menu()`               | Muestra las opciones y controla el flujo del programa. |

## 📚 Aprendizaje Clave

- Uso avanzado de archivos CSV.

- Modularización y buenas prácticas.

- Validación de entrada del usuario.

- Operaciones CRUD (Create, Read, Update, Delete).