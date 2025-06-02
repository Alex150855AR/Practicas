import cmath  # Se importa para trabajar con raíces cuadradas de números negativos

# Función para resolver la ecuación de segundo grado
def resolver_ecuacion_segundo_grado(a, b, c):
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c
    
    # Calculamos las dos soluciones (usando cmath para manejar números negativos en la raíz)
    solucion_1 = (-b + cmath.sqrt(discriminante)) / (2*a)
    solucion_2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    
    return solucion_1, solucion_2

# Entrada de los coeficientes
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

# Asegurarse de que 'a' no sea 0
if a == 0:
    print("El valor de 'a' no puede ser 0 en una ecuación de segundo grado.")
else:
    # Resolver la ecuación
    soluciones = resolver_ecuacion_segundo_grado(a, b, c)
    
    # Mostrar las soluciones
    print(f"Las soluciones son: {soluciones[0]} y {soluciones[1]}")
