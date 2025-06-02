# Función para obtener y formatear el nombre del usuario
def obtener_nombre():
    """
    Solicita el nombre del usuario y lo retorna formateado
    con la primera letra en mayúscula y el resto en minúscula.
    """
    nombre = input("Por favor, ingrese su nombre: ").strip()
    return nombre.capitalize()

# 1. Entrada de usuario: solicitar números
def ingresar_numeros():
    """
    Solicita al usuario ingresar números separados por comas.
    Retorna una lista de números flotantes.
    """
    while True:
        entrada = input("Ingrese un conjunto de números separados por comas: ")
        numeros_str = entrada.split(',')
        
        try:
            numeros = [float(num.strip()) for num in numeros_str]
            return numeros
        except ValueError:
            print("Error: Asegúrese de ingresar solo números separados por comas. Intente nuevamente.")

# 2. Procesamiento de datos: calcular estadísticas
def calcular_estadisticas(numeros):
    """
    Calcula el mayor, menor y promedio de una lista de números.
    Retorna un diccionario con estos valores.
    """
    if not numeros:
        return None
    
    mayor = max(numeros)
    menor = min(numeros)
    promedio = sum(numeros) / len(numeros)
    
    return {
        'mayor': mayor,
        'menor': menor,
        'promedio': promedio
    }

# 3. Estructuras de selección: evaluar promedio
def evaluar_promedio(promedio):
    """
    Evalúa el promedio y retorna un mensaje según rangos:
    - Bajo: menos de 30
    - Medio: entre 30 y 70
    - Alto: más de 70
    """
    if promedio < 30:
        return "bajo"
    elif 30 <= promedio <= 70:
        return "medio"
    else:
        return "alto"

# Función principal
def main():
    print("=== Programa de Análisis de Números ===")
    
    # Obtener nombre del usuario primero
    nombre = obtener_nombre()
    print(f"\n¡Hola, {nombre}! Vamos a analizar algunos números.")
    
    # Obtener números del usuario
    numeros = ingresar_numeros()
    
    # Calcular estadísticas
    estadisticas = calcular_estadisticas(numeros)
    
    if estadisticas is None:
        print("No se ingresaron números válidos.")
        return
    
    # Mostrar resultados
    print("\nResultados:")
    print(f"El número mayor es: {estadisticas['mayor']}")
    print(f"El número menor es: {estadisticas['menor']}")
    print(f"El promedio es: {estadisticas['promedio']:.2f}")
    
    # Evaluar promedio
    categoria = evaluar_promedio(estadisticas['promedio'])
    print(f"El promedio es considerado {categoria}.")
    
    # Mensaje de despedida personalizado
    print(f"\nGracias por usar el programa, {nombre}. ¡Hasta pronto!")

# Ejecutar el programa
if __name__ == "__main__":
    main()