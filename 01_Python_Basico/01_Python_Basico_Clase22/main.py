import csv
import os

# ==============================
#  Sistema de Gestión de Inventario
#  Clase 22 - Python Básico
# ==============================

ARCHIVO = "inventario.csv"

# ---------------------------------
# Función: inicializar archivo CSV
# ---------------------------------
def inicializar_archivo():
    """Crea el archivo CSV si no existe, con encabezados."""
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, mode="w", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Nombre", "Precio", "Cantidad"])
        print("📁 Archivo de inventario creado correctamente.\n")


# ---------------------------------
# Función: agregar producto
# ---------------------------------
def agregar_producto():
    """Agrega un nuevo producto al archivo CSV."""
    nombre = input("Nombre del producto: ").capitalize()
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("⚠️  Error: El precio o la cantidad no son válidos.\n")
        return

    with open(ARCHIVO, mode="a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, precio, cantidad])
    print(f"✅ Producto '{nombre}' agregado correctamente.\n")


# ---------------------------------
# Función: ver inventario completo
# ---------------------------------
def ver_inventario():
    """Muestra todos los productos almacenados."""
    if not os.path.exists(ARCHIVO):
        print("⚠️  No hay inventario disponible.\n")
        return

    with open(ARCHIVO, mode="r") as archivo:
        reader = csv.reader(archivo)
        next(reader, None)  # Saltar encabezado
        productos = list(reader)

    if not productos:
        print("📭 El inventario está vacío.\n")
        return

    print("\n📦 Inventario actual:")
    print("-" * 40)
    for producto in productos:
        print(f"{producto[0]} | Precio: {producto[1]} | Cantidad: {producto[2]}")
    print("-" * 40 + "\n")


# ---------------------------------
# Función: buscar producto
# ---------------------------------
def buscar_producto():
    """Busca un producto por nombre dentro del archivo."""
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").capitalize()
    encontrado = False

    with open(ARCHIVO, mode="r") as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            if fila["Nombre"] == nombre_buscar:
                print(f"\n🔍 Producto encontrado:")
                print(f"Nombre: {fila['Nombre']}")
                print(f"Precio: {fila['Precio']}")
                print(f"Cantidad: {fila['Cantidad']}\n")
                encontrado = True
                break

    if not encontrado:
        print(f"❌ El producto '{nombre_buscar}' no está en el inventario.\n")


# ---------------------------------
# Función principal del programa
# ---------------------------------
def menu():
    """Muestra el menú principal del sistema."""
    inicializar_archivo()

    while True:
        print("=" * 40)
        print("  Sistema de Gestión de Inventario")
        print("=" * 40)
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Buscar producto")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            print("👋 Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("⚠️  Opción no válida. Intente nuevamente.\n")


# -------------------------------
# Ejecución del programa principal
# -------------------------------
if __name__ == "__main__":
    menu()

## 💬 Explicación breve

#El programa crea automáticamente el archivo inventario.csv si no existe.

#Permite agregar, ver y buscar productos.

#Usa el módulo csv para leer y escribir datos de forma estructurada.

#Todo se ejecuta desde el menú principal.