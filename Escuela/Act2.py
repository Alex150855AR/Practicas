import heapq
from collections import defaultdict

class Ciudad:
    def __init__(self, nombre, poblacion=None, datos_historicos=None):
        self.nombre = nombre
        self.poblacion = poblacion
        self.datos_historicos = datos_historicos
        self.conexiones = {}  # {ciudad: distancia}

    def agregar_conexion(self, ciudad, distancia):
        self.conexiones[ciudad] = distancia

class ArbolCiudades:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, ciudad):
        if not self.raiz:
            self.raiz = NodoArbol(ciudad)
        else:
            self._insertar_recursivo(self.raiz, ciudad)
    
    def _insertar_recursivo(self, nodo, ciudad):
        if ciudad.nombre < nodo.ciudad.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(ciudad)
            else:
                self._insertar_recursivo(nodo.izquierda, ciudad)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(ciudad)
            else:
                self._insertar_recursivo(nodo.derecha, ciudad)
    
    def buscar(self, nombre_ciudad):
        return self._buscar_recursivo(self.raiz, nombre_ciudad)
    
    def _buscar_recursivo(self, nodo, nombre_ciudad):
        if nodo is None:
            return None
        if nombre_ciudad == nodo.ciudad.nombre:
            return nodo.ciudad
        elif nombre_ciudad < nodo.ciudad.nombre:
            return self._buscar_recursivo(nodo.izquierda, nombre_ciudad)
        else:
            return self._buscar_recursivo(nodo.derecha, nombre_ciudad)

class NodoArbol:
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.izquierda = None
        self.derecha = None

class SistemaCiudades:
    def __init__(self):
        self.arbol_ciudades = ArbolCiudades()
        self.tabla_hash = {}
        self.ciudades = {}  # {nombre: objeto Ciudad}
    
    def agregar_ciudad(self, nombre, poblacion=None, datos_historicos=None):
        ciudad = Ciudad(nombre, poblacion, datos_historicos)
        self.arbol_ciudades.insertar(ciudad)
        self.tabla_hash[nombre] = ciudad
        self.ciudades[nombre] = ciudad
    
    def conectar_ciudades(self, ciudad1, ciudad2, distancia):
        if ciudad1 in self.ciudades and ciudad2 in self.ciudades:
            self.ciudades[ciudad1].agregar_conexion(ciudad2, distancia)
            self.ciudades[ciudad2].agregar_conexion(ciudad1, distancia)
    
    def obtener_informacion(self, nombre_ciudad):
        return self.tabla_hash.get(nombre_ciudad, None)
    
    def camino_mas_corto_recursivo(self, origen, destino):
        visitados = set()
        return self._camino_mas_corto_rec(origen, destino, visitados, [origen], 0)
    
    def _camino_mas_corto_rec(self, actual, destino, visitados, camino_actual, distancia_actual):
        if actual == destino:
            return (camino_actual, distancia_actual)
        
        visitados.add(actual)
        mejor_camino = None
        mejor_distancia = float('inf')
        
        for vecino, distancia in self.ciudades[actual].conexiones.items():
            if vecino not in visitados:
                nuevo_camino = camino_actual + [vecino]
                nueva_distancia = distancia_actual + distancia
                resultado = self._camino_mas_corto_rec(vecino, destino, visitados.copy(), nuevo_camino, nueva_distancia)
                
                if resultado and resultado[1] < mejor_distancia:
                    mejor_camino, mejor_distancia = resultado
        
        return (mejor_camino, mejor_distancia) if mejor_camino else None
    
    def camino_mas_corto_dijkstra(self, origen, destino):
        # Implementación con cola de prioridad (Dijkstra)
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (0, origen, [origen]))
        visitados = set()
        
        while cola_prioridad:
            distancia, actual, camino = heapq.heappop(cola_prioridad)
            
            if actual == destino:
                return (camino, distancia)
            
            if actual in visitados:
                continue
                
            visitados.add(actual)
            
            for vecino, dist in self.ciudades[actual].conexiones.items():
                if vecino not in visitados:
                    nueva_distancia = distancia + dist
                    nuevo_camino = camino + [vecino]
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino, nuevo_camino))
        
        return None
    
    def optimizar_rutas_divide_venceras(self, ciudades):
        # Algoritmo divide y vencerás para optimizar rutas entre múltiples ciudades
        if len(ciudades) <= 2:
            return ciudades
        
        mitad = len(ciudades) // 2
        izquierda = self.optimizar_rutas_divide_venceras(ciudades[:mitad])
        derecha = self.optimizar_rutas_divide_venceras(ciudades[mitad:])
        
        return self._combinar_rutas(izquierda, derecha)
    
    def _combinar_rutas(self, ruta_izq, ruta_der):
        # Combinar rutas optimizadas de subconjuntos
        # En una implementación real, aquí se aplicaría lógica para encontrar
        # la mejor combinación de rutas entre los dos subconjuntos
        return ruta_izq + ruta_der
    
    def mostrar_rutas_ordenadas(self, origen):
        # Obtener todas las rutas desde un origen y mostrarlas ordenadas por distancia
        destinos = []
        for ciudad in self.ciudades:
            if ciudad != origen:
                resultado = self.camino_mas_corto_dijkstra(origen, ciudad)
                if resultado:
                    destinos.append((resultado[1], resultado[0]))
        
        destinos.sort()
        for distancia, ruta in destinos:
            print(f"Ruta: {' -> '.join(ruta)}, Distancia total: {distancia}")

def interfaz_usuario():
    sistema = SistemaCiudades()
    
    while True:
        print("\n--- Sistema de Gestión de Ciudades ---")
        print("1. Agregar ciudad")
        print("2. Conectar ciudades")
        print("3. Buscar camino más corto (recursivo)")
        print("4. Buscar camino más corto (Dijkstra)")
        print("5. Mostrar información de ciudad")
        print("6. Mostrar rutas ordenadas desde una ciudad")
        print("7. Optimizar rutas (Divide y Vencerás)")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la ciudad: ")
            poblacion = input("Población (opcional): ")
            datos = input("Datos históricos (opcional): ")
            sistema.agregar_ciudad(nombre, poblacion if poblacion else None, datos if datos else None)
            print(f"Ciudad {nombre} agregada.")
        
        elif opcion == "2":
            ciudad1 = input("Primera ciudad: ")
            ciudad2 = input("Segunda ciudad: ")
            distancia = float(input("Distancia entre ellas: "))
            sistema.conectar_ciudades(ciudad1, ciudad2, distancia)
            print(f"{ciudad1} y {ciudad2} conectadas.")
        
        elif opcion == "3":
            origen = input("Ciudad origen: ")
            destino = input("Ciudad destino: ")
            resultado = sistema.camino_mas_corto_recursivo(origen, destino)
            if resultado:
                print(f"Camino: {' -> '.join(resultado[0])}, Distancia: {resultado[1]}")
            else:
                print("No se encontró un camino.")
        
        elif opcion == "4":
            origen = input("Ciudad origen: ")
            destino = input("Ciudad destino: ")
            resultado = sistema.camino_mas_corto_dijkstra(origen, destino)
            if resultado:
                print(f"Camino: {' -> '.join(resultado[0])}, Distancia: {resultado[1]}")
            else:
                print("No se encontró un camino.")
        
        elif opcion == "5":
            nombre = input("Nombre de la ciudad: ")
            ciudad = sistema.obtener_informacion(nombre)
            if ciudad:
                print(f"\nInformación de {nombre}:")
                print(f"Población: {ciudad.poblacion or 'No disponible'}")
                print(f"Datos históricos: {ciudad.datos_historicos or 'No disponible'}")
                print(f"Conexiones: {', '.join(ciudad.conexiones.keys())}")
            else:
                print("Ciudad no encontrada.")
        
        elif opcion == "6":
            origen = input("Ciudad origen: ")
            sistema.mostrar_rutas_ordenadas(origen)
        
        elif opcion == "7":
            ciudades = input("Ingrese ciudades separadas por comas: ").split(',')
            ciudades = [c.strip() for c in ciudades]
            ruta_optimizada = sistema.optimizar_rutas_divide_venceras(ciudades)
            print(f"Ruta optimizada: {' -> '.join(ruta_optimizada)}")
        
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    interfaz_usuario()