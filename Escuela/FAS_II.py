import sys

# Sistema de inicio de sesión
def login():
    intentos = 4
    usuario_correcto = "Romero"
    contraseña_correcta = "Romero1508"

    print("Bienvenido al sistema de compras.")

    while intentos > 0:
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            print("Inicio de sesión exitoso.\n")
            return True
        else:
            intentos -= 1
            print(f"Usuario y contraseña incorrecto. Le quedan {intentos} intentos.")

    print("Ha excedido el número de intentos. Cerrando el programa.")
    sys.exit()

# Catálogo de productos
def mostrar_catalogo():
    catalogo = {
        "Ropa para dama": {
            "VM": {"Producto": "Vestido Mujer", "Precio": 200, "Tallas": ("CH", "M", "G", "XG"), "Colores": ("Negro", "Blanco", "Azul", "Rosa")},
            "BM": {"Producto": "Blusa Mujer", "Precio": 150, "Tallas": ("M", "G", "XG"), "Colores": ("Negro", "Blanco", "Azul")},
            "FM": {"Producto": "Falda Mujer", "Precio": 180, "Tallas": ("CH", "M", "G", "XG"), "Colores": ("Negro", "Azul")}
        },
        "Ropa para caballero": {
            "CH": {"Producto": "Camisa Hombre", "Precio": 160, "Tallas": ("CH", "M", "G", "XG"), "Colores": ("Negro", "Blanco", "Azul")},
            "PH": {"Producto": "Pantalón Hombre", "Precio": 190, "Tallas": ("CH", "M", "G"), "Colores": ("Negro", "Azul")},
            "SH": {"Producto": "Saco Hombre", "Precio": 300, "Tallas": ("CH", "M", "G", "XG"), "Colores": ("Negro", "Azul")}
        },
        "Ropa para niña": {
            "VN": {"Producto": "Vestido Niña", "Precio": 120, "Tallas": ("CH", "G", "XG"), "Colores": ("Rosa", "Blanco")},
            "BN": {"Producto": "Blusa Niña", "Precio": 100, "Tallas": ("CH", "M", "G", "XG"), "Colores": ("Rosa", "Blanco")},
            "FN": {"Producto": "Falda Niña", "Precio": 110, "Tallas": ("CH", "M", "G", "XG"), "Colores": ("Rosa", "Azul")}
        },
        "Ropa para niño": {
            "CNI": {"Producto": "Camisa Niño", "Precio": 100, "Tallas": ("M", "G", "XG"), "Colores": ("Azul", "Blanco")},
            "PNI": {"Producto": "Pantalón Niño", "Precio": 110, "Tallas": ("CH", "M", "G", "XG"), "Colores": ("Azul", "Negro")},
            "SNI": {"Producto": "Saco Niño", "Precio": 150, "Tallas": ("CH", "M", "G", "XG"), "Colores": ("Azul", "Negro")}
        }
    }

    for categoria, productos in catalogo.items():
        print(f"\n{categoria}:")
        for clave, detalles in productos.items():
            print(f"Clave: {clave}, Producto: {detalles['Producto']}, Precio: ${detalles['Precio']}, Tallas: {detalles['Tallas']}, Colores: {detalles['Colores']}")

    return catalogo

# Selección de productos, tallas y colores
def seleccionar_productos(catalogo):
    seleccion = []
    while True:
        clave = input("\nIngrese la clave del producto que desea comprar (o 'fin' para terminar): ").upper()
        if clave == 'FIN':
            break

        producto_encontrado = None
        for categoria, productos in catalogo.items():
            if clave in productos:
                producto_encontrado = productos[clave]
                break

        if producto_encontrado:
            talla = input(f"Ingrese la talla para {producto_encontrado['Producto']} ({', '.join(producto_encontrado['Tallas'])}): ").upper()
            if talla in producto_encontrado['Tallas']:
                color = input(f"Ingrese el color para {producto_encontrado['Producto']} ({', '.join(producto_encontrado['Colores'])}): ").capitalize()
                if color in producto_encontrado['Colores']:
                    seleccion.append((clave, talla, color, producto_encontrado['Precio']))
                    print(f"Producto {producto_encontrado['Producto']} talla {talla} color {color} agregado.")
                else:
                    print("Color no disponible. Por favor, seleccione otro color.")
            else:
                print("Talla no disponible. Por favor, seleccione otra talla.")
        else:
            print("Clave de producto no válida. Intente nuevamente.")

    return seleccion

# Excepciones para tallas no disponibles
def verificar_excepciones(seleccion):
    excepciones = {
        "VM": {"Tallas_no_disponibles": ["CH"]},
        "SH": {"Tallas_no_disponibles": ["CH"]},
        "SNI": {"Tallas_no_disponibles": ["G"]}
    }

    productos_no_disponibles = []
    for item in seleccion:
        clave, talla, color, precio = item
        if clave in excepciones and talla in excepciones[clave]["Tallas_no_disponibles"]:
            print(f"Lo sentimos, la talla {talla} para el producto {clave} no está disponible. Se devolverá el dinero.")
            productos_no_disponibles.append(item)

    # Eliminar productos no disponibles de la selección
    seleccion = [item for item in seleccion if item not in productos_no_disponibles]
    return seleccion, productos_no_disponibles

# Generar ticket de compra
def generar_ticket(seleccion, productos_no_disponibles):
    total = 0
    envio = 99  # Costo de envío fijo
    descuento_total = 0

    with open("ticket_compra.txt", "w") as archivo:
        archivo.write("Ticket de Compra\n")
        archivo.write("================\n")

        # Productos seleccionados
        archivo.write("Productos seleccionados:\n")
        for clave, talla, color, precio in seleccion:
            descuento = 0
            if talla == "XG":
                descuento = precio * 0.10  # 10% de descuento para talla XG
                precio_con_descuento = precio - descuento
            else:
                precio_con_descuento = precio

            archivo.write(f"Producto: {clave}, Talla: {talla}, Color: {color}, Precio: ${precio:.2f}, Descuento: ${descuento:.2f}, Precio final: ${precio_con_descuento:.2f}\n")
            total += precio_con_descuento
            descuento_total += descuento

        # Productos no disponibles
        if productos_no_disponibles:
            archivo.write("\nProductos no disponibles (se devolverá el dinero):\n")
            for clave, talla, color, precio in productos_no_disponibles:
                archivo.write(f"Producto: {clave}, Talla: {talla}, Color: {color}, Precio a devolver: ${precio:.2f}\n")

        # Resumen de la compra
        archivo.write("\nResumen de la compra:\n")
        archivo.write(f"Subtotal: ${total:.2f}\n")
        archivo.write(f"Descuentos aplicados: ${descuento_total:.2f}\n")
        archivo.write(f"Costo de envio: ${envio:.2f}\n")
        archivo.write(f"Total: ${total + envio:.2f}\n")

    print("\nTicket de compra generado con éxito. Revise el archivo 'ticket_compra.txt'.")

# Función principal
def main():
    if login():
        catalogo = mostrar_catalogo()
        seleccion = seleccionar_productos(catalogo)
        seleccion, productos_no_disponibles = verificar_excepciones(seleccion)
        generar_ticket(seleccion, productos_no_disponibles)

if __name__ == "__main__":
    main()