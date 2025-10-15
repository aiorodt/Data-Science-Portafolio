import csv

ARCHIVO = "inventario.csv"

def cargar_inventario():
    try:
        with open(ARCHIVO, newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

def guardar_inventario(inventario):
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
        campos = ["nombre", "precio", "cantidad"]
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(inventario)

def agregar_producto():
    nombre = input("Nombre del producto: ").capitalize()
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    inventario = cargar_inventario()
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    guardar_inventario(inventario)
    print(f"✅ Producto '{nombre}' agregado con éxito.")

def mostrar_inventario():
    inventario = cargar_inventario()
    if not inventario:
        print("📂 Inventario vacío.")
    else:
        print("\n=== Inventario Actual ===")
        for item in inventario:
            print(f"{item['nombre']} - Precio: ${item['precio']} - Cantidad: {item['cantidad']}")

def buscar_producto():
    inventario = cargar_inventario()
    nombre = input("Nombre del producto a buscar: ").capitalize()
    for item in inventario:
        if item["nombre"] == nombre:
            print(f"🔎 Encontrado: {item['nombre']} - Precio: ${item['precio']} - Cantidad: {item['cantidad']}")
            return
    print("❌ Producto no encontrado.")

def editar_producto():
    inventario = cargar_inventario()
    nombre = input("Producto a editar: ").capitalize()
    for item in inventario:
        if item["nombre"] == nombre:
            print(f"Producto encontrado: {item}")
            item["precio"] = float(input("Nuevo precio: "))
            item["cantidad"] = int(input("Nueva cantidad: "))
            guardar_inventario(inventario)
            print("✅ Producto actualizado.")
            return
    print("❌ Producto no encontrado.")

def eliminar_producto():
    inventario = cargar_inventario()
    nombre = input("Producto a eliminar: ").capitalize()
    inventario = [item for item in inventario if item["nombre"] != nombre]
    guardar_inventario(inventario)
    print(f"🗑️ Producto '{nombre}' eliminado (si existía).")

def menu():
    while True:
        print("\n=== SISTEMA DE INVENTARIO AVANZADO ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Editar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            editar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    menu()
