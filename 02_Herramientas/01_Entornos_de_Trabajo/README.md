# 🧠 Clase 1 – Entornos de Trabajo en Python

## 🎯 Objetivos de aprendizaje
- Comprender qué son los entornos de desarrollo en Python y por qué se usan.
- Aprender a trabajar con **VS Code** y **Jupyter Notebooks**.
- Crear y gestionar entornos virtuales con `venv` y `conda`.
- Instalar, actualizar y desinstalar librerías usando `pip`.

---

## 🧩 Nivel 1 – Fundamentos (Básico–Intermedio)

### 🖥️ 1. ¿Qué es un entorno de trabajo?
Un **entorno de trabajo** es el espacio donde escribes, ejecutas y pruebas tu código.  
En Python, los más usados son:

- **VS Code** → Editor liviano, muy personalizable, ideal para proyectos.
- **Jupyter Notebooks** → Entorno interactivo para análisis de datos, visualización y documentación en una sola interfaz.

💡 *Piensa en Jupyter como un cuaderno experimental y en VS Code como un taller de producción.*

---

### ⚙️ 2. Uso de Jupyter Notebooks

#### 🔹 Instalación
```bash
pip install notebook

```
🔹 Ejecución
jupyter notebook

Esto abrirá una interfaz web donde puedes crear archivos .ipynb.

🔹 Celdas

- Celdas de código → Para ejecutar Python.

- Celdas de texto (Markdown) → Para escribir notas, ecuaciones y explicaciones.

## 🧠 Ejemplo:

```python
# Celda de código

nombre = "Alejandro"
print(f"Hola, {nombre}! Bienvenido a Jupyter.")

```

## 🧰 3. Uso de Visual Studio Code (VS Code)
🔹 Instalación de Python Extension

- Abre VS Code → pestaña Extensions (Ctrl+Shift+X) → busca “Python” → instala.

🔹 Crear archivo y ejecutar

1. Crea hola.py

2. Escribe:

``` python 
print("Hola desde VS Code!")
```

### 3. Ejecuta con Ctrl+F5 o el botón ▶️ “Run”.

## 🧩 4. Entornos virtuales (venv y conda)

Los entornos virtuales te permiten aislar librerías entre proyectos.
Cada proyecto puede tener sus propias dependencias sin interferir con otros.

🔹 Crear entorno virtual con venv

``` bash 
python -m venv mi_entorno
```

🔹 Activar entorno

- En Windows:
``` bash
mi_entorno\Scripts\activate
```

- En macOS/Linux:
``` bash
source mi_entorno/bin/activate
```

🔹 Desactivar
``` bash
deactivate
```

🔹 Crear entorno con conda
``` bash

conda create -n mi_entorno python=3.11
conda activate mi_entorno
```

## 📦 5. Instalación y gestión de librerías con pip

pip es el gestor de paquetes oficial de Python.

🔹 Comandos principales:

``` bash 
pip install numpy
pip install pandas==2.1.0
pip uninstall matplotlib
pip list
pip freeze > requirements.txt
```

## 🧠 Ejemplo práctico:
``` python

import numpy as np
import pandas as pd

datos = np.array([10, 20, 30])
tabla = pd.DataFrame({"Valores": datos})
print(tabla)
```

# 🚀 Nivel 2 – Avanzado
## 🧩 1. requirements.txt – Control de dependencias

Permite guardar todas las librerías y versiones de un entorno:
```  bash
pip freeze > requirements.txt
```

Y luego instalarlas en otro entorno:

``` bash
pip install -r requirements.txt
```

## 🧩 2. Crear entorno de datos reproducible con conda
``` bash
conda create -n datalab python=3.12 numpy pandas matplotlib scikit-learn
```

## 🧩 3. Uso profesional de Jupyter

- Instala extensiones con jupyter contrib nbextension install --user.

- Ejecuta código del sistema con !comandos:

```python
!pip list
!dir  # (en Windows)
```

# 🧪 Ejercicios Propuestos
🔹 Ejercicios básicos (1–4)

1. Instala jupyter y crea un notebook que imprima tu nombre y edad.

2. Crea un entorno virtual llamado proyecto1 e instala numpy y pandas.

3. Usa pip list para verificar las librerías instaladas.

4. Crea un archivo requirements.txt con tus dependencias.

🔹 Ejercicios intermedios (5–6)

5. Usa Jupyter para crear una celda Markdown con una explicación y otra con código que calcule el promedio de una lista.

6. Crea un script en VS Code que lea un archivo .txt y cuente cuántas líneas tiene.

🔹 Ejercicios de la vida real (7–8)

7. 📊 Caso real: Un analista necesita crear un entorno reproducible para un análisis de ventas.
Crea un entorno ventas_env, instala pandas y guarda sus dependencias en requirements.txt.

8. 🧬 Caso real: Crea un entorno bioinfo_env y usa pip para instalar numpy y matplotlib.
Luego, genera un script que grafique datos simulados de crecimiento celular.

## Resumen

| Concepto               | Descripción breve                                      |
| ---------------------- | ------------------------------------------------------ |
| **VS Code**            | Editor profesional para desarrollo completo.           |
| **Jupyter Notebooks**  | Ideal para análisis interactivo y documentación.       |
| **Entornos virtuales** | Aíslan librerías por proyecto.                         |
| **`pip` y `conda`**    | Herramientas para instalar y administrar dependencias. |
| **`requirements.txt`** | Archivo que guarda todas las librerías de un proyecto. |

## 📚 Archivos sugeridos

02_Herramientas_Ciencia_Datos/
│
├── 01_Entornos_de_Trabajo/
│   ├── README.md
│   ├── ejemplo_notebook.ipynb
│   ├── entorno_ventas/          # entorno virtual (no subir al repo)
│   └── requirements.txt

✅ Al completar esta clase, podrás crear y gestionar entornos profesionales para cualquier proyecto de ciencia de datos en Python.