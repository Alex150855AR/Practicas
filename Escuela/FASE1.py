class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Agrega un elemento a la pila"""
        self.items.append(item)
    
    def pop(self):
        """Elimina y devuelve el elemento superior de la pila"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Devuelve el elemento superior sin eliminarlo"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Verifica si la pila está vacía"""
        return len(self.items) == 0
    
    def size(self):
        """Devuelve el tamaño de la pila"""
        return len(self.items)
    
    def mostrar_tareas(self):
        """Muestra todas las tareas en la pila"""
        print("\n--- Tareas Urgentes (Pila) ---")
        if self.is_empty():
            print("No hay tareas urgentes.")
        else:
            for i, tarea in enumerate(reversed(self.items), 1):
                print(f"{i}. {tarea}")


class Cola:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Agrega un elemento a la cola"""
        self.items.append(item)
    
    def dequeue(self):
        """Elimina y devuelve el primer elemento de la cola"""
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        """Devuelve el primer elemento sin eliminarlo"""
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        """Verifica si la cola está vacía"""
        return len(self.items) == 0
    
    def size(self):
        """Devuelve el tamaño de la cola"""
        return len(self.items)
    
    def mostrar_tareas(self):
        """Muestra todas las tareas en la cola"""
        print("\n--- Tareas Programadas (Cola) ---")
        if self.is_empty():
            print("No hay tareas programadas.")
        else:
            for i, tarea in enumerate(self.items, 1):
                print(f"{i}. {tarea}")


class ListaTareas:
    def __init__(self):
        self.tareas = {}
    
    def insert(self, departamento, tarea):
        """Agrega una tarea a la lista del departamento"""
        if departamento not in self.tareas:
            self.tareas[departamento] = []
        self.tareas[departamento].append(tarea)
    
    def delete(self, departamento, indice):
        """Elimina una tarea de la lista del departamento"""
        if departamento in self.tareas and 0 <= indice < len(self.tareas[departamento]):
            return self.tareas[departamento].pop(indice)
        return None
    
    def find(self, departamento):
        """Devuelve las tareas de un departamento"""
        return self.tareas.get(departamento, [])
    
    def mostrar_tareas(self):
        """Muestra todas las tareas organizadas por departamento"""
        print("\n--- Tareas por Departamento (Lista) ---")
        if not self.tareas:
            print("No hay tareas por departamento.")
        else:
            for departamento, tareas in self.tareas.items():
                print(f"\nDepartamento: {departamento}")
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")


def mostrar_menu_principal():
    print("\n--- Sistema de Gestión de Tareas ---")
    print("1. Gestionar tareas urgentes (Pila)")
    print("2. Gestionar tareas programadas (Cola)")
    print("3. Gestionar tareas por departamento (Lista)")
    print("4. Ver todas las tareas pendientes")
    print("5. Salir")


def gestionar_pila(pila):
    while True:
        print("\n--- Gestión de Tareas Urgentes (Pila) ---")
        print("1. Agregar tarea urgente")
        print("2. Eliminar tarea urgente (realizada)")
        print("3. Ver tarea más urgente")
        print("4. Ver todas las tareas urgentes")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tarea = input("Ingrese la tarea urgente: ")
            pila.push(tarea)
            print(f"Tarea '{tarea}' agregada a urgentes.")
        elif opcion == "2":
            tarea = pila.pop()
            if tarea:
                print(f"Tarea '{tarea}' marcada como realizada.")
            else:
                print("No hay tareas urgentes pendientes.")
        elif opcion == "3":
            tarea = pila.peek()
            if tarea:
                print(f"Tarea más urgente: {tarea}")
            else:
                print("No hay tareas urgentes pendientes.")
        elif opcion == "4":
            pila.mostrar_tareas()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def gestionar_cola(cola):
    while True:
        print("\n--- Gestión de Tareas Programadas (Cola) ---")
        print("1. Agregar tarea programada")
        print("2. Eliminar tarea programada (realizada)")
        print("3. Ver próxima tarea programada")
        print("4. Ver todas las tareas programadas")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tarea = input("Ingrese la tarea programada: ")
            cola.enqueue(tarea)
            print(f"Tarea '{tarea}' agregada a programadas.")
        elif opcion == "2":
            tarea = cola.dequeue()
            if tarea:
                print(f"Tarea '{tarea}' marcada como realizada.")
            else:
                print("No hay tareas programadas pendientes.")
        elif opcion == "3":
            tarea = cola.front()
            if tarea:
                print(f"Próxima tarea programada: {tarea}")
            else:
                print("No hay tareas programadas pendientes.")
        elif opcion == "4":
            cola.mostrar_tareas()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def gestionar_lista(lista):
    while True:
        print("\n--- Gestión de Tareas por Departamento (Lista) ---")
        print("1. Agregar tarea a departamento")
        print("2. Eliminar tarea de departamento")
        print("3. Ver tareas de un departamento")
        print("4. Ver todas las tareas por departamento")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            departamento = input("Ingrese el nombre del departamento: ")
            tarea = input("Ingrese la tarea: ")
            lista.insert(departamento, tarea)
            print(f"Tarea '{tarea}' agregada al departamento '{departamento}'.")
        elif opcion == "2":
            departamento = input("Ingrese el nombre del departamento: ")
            tareas = lista.find(departamento)
            if tareas:
                print(f"\nTareas del departamento '{departamento}':")
                for i, t in enumerate(tareas, 1):
                    print(f"{i}. {t}")
                try:
                    indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
                    tarea = lista.delete(departamento, indice)
                    if tarea:
                        print(f"Tarea '{tarea}' eliminada.")
                    else:
                        print("Índice no válido.")
                except ValueError:
                    print("Entrada no válida. Debe ingresar un número.")
            else:
                print(f"No hay tareas en el departamento '{departamento}'.")
        elif opcion == "3":
            departamento = input("Ingrese el nombre del departamento: ")
            tareas = lista.find(departamento)
            if tareas:
                print(f"\nTareas del departamento '{departamento}':")
                for i, t in enumerate(tareas, 1):
                    print(f"{i}. {t}")
            else:
                print(f"No hay tareas en el departamento '{departamento}'.")
        elif opcion == "4":
            lista.mostrar_tareas()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def ver_todas_tareas(pila, cola, lista):
    print("\n--- Todas las Tareas Pendientes ---")
    
    # Mostrar tareas urgentes (pila)
    print("\nTAREAS URGENTES:")
    if pila.is_empty():
        print("No hay tareas urgentes.")
    else:
        for i, tarea in enumerate(reversed(pila.items), 1):
            print(f"{i}. {tarea}")
    
    # Mostrar tareas programadas (cola)
    print("\nTAREAS PROGRAMADAS:")
    if cola.is_empty():
        print("No hay tareas programadas.")
    else:
        for i, tarea in enumerate(cola.items, 1):
            print(f"{i}. {tarea}")
    
    # Mostrar tareas por departamento (lista)
    print("\nTAREAS POR DEPARTAMENTO:")
    if not lista.tareas:
        print("No hay tareas por departamento.")
    else:
        for departamento, tareas in lista.tareas.items():
            print(f"\nDepartamento: {departamento}")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")


def main():
    pila = Pila()
    cola = Cola()
    lista = ListaTareas()
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            gestionar_pila(pila)
        elif opcion == "2":
            gestionar_cola(cola)
        elif opcion == "3":
            gestionar_lista(lista)
        elif opcion == "4":
            ver_todas_tareas(pila, cola, lista)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()