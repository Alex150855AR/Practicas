# Definir las credenciales esperadas
usuario_esperado = "Alex15"
contrasena_esperada = "Romero1508"

# Máximo número de intentos permitidos
max_intentos = 4

print("Bienvenido a la Tienda de Ropa")

# Ciclo para permitir hasta 4 intentos de inicio de sesión
for intento in range(1, max_intentos + 1):
    usuario_ingresado = input("Por favor, ingrese su nombre de usuario: ")
    contrasena_ingresada = input("Por favor, ingrese su contraseña: ")

    if usuario_ingresado == usuario_esperado and contrasena_ingresada == contrasena_esperada:
        print("Inicio de sesión exitoso. Bienvenido.")
        print("Catálogo de categorías:")
        print("1. Ropa de Dama")
        print("2. Ropa de Caballero")
        print("3. Ropa de Niña")
        print("4. Ropa de Niño")
        break
    else:
        print(f"Nombre de usuario o contraseña incorrectos. Intento {intento} de {max_intentos}")

    # Si se alcanza el número máximo de intentos, se cierra el programa
    if intento == max_intentos:
        print("Máximo número de intentos excedido. Cerrando página.")
