class Material:
    def __init__(self, id_material, nombre, cantidad, ubicacion, proveedor=None):
        self.id_material = id_material
        self.nombre = nombre
        self.cantidad = cantidad
        self.ubicacion = ubicacion
        self.proveedor = proveedor
    
    def __str__(self):
        return f"ID: {self.id_material} | Material: {self.nombre} | Cantidad: {self.cantidad} | Ubicación: {self.ubicacion}"

class SistemaGestionMateriales:
    def __init__(self):
        self.materiales = []
        self.contador_id = 1
    
    def agregar_material(self, nombre, cantidad, ubicacion, proveedor=None):
        nuevo_material = Material(self.contador_id, nombre, cantidad, ubicacion, proveedor)
        self.materiales.append(nuevo_material)
        self.contador_id += 1
        print(f"Material '{nombre}' agregado correctamente.")
    
    def buscar_material(self, criterio, valor):
        resultados = []
        for material in self.materiales:
            if criterio == "id" and material.id_material == valor:
                return [material]
            elif criterio == "nombre" and valor.lower() in material.nombre.lower():
                resultados.append(material)
            elif criterio == "ubicacion" and valor.lower() in material.ubicacion.lower():
                resultados.append(material)
        return resultados
    
    def modificar_material(self, id_material, **kwargs):
        for material in self.materiales:
            if material.id_material == id_material:
                for key, value in kwargs.items():
                    if hasattr(material, key):
                        setattr(material, key, value)
                print(f"Material ID {id_material} modificado correctamente.")
                return
        print(f"No se encontró material con ID {id_material}.")
    
    def eliminar_material(self, id_material):
        for i, material in enumerate(self.materiales):
            if material.id_material == id_material:
                del self.materiales[i]
                print(f"Material ID {id_material} eliminado correctamente.")
                return
        print(f"No se encontró material con ID {id_material}.")
    
    def generar_informe(self):
        print("\n--- INFORME DE MATERIALES ---")
        print(f"Total de materiales registrados: {len(self.materiales)}")
        print("\nListado de materiales:")
        for material in self.materiales:
            print(material)
        print("-----------------------------\n")

    def menu_principal(self):
        while True:
            print("\nSISTEMA DE GESTIÓN DE MATERIALES")
            print("1. Agregar nuevo material")
            print("2. Buscar material")
            print("3. Modificar material")
            print("4. Eliminar material")
            print("5. Generar informe")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                nombre = input("Nombre del material: ")
                cantidad = int(input("Cantidad: "))
                ubicacion = input("Ubicación: ")
                proveedor = input("Proveedor (opcional): ") or None
                self.agregar_material(nombre, cantidad, ubicacion, proveedor)
            
            elif opcion == "2":
                print("\nBuscar por:")
                print("1. ID")
                print("2. Nombre")
                print("3. Ubicación")
                sub_opcion = input("Seleccione criterio de búsqueda: ")
                
                if sub_opcion == "1":
                    id_busqueda = int(input("Ingrese ID: "))
                    resultados = self.buscar_material("id", id_busqueda)
                elif sub_opcion == "2":
                    nombre_busqueda = input("Ingrese nombre: ")
                    resultados = self.buscar_material("nombre", nombre_busqueda)
                elif sub_opcion == "3":
                    ubicacion_busqueda = input("Ingrese ubicación: ")
                    resultados = self.buscar_material("ubicacion", ubicacion_busqueda)
                else:
                    print("Opción no válida.")
                    continue
                
                if resultados:
                    print("\nResultados de la búsqueda:")
                    for material in resultados:
                        print(material)
                else:
                    print("No se encontraron resultados.")
            
            elif opcion == "3":
                id_modificar = int(input("Ingrese ID del material a modificar: "))
                print("Deje en blanco los campos que no desea modificar")
                nombre = input("Nuevo nombre: ") or None
                cantidad = input("Nueva cantidad: ") or None
                ubicacion = input("Nueva ubicación: ") or None
                proveedor = input("Nuevo proveedor: ") or None
                
                cambios = {}
                if nombre: cambios["nombre"] = nombre
                if cantidad: cambios["cantidad"] = int(cantidad)
                if ubicacion: cambios["ubicacion"] = ubicacion
                if proveedor: cambios["proveedor"] = proveedor
                
                if cambios:
                    self.modificar_material(id_modificar, **cambios)
                else:
                    print("No se especificaron cambios.")
            
            elif opcion == "4":
                id_eliminar = int(input("Ingrese ID del material a eliminar: "))
                confirmacion = input(f"¿Está seguro de eliminar el material ID {id_eliminar}? (s/n): ")
                if confirmacion.lower() == "s":
                    self.eliminar_material(id_eliminar)
            
            elif opcion == "5":
                self.generar_informe()
            
            elif opcion == "6":
                print("Saliendo del sistema...")
                break
            
            else:
                print("Opción no válida. Intente nuevamente.")

# Ejecutar el sistema
if __name__ == "__main__":
    sistema = SistemaGestionMateriales()
    sistema.menu_principal()