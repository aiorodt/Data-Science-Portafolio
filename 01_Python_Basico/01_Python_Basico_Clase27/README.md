# 🧮 Clase 27 — Resolución de Problemas Clásicos en Python

## 🎯 Objetivos de la clase
- Aplicar estructuras básicas de programación para resolver problemas reales.  
- Reforzar lógica algorítmica con bucles, condicionales y funciones.  
- Aprender a depurar y optimizar soluciones paso a paso.  
- Usar entradas dinámicas (`input()`) y salidas formateadas (`print()`).  

---

## 🧠 Requisitos previos
- Conocer variables, tipos de datos, listas y condicionales.  
- Haber practicado el uso de bucles `for` y `while`.  
- Saber definir funciones con `def` y usar `return`.

---

# 🧩 Problema 1: Números Primos

## 📝 Descripción
Un número primo es aquel que solo es divisible por 1 y por sí mismo.  
Crea un programa que determine si un número ingresado por el usuario es primo.

---

## 💡 Análisis
1. Leer un número entero.  
2. Comprobar si es divisible por algún número entre 2 y (n-1).  
3. Si no tiene divisores, es primo.

---

## 🧱 Código

```python
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Entrada del usuario
n = int(input("Ingrese un número: "))

# Evaluación y salida
if es_primo(n):
    print(f"✅ {n} es un número primo.")
else:
    print(f"❌ {n} no es primo.")

```
## 🧩 Ejemplo de ejecución

Ingrese un número: 17
✅ 17 es un número primo.

## 🧠 Reflexión

- Usar int(numero ** 0.5) optimiza el cálculo (no es necesario revisar todos los divisores).

- Aprendiste cómo transformar una verificación matemática en lógica computacional.

# 🧩 Problema 2: Palíndromo

## 📝 Descripción

Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda (ignorando espacios y mayúsculas).

Ejemplo:

- “reconocer”

- “anita lava la tina”

## 💡 Análisis

1. Eliminar espacios y convertir a minúsculas.

2. Comparar la cadena original con su versión invertida.

3. Si son iguales, es un palíndromo.

## 🧱 Código

``` python
def es_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

# Entrada del usuario
frase = input("Ingrese una palabra o frase: ")

# Evaluación
if es_palindromo(frase):
    print("✅ Es un palíndromo.")
else:
    print("❌ No es un palíndromo.")
``` 

## 🧩 Ejemplo de ejecución

Ingrese una palabra o frase: Anita lava la tina
✅ Es un palíndromo.

# 🧠 Reflexión

- La notación [::-1] permite invertir una cadena fácilmente.

- Reforzaste manipulación de cadenas (replace(), lower()) y comparación lógica.

# 🧩 Problema 3: Serie Fibonacci

## 📝 Descripción

La Serie Fibonacci se forma sumando los dos números anteriores:
0, 1, 1, 2, 3, 5, 8, 13...

Crea un programa que muestre los primeros n términos de la serie.

## 💡 Análisis

1. Solicitar cuántos términos generar.

2. Iniciar con [0, 1].

3. Calcular cada nuevo número como la suma de los dos anteriores.

4. Mostrar la lista completa.

## 🧱 Código
``` python

def generar_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[-1] + serie[-2])
    return serie

# Entrada del usuario
n = int(input("¿Cuántos términos de Fibonacci deseas ver? "))

# Generación y salida
fibo = generar_fibonacci(n)
print("📈 Serie Fibonacci:", fibo)
```
## 🧩 Ejemplo de ejecución

¿Cuántos términos de Fibonacci deseas ver? 8
📈 Serie Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13]

## 🧠 Reflexión

- La lista dinámica serie muestra cómo construir secuencias de manera iterativa.

- Este patrón se aplica en muchos algoritmos de crecimiento acumulativo.

## 🧾 Resumen de la Clase

| Concepto               | Aplicado en | Aprendizaje Clave          |
| ---------------------- | ----------- | -------------------------- |
| Bucles y condicionales | Problema 1  | Verificación matemática    |
| Cadenas y rebanado     | Problema 2  | Manipulación de texto      |
| Listas dinámicas       | Problema 3  | Construcción de secuencias |

## 💡 Retos adicionales (para practicar)

1. Crear un contador de vocales y consonantes en una palabra.

2. Determinar si un número es perfecto (la suma de sus divisores = número).

3. Generar una tabla de multiplicar completa con formato.

## 🧰 Requisitos técnicos

- Python 3.10 o superior.

- Editor recomendado: VS Code, Thonny o PyCharm.

- Archivos organizados dentro de:
01_Python_Basico_Clase28/
├── problema1_primo.py
├── problema2_palindromo.py
├── problema3_fibonacci.py
└── README.md

## 🧩 Cierre

Con estos tres ejercicios, consolidas las bases de la resolución algorítmica en Python:

- Pensar paso a paso antes de programar.

- Traducir la lógica humana en instrucciones precisas.

- Comprobar resultados mediante pruebas simples.

Continúa practicando y refuerza cada problema creando tus propias variaciones 🚀
