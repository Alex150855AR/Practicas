import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import os  # Importar el módulo os para manejar rutas

# Datos de usuarios predefinidos
users = {
    'Romero': 'Romero15',
    'usuario2': 'password2',
    'usuario3': 'password3'
}

# Datos de stock de materiales por rack (precios como números flotantes)
stock_data = {
    "Rack A (Intel)": [
        ["A1,A1", "B55.0004", "i3-12100", "Procesador Intel Core I3", 500.00, 700.00, 80],
        ["A2,A1", "B55.0005", "i3-10100", "Procesador Intel Core I4", 450.00, 650.00, 80],
        ["A1,A2", "B55.0006", "i5-12600K", "Procesador Intel Core I5", 700.00, 1000.00, 80],
        ["A2,A2", "B55.0007", "i5-10400F", "Procesador Intel Core I6", 650.00, 950.00, 80],
        ["A1,A3", "B55.0008", "i7-12700K", "Procesador Intel Core I7", 900.00, 1300.00, 80],
        ["A1,A3", "B55.0009", "i7-10700K", "Procesador Intel Core I8", 850.00, 1250.00, 80],
        ["A2,A3", "B55.0010", "i9-13900K", "Procesador Intel Core I9", 1200.00, 1800.00, 80],
        ["A2,A3", "B55.0011", "i9-10900K", "Procesador Intel Core I10", 1150.00, 1750.00, 80]
    ],
    "Rack A (AMD)": [
        ["A3,A1", "B65.0004", "3-3300X", "Ryzen 3", 500.00, 700.00, 80],
        ["A4,A1", "B65.0005", "3-5300G", "Ryzen 3", 450.00, 650.00, 80],
        ["A3,A2", "B65.0006", "5-5600X", "Ryzen 5", 700.00, 1000.00, 80],
        ["A4,A2", "B65.0007", "5-4600G", "Ryzen 5", 650.00, 950.00, 80],
        ["A3,A3", "B65.0008", "7-5800X", "Ryzen 7", 900.00, 1300.00, 80],
        ["A3,A3", "B65.0009", "7-5700G", "Ryzen 7", 850.00, 1250.00, 80],
        ["A4,A3", "B65.0010", "9-5900X", "Ryzen 9", 1200.00, 1800.00, 80],
        ["A4,A3", "B65.0011", "9-5950X", "Ryzen 9", 1150.00, 1750.00, 80]
    ],
    "Rack A (RAM)": [
        ["A5,A1", "B21.0001", "Corsair Vengeance LPX", "RAM 8GB DDR4 3200MHz", 500.00, 700.00, 50],
        ["A6,A1", "B21.0002", "Crucial Ballistix", "RAM 8GB DDR4 3200MHz", 450.00, 650.00, 50],
        ["A5,A2", "B21.0003", "G.Skill Trident Z Neo", "RAM 16GB DDR4 3600MHz", 700.00, 1000.00, 50],
        ["A6,A2", "B21.0004", "Kingston Fury Beast", "RAM 16GB DDR4 3200MHz", 650.00, 950.00, 50],
        ["A5,A3", "B21.0005", "Corsair Dominator Platinum RGB", "RAM 32 GB DDR5 5200MHz", 900.00, 1300.00, 50],
        ["A6,A3", "B21.0006", "Crucial Pro", "RAM 32 GB DDR5 4800MHz", 850.00, 1250.00, 50]
    ],
    "Rack B (Discos Duros)": [
        ["B1,B1", "B48.0711", "Samsung 870 EVO", "Disco Duro 500GB", 500.00, 700.00, 50],
        ["B2,B1", "B48.0712", "Crucial MX500", "Disco Duro 500GB", 450.00, 650.00, 50],
        ["B1,B2", "B48.0713", "Samsung 980 Pro", "Disco Duro 1TB", 700.00, 1000.00, 50],
        ["B2,B2", "B48.0714", "WD Black SN770", "Disco Duro 1TB", 650.00, 950.00, 50],
        ["B1,B3", "B48.0715", "Samsung 990 Pro", "Disco Duro 2TB", 900.00, 1300.00, 50],
        ["B2,B3", "B48.0716", "Kingston KC3000", "Disco Duro 2TB", 850.00, 1250.00, 50]
    ],
    "Rack B (Refrigeracion)": [
        ["B3,B1", "B71.0002", "Noctua NH-D15", "Refrigeracion Por Aire", 500.00, 700.00, 50],
        ["B4,B1", "B71.0003", "Cooler Master Hyper 212 EVO", "Refrigeracion Por Aire", 450.00, 650.00, 50],
        ["B3,B2", "B71.0004", "Arctic Freezer 34 eSports DUO", "Refrigeracion Por Aire", 400.00, 600.00, 50],
        ["B4,B2", "B71.0005", "NZXT Kraken X63", "Refrigeracion Liquida", 700.00, 1000.00, 50],
        ["B3,B3", "B71.0006", "Corsair iCUE H150i Elite LCD XT", "Refrigeracion Liquida", 900.00, 1300.00, 50],
        ["B4,B3", "B71.0007", "Cooler Master MasterLiquid ML240L V2 RGB", "Refrigeracion Liquida", 850.00, 1250.00, 50]
    ],
    "Rack B (Fuente de Poder)": [
        ["B5,B1", "B78.0001", "EVGA 600 BR", "Fuente de poder 80 PLUS Bronce", 500.00, 700.00, 70],
        ["B6,B1", "B78.0002", "Corsair CV550", "Fuente de poder 80 PLUS Bronce", 450.00, 650.00, 70],
        ["B5,B2", "B78.0003", "Seasonic FOCUS GX-650", "Fuente de poder 80 PLUS Silver", 600.00, 850.00, 70],
        ["B6,B2", "B78.0004", "XFX XTR 650", "Fuente de poder 80 PLUS Silver", 550.00, 800.00, 70],
        ["B5,B3", "B78.0005", "Corsair RM750x (2021)", "Fuente de poder 80 PLUS Gold", 700.00, 1000.00, 70],
        ["B6,B3", "B78.0006", "Seasonic PRIME TX-750", "Fuente de poder 80 PLUS Gold", 750.00, 1100.00, 70]
    ],
    "Rack C (MB Intel)": [
        ["C1,C1", "BL2.0051", "ASUS PRIME B660M-A D4", "MB Core I3-12100", 500.00, 700.00, 100],
        ["C2,C1", "BL2.0052", "ASUS H410M-E", "MB Core I3-10100", 450.00, 650.00, 100],
        ["C1,C2", "BL2.0053", "MSI MEG Z690 Unify", "MB Core I5-12600K", 700.00, 1000.00, 100],
        ["C2,C2", "BL2.0054", "ASUS PRIME H410M-K", "MB Core I5-10400F", 600.00, 900.00, 100],
        ["C1,C3", "BL2.0055", "GIGABYTE Z690 AORUS ULTRA", "MB Core I7-10700K", 800.00, 1200.00, 100],
        ["C2,C3", "BL2.0056", "ASUS ROG Maximus XII Hero", "MB Core I9-10900K", 900.00, 1300.00, 100]
    ],
    "Rack C (MB AMD)": [
        ["C3,C1", "B38.0011", "ASUS TUF Gaming B550-PLUS", "MB Ryzen 3", 500.00, 700.00, 100],
        ["C4,C1", "B38.0012", "ASUS PRIME A520M-K", "MB Ryzen 3", 450.00, 650.00, 100],
        ["C3,C2", "B38.0013", "MSI MAG B550 TOMAHAWK", "MB Ryzen 5", 600.00, 900.00, 100],
        ["C4,C2", "B38.0014", "Gigabyte B550M DS3H", "MB Ryzen 5", 550.00, 850.00, 100],
        ["C3,C3", "B38.0015", "MSI B550M PRO-VDH Wi-Fi", "MB Ryzen 7", 700.00, 1000.00, 100],
        ["C4,C3", "B38.0016", "ASUS ROG Crosshair VIII Hero", "MB Ryzen 9", 800.00, 1200.00, 100]
    ],
    "Rack C (Gabinete/Case)": [
        ["C5,C1", "BDP.0004", "Gabinete Gamer Xtreme PC Gaming Micro Torre", "Gabinete/Case", 500.00, 700.00, 30],
        ["C6,C1", "BDP.0005", "Gabinete Gamer Yeyian Stahl 900 Midi-Tower", "Gabinete/Case", 450.00, 650.00, 30],
        ["C5,C2", "BDP.0006", "Cooler Master MasterBox TD500 Mesh", "Gabinete/Case", 600.00, 900.00, 30],
        ["C6,C2", "BDP.0007", "NZXT H510", "Gabinete/Case", 550.00, 850.00, 30],
        ["C5,C3", "BDP.0008", "Corsair iCUE 4000X RGB", "Gabinete/Case", 700.00, 1000.00, 30],
        ["C6,C3", "BDP.0009", "Thermaltake Versa J24 TG RGB Edition", "Gabinete/Case", 650.00, 950.00, 30]
    ],
    "Rack D (Tarjeta de Video)": [
        ["D1,D1", "BP0.0051", "NVIDIA GeForce RTX 3060", "Nvidia", 500.00, 700.00, 40],
        ["D2,D1", "BP0.0052", "AMD Radeon RX 6700 XT", "AMD Radeon", 450.00, 650.00, 40],
        ["D1,D2", "BP0.0053", "NVIDIA GeForce RTX 4070 Ti", "Nvidia", 700.00, 1000.00, 40],
        ["D2,D2", "BP0.0054", "AMD Radeon RX 7900 XT", "AMD Radeon", 650.00, 950.00, 40],
        ["D1,D3", "BP0.0055", "NVIDIA GeForce GTX 1660 Super", "Nvidia", 400.00, 600.00, 40],
        ["D2,D3", "BP0.0056", "AMD Radeon RX 6600", "AMD Radeon", 350.00, 550.00, 40]
    ],
    "Rack D (Monitor)": [
        ["D3,D1", "BP2.00G1", "AOC 24B2XHM", "Monitor AOC", 500.00, 700.00, 40],
        ["D4,D1", "BP2.00G2", "BenQ GL2480", "Monitor BenQ", 450.00, 650.00, 40],
        ["D3,D2", "BP2.00G3", "ASUS TUF Gaming VG27VQM", "Monitor ASUS TUF Gaming", 700.00, 1000.00, 40],
        ["D4,D2", "BP2.00G4", "MSI Optix MAG272CQR", "MSI", 650.00, 950.00, 40],
        ["D3,D3", "BP2.00G5", "LG UltraGear 27GN950-B", "LG", 800.00, 1200.00, 40],
        ["D4,D3", "BP2.00G6", "Samsung Odyssey G7", "Samsung", 750.00, 1100.00, 40]
    ],
    "Rack D (Teclados)": [
        ["D5,D1", "B45.0001", "Redragon K552 Kumara", "Redragon", 500.00, 700.00, 40],
        ["D6,D1", "B45.0002", "Logitech G213 Prodigy", "Logitech", 450.00, 650.00, 40],
        ["D5,D2", "B45.0003", "HyperX Alloy FPS Pro", "HyperX", 400.00, 600.00, 40],
        ["D6,D2", "B45.0004", "Corsair K55 RGB Pro", "Corsair", 550.00, 850.00, 40],
        ["D5,D3", "B45.0005", "Razer BlackWidow V3 Pro", "Razer", 700.00, 1000.00, 40],
        ["D6,D3", "B45.0006", "Logitech G915 TKL", "Logitech", 750.00, 1100.00, 40]
    ],
    "Rack E (Mouse)": [
        ["E1,E1", "BP4.0001", "Logitech G203 Lightsync", "Logitech", 500.00, 700.00, 40],
        ["E2,E1", "BP4.0002", "Redragon M601 Centrophorus", "Redragon", 450.00, 650.00, 40],
        ["E1,E2", "BP4.0003", "Razer DeathAdder V2", "Razer", 600.00, 900.00, 40],
        ["E2,E2", "BP4.0004", "HyperX Pulsefire FPS Pro", "HyperX", 550.00, 850.00, 40],
        ["E1,E3", "BP4.0005", "Logitech G502 Lightspeed Wireless", "Logitech", 700.00, 1000.00, 40],
        ["E2,E3", "BP4.0006", "Razer Viper Ultimate", "Razer", 750.00, 1100.00, 40]
    ],
    "Rack E (Escritorio)": [
        ["E3,E1", "BP6.0001", "Escritorio Stay Elit Multifuncional", "Escritorio", 500.00, 700.00, 30],
        ["E4,E1", "BP6.0002", "Escritorio Libitum", "Escritorio", 450.00, 650.00, 30],
        ["E3,E2", "BP6.0003", "Escritorio Gamer Balam Rush Olympus MRX3000", "Escritorio", 600.00, 900.00, 30],
        ["E4,E2", "BP6.0004", "Escritorio Gamer Madesa de MDP", "Escritorio", 550.00, 850.00, 30],
        ["E3,E3", "BP6.0005", "Escritorio Gamer Cougar Mars 120", "Escritorio", 700.00, 1000.00, 30],
        ["E4,E3", "BP6.0006", "Escritorio Gamer RGB Pro", "Escritorio", 650.00, 950.00, 30]
    ],
    "Rack E (Silla)": [
        ["E5,E1", "B46.0001", "Redragon Metis", "Silla Redragon", 500.00, 700.00, 30],
        ["E6,E1", "B46.0002", "Xtreme PC Gaming Basic", "Silla Xtreme", 450.00, 650.00, 30],
        ["E5,E2", "B46.0003", "Cougar Armor One", "Silla Cougar", 600.00, 900.00, 30],
        ["E6,E2", "B46.0004", "Diablo X-One", "Silla Diablo", 550.00, 850.00, 30],
        ["E5,E3", "B46.0005", "Secretlab Titan Evo 2022", "Silla Secretlab", 700.00, 1000.00, 30],
        ["E6,E3", "B46.0006", "Razer Iskur", "Silla Razer", 750.00, 1100.00, 30]
    ],
    "Rack F (Audifonos)": [
        ["F1,F1", "B72.0005", "HyperX Cloud Stinger", "HyperX", 500.00, 700.00, 50],
        ["F2,F1", "B72.0006", "Redragon Ares H120", "Redragon", 450.00, 650.00, 50],
        ["F1,F2", "B72.0007", "Razer Kraken X", "Razer", 600.00, 900.00, 50],
        ["F2,F2", "B72.0008", "Corsair HS60 Pro", "Corsair", 550.00, 850.00, 50],
        ["F1,F3", "B72.0009", "SteelSeries Arctis Nova Pro Wireless", "SteelSeries", 700.00, 1000.00, 50],
        ["F2,F3", "B72.0010", "Logitech G Pro X Wireless", "Logitech", 750.00, 1100.00, 50]
    ],
    "Rack E (Impresoras)": [
        ["E5,E1", "BZA.0012", "HP DeskJet 2755e", "Impresora HP", 500.00, 700.00, 30],
        ["E6,E1", "BZA.0013", "Canon PIXMA MG2522", "Impresora Canon", 450.00, 650.00, 30],
        ["E5,E2", "BZA.0014", "Brother MFC-J4535DW", "Impresora Brother", 600.00, 900.00, 30],
        ["E6,E2", "BZA.0015", "Epson EcoTank ET-3850", "Impresora Epson", 550.00, 850.00, 30],
        ["E5,E3", "BZA.0016", "HP Color LaserJet Pro MFP M479fdw", "Impresora HP", 700.00, 1000.00, 30],
        ["E6,E3", "BZA.0017", "Canon imageCLASS MF743Cdw", "Impresora Canon", 750.00, 1100.00, 30]
    ],
    "Rack E (Router)": [
        ["E5,E1", "B68.0008", "TP-Link Archer C7", "Router TP-Link", 500.00, 700.00, 30],
        ["E6,E1", "B68.0009", "Tenda AC6", "Router Tenda", 450.00, 650.00, 30],
        ["E5,E2", "B68.0010", "ASUS RT-AC86U", "Router ASUS", 600.00, 900.00, 30],
        ["E6,E2", "B68.0011", "Netgear Nighthawk AX4", "Router Netgear", 550.00, 850.00, 30],
        ["E5,E3", "B68.0012", "ASUS ROG Rapture GT-AX11000", "Router ASUS", 700.00, 1000.00, 30],
        ["E6,E3", "B68.0013", "Netgear Nighthawk XR1000", "Router Netgear", 750.00, 1100.00, 30]
    ],
}

# Lista global para almacenar los P/N, descripción y cantidad generados en ventas
manufactured_pns = []

# Función de inicio de sesión
def login(event=None):
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        open_main_window()
    else:
        messagebox.showerror("Login", "Usuario o contraseña incorrectos")

# Función para abrir la ventana principal
def open_main_window():
    global main_window  # Declaramos main_window como global para acceder a ella después
    if 'root' in globals():
        root.withdraw()  # Ocultar la ventana de inicio de sesión en lugar de destruirla

    main_window = tk.Tk()
    main_window.title("Gestión de Almacén")
    main_window.geometry("400x300")
    main_window.configure(bg="white")

    font_style = ("Times New Roman", 14)

    stock_button = tk.Button(main_window, text="Stock de almacén", font=font_style, command=open_stock_window)
    stock_button.pack(pady=10)

    purchase_button = tk.Button(main_window, text="Compra de material", font=font_style, command=open_purchase_window)
    purchase_button.pack(pady=10)

    sale_button = tk.Button(main_window, text="Venta de material", font=font_style, command=open_sale_window)
    sale_button.pack(pady=10)

    # Botón para Manufactura
    manufacture_button = tk.Button(main_window, text="Manufactura", font=font_style, command=open_manufacture_window)
    manufacture_button.pack(pady=10)

    exit_button = tk.Button(main_window, text="Salir", font=font_style, command=main_window.destroy)
    exit_button.pack(pady=10)

    main_window.mainloop()  # Ejecutar la ventana principal

# Función para abrir la ventana de manufactura
def open_manufacture_window():
    if 'main_window' in globals():
        main_window.withdraw()

    manufacture_window = tk.Tk()
    manufacture_window.title("Manufactura")
    manufacture_window.geometry("800x600")
    manufacture_window.configure(bg="white")

    font_style = ("Times New Roman", 14)

    # Título
    label = tk.Label(manufacture_window, 
                    text="Lista de P/N generados en ventas",
                    font=("Times New Roman", 16, "bold"),
                    bg="white")
    label.pack(pady=10)

    # Crear un Treeview para mostrar los P/N, descripción y cantidad
    columns = ("P/N", "Descripción", "Cantidad", "Locación")
    treeview = ttk.Treeview(manufacture_window, columns=columns, show="headings")

    for col in columns:
        treeview.heading(col, text=col, anchor="center")
        treeview.column(col, anchor="center")

    # Llenar el Treeview con los datos de manufactured_pns
    for pn, description, quantity, location in manufactured_pns:
        treeview.insert("", "end", values=(pn, description, quantity, location))

    treeview.pack(expand=True, fill="both", padx=10, pady=10)

    # Función para generar un archivo .txt con la lista de componentes
    def generate_report():
        if manufactured_pns:
            report = "=== Reporte de Manufactura ===\n"
            report += "P/N\tDescripción\tCantidad\tLocación\n"
            for pn, description, quantity, location in manufactured_pns:
                report += f"{pn}\t{description}\t{quantity}\t{location}\n"

            # Especificar una ruta absoluta para guardar el archivo
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Ruta al escritorio
            file_path = os.path.join(desktop_path, "reporte_manufactura.txt")  # Ruta completa del archivo

            try:
                # Guardar el reporte en un archivo .txt
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(report)
                messagebox.showinfo("Reporte Generado", f"Reporte generado y guardado en '{file_path}'")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
        else:
            messagebox.showwarning("Reporte Vacío", "No hay componentes para generar el reporte.")

    # Botón para generar el reporte
    generate_report_button = tk.Button(manufacture_window,
                                      text="Generar Reporte",
                                      font=font_style,
                                      command=generate_report)
    generate_report_button.pack(pady=10)

    # Botón de regreso
    return_button = tk.Button(manufacture_window,
                            text="Regresar",
                            font=font_style,
                            command=lambda: return_to_main(manufacture_window))
    return_button.pack(pady=10)

    manufacture_window.mainloop()

# Función para abrir la ventana de stock de materiales
def open_stock_window():
    if 'main_window' in globals():
        main_window.withdraw()  # Ocultar la ventana principal antes de abrir la nueva

    stock_window = tk.Tk()
    stock_window.title("Stock de Materiales")
    stock_window.geometry("1000x600")
    stock_window.configure(bg="white")

    font_style = ("Times New Roman", 14)

    # Añadir marco de búsqueda
    search_frame = tk.Frame(stock_window)
    search_frame.pack(fill="x", padx=10, pady=5)

    tk.Label(search_frame, text="Buscar por P/N:", font=font_style).pack(side="left")
    search_entry = tk.Entry(search_frame, font=font_style)
    search_entry.pack(side="left", padx=5)

    def search(event=None):
        query = search_entry.get().strip().lower()
        for item in treeview.get_children():
            treeview.item(item, tags=())
            for child in treeview.get_children(item):
                if query in treeview.item(child)["values"][1].lower():  # Buscar por P/N (segunda columna)
                    treeview.item(child, tags=("highlight",))
                else:
                    treeview.item(child, tags=())

    search_button = tk.Button(search_frame, text="Buscar", font=font_style, command=search)
    search_button.pack(side="left", padx=5)

    # Vincular la tecla Enter con el campo de búsqueda
    search_entry.bind("<Return>", search)

    columns = ("Locación", "P/N", "Modelo", "Descripción", "Precio de Compra", "Precio de Venta", "Cantidad")
    treeview = ttk.Treeview(stock_window, columns=columns, show="tree headings")

    # Añadimos el Scrollbar
    scrollbar = ttk.Scrollbar(stock_window, orient="vertical", command=treeview.yview)
    treeview.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    for col in columns:
        treeview.heading(col, text=col, anchor="center")
        treeview.column(col, anchor="center")

    for rack, items in stock_data.items():
        parent = treeview.insert("", "end", text=rack)
        for item in items:
            treeview.insert(parent, "end", values=item)

    treeview.pack(expand=True, fill="both")

    # Configurar el color de resaltado
    treeview.tag_configure("highlight", background="yellow")

    # Botón para regresar a la ventana principal
    return_button = tk.Button(stock_window, text="Regresar", font=font_style, command=lambda: return_to_main(stock_window))
    return_button.pack(pady=10)

    exit_button = tk.Button(stock_window, text="Salir", font=font_style, command=stock_window.destroy)
    exit_button.pack(pady=10)

    stock_window.mainloop()  # Ejecutar la ventana de stock de materiales

# Función para abrir la ventana de compra de material
def open_purchase_window():
    if 'main_window' in globals():
        main_window.withdraw()  # Ocultar la ventana principal antes de abrir la nueva

    purchase_window = tk.Tk()
    purchase_window.title("Compra de Material")
    purchase_window.geometry("800x600")
    purchase_window.configure(bg="white")

    font_style = ("Times New Roman", 14)

    # Lista para almacenar los materiales seleccionados
    selected_materials = []

    # Función para buscar materiales por P/N
    def search_material(event=None):
        query = search_entry.get().strip().lower()
        for item in treeview.get_children():
            treeview.item(item, tags=())
            for child in treeview.get_children(item):
                if query in treeview.item(child)["values"][1].lower():  # Buscar por P/N (segunda columna)
                    treeview.item(child, tags=("highlight",))
                else:
                    treeview.item(child, tags=())

    # Función para agregar materiales seleccionados a la lista
    def add_material():
        selected_item = treeview.selection()
        if selected_item:
            item_values = treeview.item(selected_item)["values"]
            location = item_values[0]  # Locación
            pn = item_values[1]  # P/N
            description = item_values[3]  # Descripción
            price = float(item_values[4])  # Precio de compra

            # Pedir la cantidad al usuario
            quantity = simpledialog.askinteger("Cantidad", f"Ingrese la cantidad para {pn} ({description}):", parent=purchase_window, minvalue=1)
            if quantity:
                total_cost = price * quantity
                selected_materials.append((location, pn, description, quantity, price, total_cost))
                update_selected_materials_list()

    # Función para actualizar la lista de materiales seleccionados
    def update_selected_materials_list():
        selected_listbox.delete(0, tk.END)
        total = 0
        for material in selected_materials:
            location, pn, description, quantity, price, total_cost = material
            selected_listbox.insert(tk.END, f"{location} - {pn} - {description} - Cantidad: {quantity} - Precio Unitario: ${price:.2f} - Total: ${total_cost:.2f}")
            total += total_cost
        total_label.config(text=f"Total de la compra: ${total:.2f}")

    # Función para generar el ticket y guardarlo en un archivo .txt
    def generate_ticket():
        if selected_materials:
            ticket = "=== Ticket de Compra ===\n"
            for material in selected_materials:
                location, pn, description, quantity, price, total_cost = material
                ticket += f"{location} - {pn} - {description} - Cantidad: {quantity} - Precio Unitario: ${price:.2f} - Total: ${total_cost:.2f}\n"

                # Actualizar el stock del material comprado
                for rack, items in stock_data.items():
                    for item in items:
                        if item[1] == pn:  # Buscar por P/N
                            item[6] += quantity  # Aumentar la cantidad en stock
                            break

            ticket += f"\nTotal de la compra: ${sum(m[5] for m in selected_materials):.2f}"

            # Especificar una ruta absoluta para guardar el archivo
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Ruta al escritorio
            file_path = os.path.join(desktop_path, "ticket_compra.txt")  # Ruta completa del archivo

            try:
                # Guardar el ticket en un archivo .txt
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(ticket)
                messagebox.showinfo("Ticket de Compra", f"Ticket generado y guardado en '{file_path}'")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
        else:
            messagebox.showwarning("Ticket de Compra", "No se han seleccionado materiales para comprar.")

    # Añadir marco de búsqueda
    search_frame = tk.Frame(purchase_window)
    search_frame.pack(fill="x", padx=10, pady=5)

    tk.Label(search_frame, text="Buscar por P/N:", font=font_style).pack(side="left")
    search_entry = tk.Entry(search_frame, font=font_style)
    search_entry.pack(side="left", padx=5)

    search_button = tk.Button(search_frame, text="Buscar", font=font_style, command=search_material)
    search_button.pack(side="left", padx=5)

    # Vincular la tecla Enter con el campo de búsqueda
    search_entry.bind("<Return>", search_material)

    # Crear un Treeview para mostrar los materiales disponibles
    columns = ("Locación", "P/N", "Modelo", "Descripción", "Precio de Compra", "Precio de Venta", "Cantidad")
    treeview = ttk.Treeview(purchase_window, columns=columns, show="tree headings")

    for col in columns:
        treeview.heading(col, text=col, anchor="center")
        treeview.column(col, anchor="center")

    for rack, items in stock_data.items():
        parent = treeview.insert("", "end", text=rack)
        for item in items:
            treeview.insert(parent, "end", values=item)

    treeview.pack(expand=True, fill="both", padx=10, pady=10)

    # Configurar el color de resaltado
    treeview.tag_configure("highlight", background="yellow")

    # Listbox para mostrar los materiales seleccionados
    selected_listbox = tk.Listbox(purchase_window, font=font_style)
    selected_listbox.pack(expand=True, fill="both", padx=10, pady=10)

    # Etiqueta para mostrar el total de la compra
    total_label = tk.Label(purchase_window, text="Total de la compra: $0.00", font=font_style, bg="white")
    total_label.pack(pady=5)

    # Frame para agrupar los botones
    button_frame = tk.Frame(purchase_window)
    button_frame.pack(pady=10)

    # Botón para agregar material seleccionado
    add_button = tk.Button(button_frame, text="Agregar Material", font=font_style, command=add_material)
    add_button.pack(side="left", padx=5)

    # Botón para generar el ticket
    generate_ticket_button = tk.Button(button_frame, text="Generar Ticket", font=font_style, command=generate_ticket)
    generate_ticket_button.pack(side="left", padx=5)

    # Botón para regresar a la ventana principal
    return_button = tk.Button(button_frame, text="Regresar", font=font_style, command=lambda: return_to_main(purchase_window))
    return_button.pack(side="left", padx=5)

    purchase_window.mainloop()

# Función para abrir la ventana de venta de material
def open_sale_window():
    if 'main_window' in globals():
        main_window.withdraw()  # Ocultar la ventana principal antes de abrir la nueva

    sale_window = tk.Tk()
    sale_window.title("Venta de Material")
    sale_window.geometry("800x600")
    sale_window.configure(bg="white")

    font_style = ("Times New Roman", 14)

    # Lista para almacenar los materiales seleccionados
    selected_materials = []

    # Costo de envío fijo
    shipping_cost = 99.00

    # Función para buscar materiales por P/N
    def search_material(event=None):
        query = search_entry.get().strip().lower()
        for item in treeview.get_children():
            treeview.item(item, tags=())
            for child in treeview.get_children(item):
                if query in treeview.item(child)["values"][1].lower():  # Buscar por P/N (segunda columna)
                    treeview.item(child, tags=("highlight",))
                else:
                    treeview.item(child, tags=())

    # Función para agregar materiales seleccionados a la lista
    def add_material():
        selected_item = treeview.selection()
        if selected_item:
            item_values = treeview.item(selected_item)["values"]
            location = item_values[0]  # Locación
            pn = item_values[1]  # P/N
            description = item_values[3]  # Descripción
            price = float(item_values[5])  # Precio de venta

            # Pedir la cantidad al usuario
            quantity = simpledialog.askinteger("Cantidad", f"Ingrese la cantidad para {pn} ({description}):", parent=sale_window, minvalue=1)
            if quantity:
                # Verificar si hay suficiente stock
                for rack, items in stock_data.items():
                    for item in items:
                        if item[1] == pn:  # Buscar por P/N
                            if item[6] >= quantity:
                                total_cost = price * quantity
                                selected_materials.append((location, pn, description, quantity, price, total_cost))
                                item[6] -= quantity  # Reducir el stock
                                update_selected_materials_list()
                                manufactured_pns.append((pn, description, quantity, location))  # Registrar el P/N, descripción, cantidad y locación
                            else:
                                messagebox.showwarning("Stock Insuficiente", f"No hay suficiente stock para {pn} ({description}). Stock disponible: {item[6]}")
                            break

    # Función para actualizar la lista de materiales seleccionados
    def update_selected_materials_list():
        selected_listbox.delete(0, tk.END)
        subtotal = 0
        for material in selected_materials:
            location, pn, description, quantity, price, total_cost = material
            selected_listbox.insert(tk.END, f"{location} - {pn} - {description} - Cantidad: {quantity} - Precio Unitario: ${price:.2f} - Total: ${total_cost:.2f}")
            subtotal += total_cost

        # Calcular el total incluyendo el costo de envío
        total = subtotal + shipping_cost
        subtotal_label.config(text=f"Subtotal: ${subtotal:.2f}")
        shipping_label.config(text=f"Costo de envío: ${shipping_cost:.2f}")
        total_label.config(text=f"Total (incluye envío): ${total:.2f}")

    # Función para generar la orden de venta y guardarla en un archivo .txt
    def generate_sale_order():
        if selected_materials:
            order = "=== Orden de Venta ===\n"
            for material in selected_materials:
                location, pn, description, quantity, price, total_cost = material
                order += f"{location} - {pn} - {description} - Cantidad: {quantity} - Precio Unitario: ${price:.2f} - Total: ${total_cost:.2f}\n"

            # Agregar el costo de envío a la orden
            order += f"\nSubtotal: ${sum(m[5] for m in selected_materials):.2f}"
            order += f"\nCosto de envío: ${shipping_cost:.2f}"
            order += f"\nTotal (incluye envío): ${sum(m[5] for m in selected_materials) + shipping_cost:.2f}"

            # Especificar una ruta absoluta para guardar el archivo
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Ruta al escritorio
            file_path = os.path.join(desktop_path, "orden_venta.txt")  # Ruta completa del archivo

            try:
                # Guardar la orden en un archivo .txt
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(order)
                messagebox.showinfo("Orden de Venta", f"Orden generada y guardada en '{file_path}'")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
        else:
            messagebox.showwarning("Orden de Venta", "No se han seleccionado materiales para vender.")

    # Añadir marco de búsqueda
    search_frame = tk.Frame(sale_window)
    search_frame.pack(fill="x", padx=10, pady=5)

    tk.Label(search_frame, text="Buscar por P/N:", font=font_style).pack(side="left")
    search_entry = tk.Entry(search_frame, font=font_style)
    search_entry.pack(side="left", padx=5)

    search_button = tk.Button(search_frame, text="Buscar", font=font_style, command=search_material)
    search_button.pack(side="left", padx=5)

    # Vincular la tecla Enter con el campo de búsqueda
    search_entry.bind("<Return>", search_material)

    # Crear un Treeview para mostrar los materiales disponibles
    columns = ("Locación", "P/N", "Modelo", "Descripción", "Precio de Compra", "Precio de Venta", "Cantidad")
    treeview = ttk.Treeview(sale_window, columns=columns, show="tree headings")

    for col in columns:
        treeview.heading(col, text=col, anchor="center")
        treeview.column(col, anchor="center")

    for rack, items in stock_data.items():
        parent = treeview.insert("", "end", text=rack)
        for item in items:
            treeview.insert(parent, "end", values=item)

    treeview.pack(expand=True, fill="both", padx=10, pady=10)

    # Configurar el color de resaltado
    treeview.tag_configure("highlight", background="yellow")

    # Listbox para mostrar los materiales seleccionados
    selected_listbox = tk.Listbox(sale_window, font=font_style)
    selected_listbox.pack(expand=True, fill="both", padx=10, pady=10)

    # Etiqueta para mostrar el subtotal
    subtotal_label = tk.Label(sale_window, text="Subtotal: $0.00", font=font_style, bg="white")
    subtotal_label.pack(pady=5)

    # Etiqueta para mostrar el costo de envío
    shipping_label = tk.Label(sale_window, text=f"Costo de envío: ${shipping_cost:.2f}", font=font_style, bg="white")
    shipping_label.pack(pady=5)

    # Etiqueta para mostrar el total (incluye envío)
    total_label = tk.Label(sale_window, text="Total (incluye envío): $0.00", font=font_style, bg="white")
    total_label.pack(pady=5)

    # Frame para agrupar los botones
    button_frame = tk.Frame(sale_window)
    button_frame.pack(pady=10)

    # Botón para agregar material seleccionado
    add_button = tk.Button(button_frame, text="Agregar Material", font=font_style, command=add_material)
    add_button.pack(side="left", padx=5)

    # Botón para generar la orden de venta
    generate_order_button = tk.Button(button_frame, text="Generar Orden de Venta", font=font_style, command=generate_sale_order)
    generate_order_button.pack(side="left", padx=5)

    # Botón para regresar a la ventana principal
    return_button = tk.Button(button_frame, text="Regresar", font=font_style, command=lambda: return_to_main(sale_window))
    return_button.pack(side="left", padx=5)

    sale_window.mainloop()

# Función para regresar a la ventana principal
def return_to_main(current_window):
    current_window.destroy()  # Cerrar la ventana actual
    if 'main_window' in globals():
        main_window.deiconify()  # Mostrar la ventana principal

# Crear ventana de inicio de sesión
root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("400x250")  # Tamaño de la ventana
root.configure(bg="white")  # Fondo blanco

font_style = ("Times New Roman", 14)

# Crear y colocar etiquetas y entradas
label_username = tk.Label(root, text="Nombre de usuario", bg="white", font=font_style)
label_username.pack(pady=5)
entry_username = tk.Entry(root, font=font_style)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Contraseña", bg="white", font=font_style)
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*", font=font_style)
entry_password.pack(pady=5)

# Botón de inicio de sesión
login_button = tk.Button(root, text="Iniciar sesión", font=font_style, command=login)
login_button.pack(pady=10)

# Configurar tecla Enter para iniciar sesión
root.bind('<Return>', login)

# Ejecutar la aplicación
root.mainloop()