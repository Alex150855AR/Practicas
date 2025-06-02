import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Definir colores
blanco = (255, 255, 255)
amarillo = (255, 255, 102)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Definir dimensiones de la ventana
ancho = 600
alto = 400

# Crear la ventana del juego
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Juego de la Serpiente')

# Configurar el reloj
reloj = pygame.time.Clock()

# Tamaño de la serpiente
tamaño_celda = 10
velocidad = 15

# Fuente para el texto
fuente_puntuacion = pygame.font.SysFont("bahnschrift", 25)

# Función para mostrar la puntuación
def puntuacion(score):
    valor = fuente_puntuacion.render("Puntuación: " + str(score), True, negro)
    pantalla.blit(valor, [0, 0])

# Función para dibujar la serpiente
def nuestra_serpiente(tamaño_celda, lista_segmentos):
    for x in lista_segmentos:
        pygame.draw.rect(pantalla, verde, [x[0], x[1], tamaño_celda, tamaño_celda])

# Función principal del juego
def juego():
    juego_terminado = False
    juego_perdido = False

    # Coordenadas iniciales de la serpiente
    x1 = ancho / 2
    y1 = alto / 2

    # Velocidades iniciales
    x1_cambio = 0
    y1_cambio = 0

    # Longitud inicial de la serpiente
    serpiente_lista = []
    longitud_serpiente = 1

    # Posición de la comida
    comida_x = round(random.randrange(0, ancho - tamaño_celda) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tamaño_celda) / 10.0) * 10.0

    while not juego_terminado:

        while juego_perdido:
            pantalla.fill(azul)
            mensaje = fuente_puntuacion.render("Perdiste! Presiona C para jugar otra vez o Q para salir", True, rojo)
            pantalla.blit(mensaje, [ancho / 6, alto / 3])
            puntuacion(longitud_serpiente - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        juego_terminado = True
                        juego_perdido = False
                    if evento.key == pygame.K_c:
                        juego()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_celda
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_celda
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_celda
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_celda
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            juego_perdido = True
        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, amarillo, [comida_x, comida_y, tamaño_celda, tamaño_celda])
        serpiente_cabeza = []
        serpiente_cabeza.append(x1)
        serpiente_cabeza.append(y1)
        serpiente_lista.append(serpiente_cabeza)

        if len(serpiente_lista) > longitud_serpiente:
            del serpiente_lista[0]

        for x in serpiente_lista[:-1]:
            if x == serpiente_cabeza:
                juego_perdido = True

        nuestra_serpiente(tamaño_celda, serpiente_lista)
        puntuacion(longitud_serpiente - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_celda) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto - tamaño_celda) / 10.0) * 10.0
            longitud_serpiente += 1

        reloj.tick(velocidad)

    pygame.quit()
    quit()

# Llamar a la función de juego
juego()
