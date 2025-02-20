import pygame
import random
import time

# Inicializar pygame
pygame.init()

# Definir colores
COLOR_FONDO = (0, 0, 0)
COLOR_SERPIENTE = (0, 100, 0)
COLOR_COMIDA = (255, 255, 255)

# Definir el tamaño de la pantalla
ANCHO = 800
ALTO = 600

# Definir el tamaño de los bloques
TAMANO_BLOQUE = 20

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake Game")

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Fuente para el texto
fuente = pygame.font.SysFont(None, 50)

def mostrar_puntuacion(puntuacion):
    texto = fuente.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, [10, 10])

def dibujar_serpiente(TAMANO_BLOQUE, lista_serpiente):
    for bloque in lista_serpiente:
        pygame.draw.rect(pantalla, COLOR_SERPIENTE, [bloque[0], bloque[1], TAMANO_BLOQUE, TAMANO_BLOQUE])

def generar_comida():
    comida_x = round(random.randrange(0, ANCHO - TAMANO_BLOQUE) / TAMANO_BLOQUE) * TAMANO_BLOQUE
    comida_y = round(random.randrange(0, ALTO - TAMANO_BLOQUE) / TAMANO_BLOQUE) * TAMANO_BLOQUE
    color_comida = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return comida_x, comida_y, color_comida

def juego():
    game_over = False
    game_close = False

    x = ANCHO / 2
    y = ALTO / 2

    x_cambio = 0
    y_cambio = 0

    lista_serpiente = []
    largo_serpiente = 1

    comida_x, comida_y, color_comida = generar_comida()

    pausa = False

    while not game_over:

        while game_close:
            pantalla.fill(COLOR_FONDO)
            mostrar_puntuacion(largo_serpiente - 1)
            texto = fuente.render("¡Perdiste! Presiona Q para salir o C para jugar de nuevo", True, (255, 255, 255))
            pantalla.blit(texto, [ANCHO / 6, ALTO / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_cambio == 0:
                    x_cambio = -TAMANO_BLOQUE
                    y_cambio = 0
                elif event.key == pygame.K_RIGHT and x_cambio == 0:
                    x_cambio = TAMANO_BLOQUE
                    y_cambio = 0
                elif event.key == pygame.K_UP and y_cambio == 0:
                    y_cambio = -TAMANO_BLOQUE
                    x_cambio = 0
                elif event.key == pygame.K_DOWN and y_cambio == 0:
                    y_cambio = TAMANO_BLOQUE
                    x_cambio = 0
                elif event.key == pygame.K_SPACE:
                    pausa = not pausa

        if pausa:
            continue

        # Si la serpiente sale por un borde, reaparece en el lado opuesto
        if x >= ANCHO:
            x = 0
        elif x < 0:
            x = ANCHO - TAMANO_BLOQUE
        if y >= ALTO:
            y = 0
        elif y < 0:
            y = ALTO - TAMANO_BLOQUE

        x += x_cambio
        y += y_cambio
        pantalla.fill(COLOR_FONDO)
        pygame.draw.rect(pantalla, color_comida, [comida_x, comida_y, TAMANO_BLOQUE, TAMANO_BLOQUE])

        cabeza_serpiente = [x, y]
        lista_serpiente.append(cabeza_serpiente)

        if len(lista_serpiente) > largo_serpiente:
            del lista_serpiente[0]

        for bloque in lista_serpiente[:-1]:
            if bloque == cabeza_serpiente:
                game_close = True

        dibujar_serpiente(TAMANO_BLOQUE, lista_serpiente)
        mostrar_puntuacion(largo_serpiente - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x, comida_y, color_comida = generar_comida()
            largo_serpiente += 1

        reloj.tick(15)

    pygame.quit()
    quit()

juego()
