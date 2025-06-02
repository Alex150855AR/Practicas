def crear_tabla_pitagoras(tamano):
    # Crear la tabla de Pitágoras usando una lista de listas
    tabla = [[i * j for j in range(1, tamano + 1)] for i in range(1, tamano + 1)]
    return tabla

def mostrar_tabla(tabla):
    tamano = len(tabla)
    
    # Imprimir la cabecera de la tabla
    print("   |", end="")
    for i in range(1, tamano + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * (4 * (tamano + 1) + 3))
    
    # Imprimir las filas de la tabla
    for i in range(tamano):
        print(f"{i + 1:2} |", end="")
        for j in range(tamano):
            print(f"{tabla[i][j]:4}", end="")
        print()

def multiplicar_con_tabla(tabla, factor1, factor2):
    # Obtener el resultado de la multiplicación usando la tabla
    # Restamos 1 porque los índices de la lista comienzan en 0
    return tabla[factor1 - 1][factor2 - 1]

# Tamaño de la tabla (10x10)
tamano = 10

# Crear la tabla de Pitágoras
tabla = crear_tabla_pitagoras(tamano)

# Mostrar la tabla de Pitágoras
print("Tabla de Pitágoras (10x10):")
mostrar_tabla(tabla)

# Solicitar los factores al usuario
factor1 = int(input("\nIngresa el primer factor (1-10): "))
factor2 = int(input("Ingresa el segundo factor (1-10): "))

# Verificar que los factores estén dentro del rango de la tabla
if 1 <= factor1 <= 10 and 1 <= factor2 <= 10:
    # Realizar la multiplicación usando la tabla
    resultado = multiplicar_con_tabla(tabla, factor1, factor2)
    # Mostrar el resultado
    print(f"\nEl resultado de multiplicar {factor1} x {factor2} es: {resultado}")
else:
    print("\nError: Los factores deben estar entre 1 y 10.")