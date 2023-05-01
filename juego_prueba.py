import pygame
import sys
import random


pygame.init()
pygame.font.init()


#constantes
ANCHO = 800
ALTO = 600
COLOR_ROJO = (255,0,0)
COLOR_NEGRO = (0,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VERDE = (0,255,0)
COLOR_BLANCO = (255,255,255)

#JUGADOR

class Jugador:
    def __init__(self):
        self.size = [50,50]
        self.pos = [ANCHO / 2 , ALTO - self.size[1] * 2]
        self.col = COLOR_ROJO

jugador = Jugador()

#ENEMIGOS
class Enemigo_1:
    def __init__(self):
        self.size = [50,50]
        self.pos = [random.randint(0, ANCHO - self.size[0]), 0]
        self.col = COLOR_VERDE

class Enemigo_2:
    def __init__(self):
        self.size = [70,50]
        self.pos = [random.randint(0, ANCHO - self.size[0]), 0]
        self.col = COLOR_BLANCO


class Enemigo_3:
    def __init__(self):
        self.size = [50,80]
        self.pos = [random.randint(0, ANCHO - self.size[0]), 0]
        self.col = COLOR_AZUL

clases_de_enemigos = [
    Enemigo_1,
    Enemigo_2,
    Enemigo_3
]

enemigos = [Enemigo_1()]


#Funciones

def dibujar_enemigo(enemigo):
    pygame.draw.rect(ventana, 
                     enemigo.col, 
                     (enemigo.pos[0],enemigo.pos[1],
                      enemigo.size[0],enemigo.size[1]))

def detectar_colision(jugador, enemigo):
    jx = jugador.pos[0]
    jy = jugador.pos[1]
    ex = enemigo.pos[0]
    ey = enemigo.pos[1]

    if (ex >= jx and ex < (jx + jugador.size[0])) or (jx >= ex and jx < (ex + enemigo.size[0])):
        if (ey >= jy and ey < (jy + jugador.size[0])) or (jy >= ey and jy < (ey + enemigo.size[0])):
            return True
    return False

# Fuente y tamaño del texto de puntuación
font = pygame.font.Font(None, 36)

#ventana
ventana = pygame.display.set_mode((ANCHO,ALTO))

game_over = False
clock = pygame.time.Clock()

score = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = jugador.pos[0]
            if event.key == pygame.K_LEFT:
                x -= jugador.size[0]
            if event.key == pygame.K_RIGHT:
                x += jugador.size[0]

            jugador.pos[0] = x

    ventana.fill(COLOR_NEGRO)
    tiempo_transcurrido = pygame.time.get_ticks() // 1000

    # Dibujar la puntuación en la esquina superior derecha
    text = font.render(f"Puntuación: {score}", True, COLOR_BLANCO)
    text_rect = text.get_rect()
    text_rect.topright = (ANCHO - 10, 10)
    ventana.blit(text, text_rect)

    #Agregar mas enemigos
    if len(enemigos) < 5:
        if tiempo_transcurrido >= len(enemigos):
            nuevo_enemigo = clases_de_enemigos[0]()
            enemigos.append(nuevo_enemigo)
            

    i = -1
    for enemigo in enemigos :

      i += 1

      #Para que el enemigo descienda

      if enemigo.pos[1] >= 0 and enemigo.pos[1] < ALTO:
          enemigo.pos[1] += 15
      else:
          score += 1
          enemigos.pop(i)
          def clase():
              if tiempo_transcurrido < 10:
                  return 0
              elif tiempo_transcurrido < 20:
                  return random.randint(0 , 1)
              else:
                  return random.randint(0 , 2)
          nuevo_enemigo = clases_de_enemigos[clase()]()
          enemigos.append(nuevo_enemigo)

      #Colisiones
      if detectar_colision(jugador, enemigo):
        game_over = True

      #dibujar enemigo

      dibujar_enemigo(enemigo)



    #dibujar jugador
    pygame.draw.rect(ventana, 
                     jugador.col, 
                     (jugador.pos[0],jugador.pos[1],
                      jugador.size[0],jugador.size[0]))
    
    clock.tick(30)
    pygame.display.update()

print("Tu puntuacion fue de", score)
