import heapq
from datetime import datetime
from collections import defaultdict

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_limite, duracion_estimada=1):
        self.descripcion = descripcion
        self.prioridad = prioridad  # 1-10 (10 es más urgente)
        self.fecha_limite = datetime.strptime(fecha_limite, "%Y-%m-%d") if isinstance(fecha_limite, str) else fecha_limite
        self.duracion_estimada = duracion_estimada  # en horas
        self.dependencias = []  # para el grafo de dependencias
    
    def __lt__(self, other):
        # Comparación para la cola de prioridad
        if self.prioridad == other.prioridad:
            return self.fecha_limite < other.fecha_limite
        return self.prioridad > other.prioridad
    
    def __repr__(self):
        return f"{self.descripcion} (Prioridad: {self.prioridad}, Fecha límite: {self.fecha_limite.strftime('%Y-%m-%d')})"

class NodoEmpleado:
    def __init__(self, id_empleado, nombre, departamento):
        self.id = id_empleado
        self.nombre = nombre
        self.departamento = departamento
        self.left = None
        self.right = None

class ArbolEmpleados:
    def __init__(self):
        self.root = None
    
    def insert(self, id_empleado, nombre, departamento):
        if not self.root:
            self.root = NodoEmpleado(id_empleado, nombre, departamento)
        else:
            self._insert(self.root, id_empleado, nombre, departamento)
    
    def _insert(self, nodo, id_empleado, nombre, departamento):
        if id_empleado < nodo.id:
            if nodo.left is None:
                nodo.left = NodoEmpleado(id_empleado, nombre, departamento)
            else:
                self._insert(nodo.left, id_empleado, nombre, departamento)
        else:
            if nodo.right is None:
                nodo.right = NodoEmpleado(id_empleado, nombre, departamento)
            else:
                self._insert(nodo.right, id_empleado, nombre, departamento)
    
    def buscar_por_departamento(self, departamento):
        empleados = []
        self._buscar_departamento(self.root, departamento, empleados)
        return empleados
    
    def _buscar_departamento(self, nodo, departamento, empleados):
        if nodo:
            if nodo.departamento == departamento:
                empleados.append((nodo.id, nodo.nombre))
            self._buscar_departamento(nodo.left, departamento, empleados)
            self._buscar_departamento(nodo.right, departamento, empleados)

class GrafoDependencias:
    def __init__(self):
        self.grafo = defaultdict(list)
    
    def agregar_tarea(self, tarea):
        self.grafo[tarea] = []
    
    def agregar_dependencia(self, tarea, dependencia):
        if tarea in self.grafo and dependencia in self.grafo:
            self.grafo[tarea].append(dependencia)
    
    def obtener_dependencias(self, tarea):
        return self.grafo.get(tarea, [])
    
    def todas_tareas(self):
        return list(self.grafo.keys())

class ColaPrioridad:
    def __init__(self):
        self.heap = []
    
    def push(self, tarea):
        heapq.heappush(self.heap, tarea)
    
    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)
    
    def mostrar_tareas(self):
        print("\n--- Tareas por Prioridad ---")
        if self.is_empty():
            print("No hay tareas en la cola de prioridad.")
        else:
            # Mostrar ordenadas sin modificar el heap
            temp = sorted(self.heap, reverse=True)
            for i, tarea in enumerate(temp, 1):
                print(f"{i}. {tarea}")

class HashMapTareas:
    def __init__(self):
        self.size = 100
        self.map = [[] for _ in range(self.size)]
    
    def _get_hash(self, key):
        return hash(key) % self.size
    
    def agregar(self, key, value):
        hash_key = self._get_hash(key)
        bucket = self.map[hash_key]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def obtener(self, key):
        hash_key = self._get_hash(key)
        bucket = self.map[hash_key]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def eliminar(self, key):
        hash_key = self._get_hash(key)
        bucket = self.map[hash_key]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False
    
    def mostrar_todas(self):
        print("\n--- Todas las Tareas (HashMap) ---")
        for bucket in self.map:
            for key, value in bucket:
                print(f"{key}: {value}")

class SistemaGestionTareas:
    def __init__(self):
        self.pila_urgentes = []
        self.cola_programadas = []
        self.lista_departamentos = defaultdict(list)
        self.cola_prioridad = ColaPrioridad()
        self.arbol_empleados = ArbolEmpleados()
        self.grafo_dependencias = GrafoDependencias()
        self.hash_tareas = HashMapTareas()
        self.estadisticas = {
            'total_tareas': 0,
            'horas_totales': 0,
            'tareas_por_departamento': defaultdict(int)
        }
    
    # Métodos para la pila de tareas urgentes
    def agregar_urgente(self, tarea):
        self.pila_urgentes.append(tarea)
        self._actualizar_estadisticas(tarea)
    
    def completar_urgente(self):
        if self.pila_urgentes:
            return self.pila_urgentes.pop()
        return None
    
    # Métodos para la cola de tareas programadas
    def agregar_programada(self, tarea):
        self.cola_programadas.append(tarea)
        self._actualizar_estadisticas(tarea)
    
    def completar_programada(self):
        if self.cola_programadas:
            return self.cola_programadas.pop(0)
        return None
    
    # Métodos para la lista por departamentos
    def agregar_departamento(self, departamento, tarea):
        self.lista_departamentos[departamento].append(tarea)
        self._actualizar_estadisticas(tarea)
    
    def eliminar_departamento(self, departamento, indice):
        if departamento in self.lista_departamentos and 0 <= indice < len(self.lista_departamentos[departamento]):
            return self.lista_departamentos[departamento].pop(indice)
        return None
    
    # Métodos para la cola de prioridad
    def agregar_prioridad(self, tarea):
        self.cola_prioridad.push(tarea)
        self._actualizar_estadisticas(tarea)
    
    def completar_prioridad(self):
        return self.cola_prioridad.pop()
    
    # Métodos para el árbol de empleados
    def agregar_empleado(self, id_empleado, nombre, departamento):
        self.arbol_empleados.insert(id_empleado, nombre, departamento)
    
    def buscar_empleados_departamento(self, departamento):
        return self.arbol_empleados.buscar_por_departamento(departamento)
    
    # Métodos para el grafo de dependencias
    def agregar_tarea_grafo(self, tarea):
        self.grafo_dependencias.agregar_tarea(tarea)
    
    def agregar_dependencia(self, tarea, dependencia):
        self.grafo_dependencias.agregar_dependencia(tarea, dependencia)
    
    def obtener_dependencias(self, tarea):
        return self.grafo_dependencias.obtener_dependencias(tarea)
    
    # Métodos para el hashmap de tareas
    def agregar_hash_tarea(self, key, tarea):
        self.hash_tareas.agregar(key, tarea)
    
    def obtener_hash_tarea(self, key):
        return self.hash_tareas.obtener(key)
    
    # Métodos de estadísticas con recursividad
    def _actualizar_estadisticas(self, tarea):
        self.estadisticas['total_tareas'] += 1
        self.estadisticas['horas_totales'] += tarea.duracion_estimada
        if hasattr(tarea, 'departamento'):
            self.estadisticas['tareas_por_departamento'][tarea.departamento] += 1
    
    def calcular_estadisticas(self):
        print("\n--- Estadísticas de Tareas ---")
        print(f"Total de tareas: {self.estadisticas['total_tareas']}")
        print(f"Horas totales estimadas: {self.estadisticas['horas_totales']}")
        print("\nTareas por departamento:")
        for depto, count in self.estadisticas['tareas_por_departamento'].items():
            print(f"{depto}: {count} tareas")
    
    # Algoritmo divide y vencerás para distribución de tareas
    def distribuir_tareas(self, tareas, empleados):
        if not tareas or not empleados:
            return {}
        
        if len(tareas) == 1:
            return {empleados[0]: tareas}
        
        mitad = len(tareas) // 2
        mitad_empleados = len(empleados) // 2
        
        izquierda = self.distribuir_tareas(tareas[:mitad], empleados[:mitad_empleados])
        derecha = self.distribuir_tareas(tareas[mitad:], empleados[mitad_empleados:])
        
        return {**izquierda, **derecha}
    
    # Métodos de ordenamiento
    def ordenar_tareas_prioridad(self, tareas):
        return sorted(tareas, key=lambda x: (-x.prioridad, x.fecha_limite))
    
    def ordenar_tareas_fecha(self, tareas):
        return sorted(tareas, key=lambda x: x.fecha_limite)
    
    # Métodos de búsqueda
    def buscar_tarea_descripcion(self, descripcion):
        todas_tareas = self.grafo_dependencias.todas_tareas()
        return [t for t in todas_tareas if descripcion.lower() in t.descripcion.lower()]
    
    def buscar_tarea_fecha(self, fecha):
        fecha_busqueda = datetime.strptime(fecha, "%Y-%m-%d")
        todas_tareas = self.grafo_dependencias.todas_tareas()
        return [t for t in todas_tareas if t.fecha_limite.date() == fecha_busqueda.date()]

def mostrar_menu_principal():
    print("\n--- Sistema Avanzado de Gestión de Tareas ---")
    print("1. Gestión de tareas urgentes (Pila)")
    print("2. Gestión de tareas programadas (Cola)")
    print("3. Gestión por departamentos (Lista)")
    print("4. Cola de prioridad de tareas")
    print("5. Árbol de empleados")
    print("6. Grafo de dependencias")
    print("7. HashMap de tareas")
    print("8. Estadísticas y distribución")
    print("9. Ordenamiento y búsqueda")
    print("10. Salir")

def gestionar_pila(sistema):
    while True:
        print("\n--- Gestión de Tareas Urgentes (Pila) ---")
        print("1. Agregar tarea urgente")
        print("2. Completar tarea urgente")
        print("3. Ver tareas urgentes")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            prioridad = int(input("Prioridad (1-10): "))
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            duracion = float(input("Duración estimada (horas): "))
            tarea = Tarea(descripcion, prioridad, fecha, duracion)
            sistema.agregar_urgente(tarea)
            sistema.agregar_tarea_grafo(tarea)
            sistema.agregar_hash_tarea(descripcion, tarea)
            print("Tarea urgente agregada.")
        elif opcion == "2":
            tarea = sistema.completar_urgente()
            if tarea:
                print(f"Tarea completada: {tarea.descripcion}")
            else:
                print("No hay tareas urgentes pendientes.")
        elif opcion == "3":
            print("\nTareas urgentes (última primero):")
            for i, t in enumerate(reversed(sistema.pila_urgentes), 1):
                print(f"{i}. {t}")
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def gestionar_cola(sistema):
    while True:
        print("\n--- Gestión de Tareas Programadas (Cola) ---")
        print("1. Agregar tarea programada")
        print("2. Completar tarea programada")
        print("3. Ver tareas programadas")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            prioridad = int(input("Prioridad (1-10): "))
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            duracion = float(input("Duración estimada (horas): "))
            tarea = Tarea(descripcion, prioridad, fecha, duracion)
            sistema.agregar_programada(tarea)
            sistema.agregar_tarea_grafo(tarea)
            sistema.agregar_hash_tarea(descripcion, tarea)
            print("Tarea programada agregada.")
        elif opcion == "2":
            tarea = sistema.completar_programada()
            if tarea:
                print(f"Tarea completada: {tarea.descripcion}")
            else:
                print("No hay tareas programadas pendientes.")
        elif opcion == "3":
            print("\nTareas programadas (primera primero):")
            for i, t in enumerate(sistema.cola_programadas, 1):
                print(f"{i}. {t}")
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def gestionar_departamentos(sistema):
    while True:
        print("\n--- Gestión por Departamentos ---")
        print("1. Agregar tarea a departamento")
        print("2. Eliminar tarea de departamento")
        print("3. Ver tareas por departamento")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            depto = input("Nombre del departamento: ")
            descripcion = input("Descripción de la tarea: ")
            prioridad = int(input("Prioridad (1-10): "))
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            duracion = float(input("Duración estimada (horas): "))
            tarea = Tarea(descripcion, prioridad, fecha, duracion)
            tarea.departamento = depto
            sistema.agregar_departamento(depto, tarea)
            sistema.agregar_tarea_grafo(tarea)
            sistema.agregar_hash_tarea(descripcion, tarea)
            print(f"Tarea agregada al departamento {depto}.")
        elif opcion == "2":
            depto = input("Nombre del departamento: ")
            if depto in sistema.lista_departamentos:
                print(f"\nTareas en {depto}:")
                for i, t in enumerate(sistema.lista_departamentos[depto], 1):
                    print(f"{i}. {t}")
                try:
                    idx = int(input("Índice de tarea a eliminar: ")) - 1
                    tarea = sistema.eliminar_departamento(depto, idx)
                    if tarea:
                        print(f"Tarea eliminada: {tarea.descripcion}")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Entrada inválida.")
            else:
                print("Departamento no encontrado.")
        elif opcion == "3":
            print("\nTareas por departamento:")
            for depto, tareas in sistema.lista_departamentos.items():
                print(f"\n{depto}:")
                for i, t in enumerate(tareas, 1):
                    print(f"{i}. {t}")
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def gestionar_cola_prioridad(sistema):
    while True:
        print("\n--- Cola de Prioridad ---")
        print("1. Agregar tarea con prioridad")
        print("2. Completar tarea más prioritaria")
        print("3. Ver próxima tarea")
        print("4. Ver todas las tareas ordenadas")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            prioridad = int(input("Prioridad (1-10): "))
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            duracion = float(input("Duración estimada (horas): "))
            tarea = Tarea(descripcion, prioridad, fecha, duracion)
            sistema.agregar_prioridad(tarea)
            sistema.agregar_tarea_grafo(tarea)
            sistema.agregar_hash_tarea(descripcion, tarea)
            print("Tarea agregada a la cola de prioridad.")
        elif opcion == "2":
            tarea = sistema.completar_prioridad()
            if tarea:
                print(f"Tarea completada: {tarea.descripcion}")
            else:
                print("No hay tareas en la cola de prioridad.")
        elif opcion == "3":
            tarea = sistema.cola_prioridad.peek()
            if tarea:
                print(f"Próxima tarea: {tarea}")
            else:
                print("No hay tareas en la cola de prioridad.")
        elif opcion == "4":
            sistema.cola_prioridad.mostrar_tareas()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

def gestionar_empleados(sistema):
    while True:
        print("\n--- Árbol de Empleados ---")
        print("1. Agregar empleado")
        print("2. Buscar empleados por departamento")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_emp = input("ID del empleado: ")
            nombre = input("Nombre del empleado: ")
            depto = input("Departamento del empleado: ")
            sistema.agregar_empleado(id_emp, nombre, depto)
            print("Empleado agregado.")
        elif opcion == "2":
            depto = input("Departamento a buscar: ")
            empleados = sistema.buscar_empleados_departamento(depto)
            if empleados:
                print(f"\nEmpleados en {depto}:")
                for id_emp, nombre in empleados:
                    print(f"{id_emp}: {nombre}")
            else:
                print("No se encontraron empleados en ese departamento.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")

def gestionar_dependencias(sistema):
    while True:
        print("\n--- Grafo de Dependencias ---")
        print("1. Agregar tarea al grafo")
        print("2. Agregar dependencia entre tareas")
        print("3. Ver dependencias de una tarea")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            prioridad = int(input("Prioridad (1-10): "))
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            duracion = float(input("Duración estimada (horas): "))
            tarea = Tarea(descripcion, prioridad, fecha, duracion)
            sistema.agregar_tarea_grafo(tarea)
            sistema.agregar_hash_tarea(descripcion, tarea)
            print("Tarea agregada al grafo.")
        elif opcion == "2":
            tarea_principal = input("Descripción de la tarea principal: ")
            dependencia = input("Descripción de la tarea dependiente: ")
            # Buscar las tareas en el hashmap
            t1 = sistema.obtener_hash_tarea(tarea_principal)
            t2 = sistema.obtener_hash_tarea(dependencia)
            if t1 and t2:
                sistema.agregar_dependencia(t1, t2)
                print(f"Dependencia agregada: {tarea_principal} -> {dependencia}")
            else:
                print("Una o ambas tareas no fueron encontradas.")
        elif opcion == "3":
            tarea = input("Descripción de la tarea: ")
            t = sistema.obtener_hash_tarea(tarea)
            if t:
                dependencias = sistema.obtener_dependencias(t)
                if dependencias:
                    print(f"\nDependencias de {tarea}:")
                    for d in dependencias:
                        print(f"- {d.descripcion}")
                else:
                    print("La tarea no tiene dependencias.")
            else:
                print("Tarea no encontrada.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def gestionar_hashmap(sistema):
    while True:
        print("\n--- HashMap de Tareas ---")
        print("1. Agregar tarea al hashmap")
        print("2. Buscar tarea por descripción")
        print("3. Eliminar tarea del hashmap")
        print("4. Ver todas las tareas")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            prioridad = int(input("Prioridad (1-10): "))
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            duracion = float(input("Duración estimada (horas): "))
            tarea = Tarea(descripcion, prioridad, fecha, duracion)
            sistema.agregar_hash_tarea(descripcion, tarea)
            print("Tarea agregada al hashmap.")
        elif opcion == "2":
            descripcion = input("Descripción de la tarea a buscar: ")
            tarea = sistema.obtener_hash_tarea(descripcion)
            if tarea:
                print(f"Tarea encontrada: {tarea}")
            else:
                print("Tarea no encontrada.")
        elif opcion == "3":
            descripcion = input("Descripción de la tarea a eliminar: ")
            if sistema.hash_tareas.eliminar(descripcion):
                print("Tarea eliminada.")
            else:
                print("Tarea no encontrada.")
        elif opcion == "4":
            sistema.hash_tareas.mostrar_todas()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

def gestionar_estadisticas(sistema):
    while True:
        print("\n--- Estadísticas y Distribución ---")
        print("1. Ver estadísticas generales")
        print("2. Distribuir tareas entre empleados (Divide y Vencerás)")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            sistema.calcular_estadisticas()
        elif opcion == "2":
            depto = input("Departamento para distribución: ")
            empleados = sistema.buscar_empleados_departamento(depto)
            tareas = sistema.lista_departamentos.get(depto, [])
            
            if empleados and tareas:
                print(f"\nDistribuyendo {len(tareas)} tareas entre {len(empleados)} empleados...")
                distribucion = sistema.distribuir_tareas(tareas, empleados)
                
                print("\nDistribución resultante:")
                for emp, tareas_asignadas in distribucion.items():
                    emp_id, emp_nombre = emp
                    print(f"\nEmpleado: {emp_nombre} ({emp_id})")
                    for t in tareas_asignadas:
                        print(f"- {t.descripcion}")
            else:
                if not empleados:
                    print("No hay empleados en ese departamento.")
                if not tareas:
                    print("No hay tareas en ese departamento.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")

def gestionar_ordenamiento_busqueda(sistema):
    while True:
        print("\n--- Ordenamiento y Búsqueda ---")
        print("1. Ordenar tareas por prioridad")
        print("2. Ordenar tareas por fecha")
        print("3. Buscar tareas por descripción")
        print("4. Buscar tareas por fecha")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            todas_tareas = sistema.grafo_dependencias.todas_tareas()
            ordenadas = sistema.ordenar_tareas_prioridad(todas_tareas)
            print("\nTareas ordenadas por prioridad:")
            for i, t in enumerate(ordenadas, 1):
                print(f"{i}. {t}")
        elif opcion == "2":
            todas_tareas = sistema.grafo_dependencias.todas_tareas()
            ordenadas = sistema.ordenar_tareas_fecha(todas_tareas)
            print("\nTareas ordenadas por fecha:")
            for i, t in enumerate(ordenadas, 1):
                print(f"{i}. {t}")
        elif opcion == "3":
            descripcion = input("Texto a buscar en descripciones: ")
            resultados = sistema.buscar_tarea_descripcion(descripcion)
            if resultados:
                print("\nTareas encontradas:")
                for i, t in enumerate(resultados, 1):
                    print(f"{i}. {t}")
            else:
                print("No se encontraron tareas con esa descripción.")
        elif opcion == "4":
            fecha = input("Fecha a buscar (YYYY-MM-DD): ")
            resultados = sistema.buscar_tarea_fecha(fecha)
            if resultados:
                print("\nTareas encontradas:")
                for i, t in enumerate(resultados, 1):
                    print(f"{i}. {t}")
            else:
                print("No se encontraron tareas para esa fecha.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

def main():
    sistema = SistemaGestionTareas()
    
    # Datos de ejemplo
    sistema.agregar_empleado("E100", "Juan Pérez", "Ventas")
    sistema.agregar_empleado("E101", "María Gómez", "Ventas")
    sistema.agregar_empleado("E200", "Carlos Ruiz", "TI")
    sistema.agregar_empleado("E201", "Ana López", "TI")
    
    t1 = Tarea("Preparar informe trimestral", 8, "2023-12-15", 4)
    t1.departamento = "Ventas"
    sistema.agregar_departamento("Ventas", t1)
    sistema.agregar_tarea_grafo(t1)
    sistema.agregar_hash_tarea(t1.descripcion, t1)
    
    t2 = Tarea("Actualizar servidores", 9, "2023-11-30", 8)
    t2.departamento = "TI"
    sistema.agregar_departamento("TI", t2)
    sistema.agregar_tarea_grafo(t2)
    sistema.agregar_hash_tarea(t2.descripcion, t2)
    
    t3 = Tarea("Revisar contratos clientes", 7, "2023-12-10", 3)
    sistema.agregar_prioridad(t3)
    sistema.agregar_tarea_grafo(t3)
    sistema.agregar_hash_tarea(t3.descripcion, t3)
    
    sistema.agregar_dependencia(t1, t3)
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            gestionar_pila(sistema)
        elif opcion == "2":
            gestionar_cola(sistema)
        elif opcion == "3":
            gestionar_departamentos(sistema)
        elif opcion == "4":
            gestionar_cola_prioridad(sistema)
        elif opcion == "5":
            gestionar_empleados(sistema)
        elif opcion == "6":
            gestionar_dependencias(sistema)
        elif opcion == "7":
            gestionar_hashmap(sistema)
        elif opcion == "8":
            gestionar_estadisticas(sistema)
        elif opcion == "9":
            gestionar_ordenamiento_busqueda(sistema)
        elif opcion == "10":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()