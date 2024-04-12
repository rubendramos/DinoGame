import pygame
import random
import math

from Image import Image as Image
from Dino import Dino as Dino
from EstateEnum import EstateEnum as EstateEnum
from Picture import Picture as Picture
from Pterodaptilo import Pterodaptilo as Pterodaptilo
from Cloud import Cloud as Cloud

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
PTERODAPTILO_LAUNCH =9000
OBSTACLE_LAUNCH =1000
# create a bunch of events
pterodaptilo_lauch_event = pygame.USEREVENT + 1
obstacle_lauch_event = pygame.USEREVENT + 2

colision = False
colisionCaputs = False
colisionPterodaptilo = False

# Titulo e Icono
pygame.display.set_caption("Dino Game")
icono = pygame.image.load("images/dinorun1.png")
pygame.display.set_icon(icono)
fondo = [255, 255, 255]
gravedad = 1
speed = -7

# Imamegenes Dino
img_dino_left = Image("dino_left", pygame.image.load("images/dinorun1.png"), 43, 40)
img_dino_rigth = Image("dino_rigth", pygame.image.load("images/dinorun2.png"), 43, 40)
img_dino_jump = Image("dino_jump", pygame.image.load("images/dinojump.png"), 43, 40)
img_dino_dead = Image("dino_dead", pygame.image.load("images/dinodead.png"), 43, 40)
img_dino_bend_left = Image("dino_bend_left", pygame.image.load("images/dinobendleft.png"), 26, 55)
img_dino_bend_right = Image("dino_bend_right", pygame.image.load("images/dinobendright.png"), 26, 55)

# Imganes suelo
img_ground1 = Image("ground1", pygame.image.load("images/ground1.png"), 12, 100)
img_ground2 = Image("ground2", pygame.image.load("images/ground2.png"), 12, 100)
img_ground3 = Image("ground3", pygame.image.load("images/ground3.png"), 12, 100)
img_ground4 = Image("ground4", pygame.image.load("images/ground4.png"), 20, 120)
captus3 = Image("3captus", pygame.image.load("images/3captus.png"), 33, 50)
captus1 = Image("captus", pygame.image.load("images/1captus.png"), 33, 15)
bigCaptus = Image("bigCaptus", pygame.image.load("images/big_captus.png"), 48, 23)
multipeCaptus = Image("multipeCaptus", pygame.image.load("images/multiple_captus.png"), 48, 73)
terodaptiloUp = Image("terodaptilo", pygame.image.load("images/terodaptiloUp.png"), 30, 44)
terodaptiloDown = Image("terodaptilo", pygame.image.load("images/terodaptiloDown.png"), 30, 44)
# set timer for the dino events
pygame.time.set_timer(pterodaptilo_lauch_event, PTERODAPTILO_LAUNCH)
pygame.time.set_timer(obstacle_lauch_event, OBSTACLE_LAUNCH)

#Game over
game_over = Image("gameover", pygame.image.load("images/gameover.png"), 65, 191)
gameOverImage = Picture(game_over, 300, 200, pantalla, False)

#cloud
cloud = Image("cloud", pygame.image.load("images/cloud.png"), 17, 58)

dino_x = 124
dino_y = 300
dinoImageLeft = Picture(img_dino_left, dino_x, dino_y, pantalla, False)
dinoImageRight = Picture(img_dino_rigth, dino_x, dino_y, pantalla, False)
dinoImageJump = Picture(img_dino_jump, dino_x, dino_y, pantalla, False)
dinoImageBendLeft = Picture(img_dino_bend_left, dino_x, dino_y, pantalla, False)
dinoImageBendRight = Picture(img_dino_bend_right, dino_x, dino_y, pantalla, False)
dinoImageDead = Picture(img_dino_dead, dino_x, dino_y, pantalla, False)
terodaptiloImageUp = Picture(terodaptiloUp, 0, 0, pantalla, True)
terodaptiloImageDown = Picture(terodaptiloDown, 0, 0, pantalla, True)

#Instancia dino
dino = Dino(EstateEnum.RUN, dinoImageJump, dinoImageLeft, dinoImageRight, dinoImageBendLeft, dinoImageBendRight, dinoImageDead)
dino.image = dinoImageLeft
dino.set_pos_x(dino_x)
dino.set_pos_y(dino_y)

#Inicializa cloud
cloudPicture = Picture(cloud, 0, 0, pantalla, False)
cloudHi = Cloud(-.1, cloudPicture, 800, 250)
cloudMid = Cloud(-.2, cloudPicture, 800, 225)
cloudLow = Cloud(-.3, cloudPicture, 800, 200)

# puntaje
hi_score = 0
score = 0
score_font = pygame.font.Font('TerminalVector.ttf', 15)
score_x = 550
score_y = 10

##Inicializamos dinon game
def inicializa_dinogame():
    pos_x_inicial = 0
    ground1 = Picture(img_ground1, 0, 0, pantalla, False)
    ground2 = Picture(img_ground2, 0, 0, pantalla, False)
    ground3 = Picture(img_ground3, 0, 0, pantalla, False)
    ground4 = Picture(img_ground1, 0, 0, pantalla, False)
    ground5 = Picture(img_ground2, 0, 0, pantalla, False)
    ground6 = Picture(img_ground3, 0, 0, pantalla, False)
    ground7 = Picture(img_ground1, 0, 0, pantalla, False)
    ground8 = Picture(img_ground2, 0, 0, pantalla, False)
    ground9 = Picture(img_ground3, 0, 0, pantalla, False)
    ground10 = Picture(img_ground1, 0, 0, pantalla, False)
    ground11 = Picture(img_ground2, 0, 0, pantalla, False)

    initialPterodaptloList = []

    initialGroundList = [ground1, ground2, ground3, ground4, ground5, ground6, ground7, ground8, ground9,
                         ground10, ground11]
    for ground in initialGroundList:
        ground.set_pos_x(pos_x_inicial)
        pos_x_inicial = pos_x_inicial + ground.image.width

    return initialGroundList, initialPterodaptloList


# funcion mostrar puntaje
def mostrar_puntuacion(score, hi_score, x, y):
    format_score = "{:05d}".format(score)
    format_hi_score = "{:05d}".format(hi_score)
    texto_score = score_font.render(f"HI: {format_hi_score} - SCORE: {format_score}", True, (120, 120, 120))
    pantalla.blit(texto_score, (x, y))


def pinta_obstaculo(pos_y):
    initialGroundList.append(
        Picture(random.choice(obstacles), initialGroundList[-1].pos_x + initialGroundList[-1].image.width, pos_y,
                pantalla, True))

def engade_pterodaptilo():
        initialPterodaptloList.append(Pterodaptilo(-2, Picture(terodaptiloUp, 0, 0, pantalla, True), Picture(terodaptiloDown, 0, 0, pantalla, True), 800,
                 random.choice(pterodaptiloHiList)))

def pinta_suelo(dino):

    colision = False
    for ground in initialGroundList:
        pos_y = dino_y + dinoImageLeft.image.height - ground.image.height
        if ground.pos_x <= -100:
            initialGroundList.remove(ground)
            initialGroundList.append(Picture(random.choice(groundList), initialGroundList[-1].pos_x + initialGroundList[-1].image.width, pos_y, pantalla, False))
            initialGroundList.append(Picture(random.choice(groundList), initialGroundList[-1].pos_x + initialGroundList[-1].image.width, pos_y, pantalla, False))
        ground.set_position_and_paint(ground.get_pos_x() + dino.get_speed(), pos_y)
        if(ground.es_obstaculo() and hai_colisionRectangulos(ground, dino)):
            colision = True
    return colision

def pinta_pterodaptilos(dino):
    colision = False
    for pterodaptilo in initialPterodaptloList:
        if pterodaptilo.pos_x <= -100:
            initialPterodaptloList.remove(pterodaptilo)
        pterodaptilo.set_velocidad(dino.get_speed())
        pterodaptilo.pinta_pterodaptilo()
        if (pterodaptilo.es_obstaculo() and hai_colisionRectangulos(pterodaptilo, dino)):
            colision = True
    return colision

def pinta_nuves() -> object:
    cloudLow.pinta_cloud()
    cloudMid.pinta_cloud()

# funcion pinta paisaje
def pinta_paisaje(dino):
    dino.pinta_dino(gravedad)
    colisionCaputs = pinta_suelo(dino)
    colisionPterodaptilo = pinta_pterodaptilos(dino)
    pinta_nuves()
    return colisionCaputs or colisionPterodaptilo


# Dectecta colisión
def hai_colision_cicumferencia(x1,y1,x2,y2):
    distancia = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
    print("Distancia:", distancia)
    if distancia < 35:
        print("Colision!!!!!")
        return True
    else:
        return False


def hai_colisionRectangulos(picture1, dino1):
    tolerance = 20
    p1_x = picture1.pos_x
    p1_y = picture1.pos_y
    p1_h = picture1.get_image().height
    p1_w = picture1.get_image().width

    d_x = dino1.pos_x
    d_y = dino1.pos_y
    d_w = dino1.get_image().image.width
    d_h = dino1.get_image().image.height



    if (p1_x >= d_x + d_w - tolerance) :
        return False
    elif (p1_x + p1_w - tolerance <= d_x):
        return False
    elif (p1_y >= d_y + d_h - tolerance):
        return False
    elif (p1_y + p1_h - tolerance <= d_y):
        return False
    else:

  #      print("p1x", p1_x, ">=", d_x + d_w - tolerance)
  #        print("p1y", p1_y, ">=", d_y + d_h - tolerance)
  #      print("p1h", p1_h)
  #      print("p1w", p1_w)

  #     print("d1x", d_x, ">=", p1_x + p1_w - tolerance,)
  #      print("d1y", d_y, ">=", p1_y + p1_h - tolerance )
  #      print("d1h", d_h)
  #     print("d1w", d_w)

        print("Colision!!!!!")
        return True

en_ejecucion = True

initialGroundList, initialPterodaptloList = inicializa_dinogame()
groundList = [img_ground1, img_ground2, img_ground3]
obstacles = [captus3, captus1, bigCaptus, multipeCaptus]
clouds = [cloudLow,cloudHi,cloudMid]
pterodaptiloHiList = [295,290,280]

#animals = [pterodaptiloHi, pterodaptiloMid, pterodaptiloLow]


start_ticks = pygame.time.get_ticks()
while en_ejecucion:
    clock.tick(100)
    if colision == False:
        score = int((pygame.time.get_ticks() - start_ticks) / 100)
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            en_ejecucion = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                dino.set_estate(EstateEnum.JUMP)
                print("tecla espacio presionada")
            if evento.key == pygame.K_DOWN:
                print("tecla down presionada")
                if dino.get_estate() == EstateEnum.RUN or dino.get_estate() == EstateEnum.JUMP:
                    dino.reset_jump_speed()
                    dino.set_estate(EstateEnum.BEND)
                print("Estado: ", dino.get_estate())
            if evento.key == pygame.K_RETURN:
                print("tecla return  down")
                dino.reset()
                start_ticks = pygame.time.get_ticks()
                speed = -5
                score = 0
                initialGroundList, initialPterodaptloList = inicializa_dinogame()
                colision = False
                colisionCaputs = False
                colisionPterodaptilo = False

                pygame.display.update()
        if evento.type == pygame.KEYUP:
             if evento.key == pygame.K_DOWN:
                if dino.get_estate() == EstateEnum.BEND:
                    dino.pos_y = dino_y
                    dino.reset_jump_speed()
                    dino.set_estate(EstateEnum.RUN)
                print("tecla down up")
        if evento.type == pterodaptilo_lauch_event:
            engade_pterodaptilo()
            pygame.time.set_timer(pterodaptilo_lauch_event, random.randint(10000, 15000))
        if evento.type == obstacle_lauch_event:
            pos_y = dino.dino_y + dinoImageLeft.image.height - initialGroundList[1].image.height
            pinta_obstaculo(pos_y)

    pantalla.fill(fondo)
    mostrar_puntuacion(score, hi_score, score_x, score_y)
    if colision == False:
        colision = pinta_paisaje(dino)
        pygame.display.update()
        dino.set_speed(dino.get_speed() - 0.001)
    else:
        dino.set_speed(0)
        dino.set_estate(EstateEnum.DEAD)
        pinta_paisaje(dino)
        gameOverImage.paint()
        if (score > hi_score):
            hi_score = score
        dino.pinta_dino(gravedad)
        pygame.display.update()
