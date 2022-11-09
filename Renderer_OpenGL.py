from pickle import TRUE
import pygame
import pygame_menu as pm
from pygame.locals import *

from shaders import *

from gl import Renderer, Model

from math import cos, sin, radians

width = 1080
height = 720
deltaTime = 0.0
ctrlR = 2
ctrlL = 2

# ------------------------INITS--------------------------------------
pygame.init()
pygame.mixer.init()
# --------------------------------------------------------------

screen = pygame.display.set_mode(
    (width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

# --------------------------------------------------------------
# Loading assets
icon = pygame.image.load("Logo_Cristian_Color.png")
bg = pygame.image.load("bg.png").convert()
pygame.mixer.music.load("kokiri.mp3")

mod = Model("models/Teddy.obj", "models/Teddy.bmp")
goat = Model("models/goat.obj", "models/goat.bmp")
ship = Model("models/ship.obj", "models/ship.bmp")
cat = Model("models/cat.obj", "models/cat.bmp")
tractor = Model("models/tractor.obj", "models/tractor.bmp")
# --------------------------------------------------------------

# --------------------------------------------------------------
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

rend = Renderer(screen, 0.145, 0.588, 0.745)

rend.setShaders(vertex_shader, fragment_shader)

rend.target.z = -5

# --------------------------------------------------------------
# Positioning MODEL 1
goat.position.z -= 5
goat.position.y -= 0.4
goat.scale.x = 0.3
goat.scale.y = 0.3
goat.scale.z = 0.3
goat.rotation.y = 20

# Positioning MODEL 2
mod.position.z -= 5
mod.position.y -= 0.4
mod.scale.x = 2
mod.scale.y = 2
mod.scale.z = 2
mod.rotation.y = 90

# Positioning MODEL 3
ship.position.z -= 5
ship.position.y -= 0.5
ship.scale.x = 1
ship.scale.y = 1
ship.scale.z = 1
ship.rotation.y = 30

# Positioning MODEL 4
cat.position.z -= 5
cat.position.y -= 0.8
cat.scale.x = 1.8
cat.scale.y = 1.8
cat.scale.z = 1.8
cat.rotation.y = 5

# Positioning MODEL 5
# --------------------------------------------------------------
tractor.scale.x = 0.4
tractor.scale.y = 0.4
tractor.scale.z = 0.4
tractor.position.z -= 5
tractor.rotation.y = 20

rend.scene.append(cat)

# --------------------------------------------------------------
rend.pointLight.x -= 10
# --------------------------------------------------------------

pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
pygame.display.set_caption("Lab4 Shaders")
pygame.display.set_icon(icon)
isRunning = True

while isRunning:
    clock.tick(60)
    # draw background
    screen.blit(bg, (0, 0))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_z:
                rend.filledMode()
            elif event.key == pygame.K_x:
                rend.wireframeMode()

        # --------------------MOUSE WHEEL SCROLL TO ZOOM IN AND OUT
        elif event.type == pygame.MOUSEWHEEL:
            if rend.camDistance >= 2 and rend.camDistance <= 10:
                rend.camDistance -= (event.y * 10) * deltaTime
            elif rend.camDistance < 2:
                rend.camDistance = 2
            elif rend.camDistance > 10:
                rend.camDistance = 10

        # ---------------------LEFT CLICK TO CHANGE SHADER--------------------------
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:

                pygame.mixer.Channel(1).play(
                    pygame.mixer.Sound("popsound.mp3"))
                if ctrlL == 1:
                    rend.scene.pop()
                    rend.scene.append(cat)
                elif ctrlL == 2:
                    rend.scene.pop()
                    rend.scene.append(mod)
                elif ctrlL == 3:
                    rend.scene.pop()
                    rend.scene.append(ship)
                elif ctrlL == 4:
                    rend.scene.pop()
                    rend.scene.append(goat)
                elif ctrlL == 5:
                    rend.scene.pop()
                    rend.scene.append(tractor)
                ctrlL += 1
                if ctrlL == 6:
                    ctrlL = 1

            if mouse[2]:

                pygame.mixer.Channel(1).play(
                    pygame.mixer.Sound("popsound.mp3"))
                if ctrlR == 1:
                    rend.setShaders(vertex_shader, fragment_shader)
                elif ctrlR == 2:
                    rend.setShaders(vertex_shader, fragment_shader_toon)
                elif ctrlR == 3:
                    rend.setShaders(vertex_shader, fragment_shader_termal)
                elif ctrlR == 4:
                    rend.setShaders(vertex_shader_expandloop,
                                    fragment_shader_bluered)
                elif ctrlR == 5:
                    rend.setShaders(vertex_shader, fragment_shader_toonpop)
                elif ctrlR == 6:
                    rend.setShaders(vertex_shader, fragment_shader_rainbow)
                elif ctrlR == 7:
                    rend.setShaders(vertex_shader, fragment_shader_tooncrazy)
                ctrlR += 1
                if ctrlR == 8:
                    ctrlR = 1

    # -------------MOVEMENT OF CAMERA-------------------------------
    cursorposition = pygame.mouse.get_rel()

    if keys[K_a]:
        rend.angle -= 30 * deltaTime
    elif keys[K_d]:
        rend.angle += 30 * deltaTime

    elif rend.camPosition.y >= -2 and rend.camPosition.y <= 2:
        rend.camPosition.y += cursorposition[1] * deltaTime
    elif rend.camPosition.y < -2:
        rend.camPosition.y = -2
    elif rend.camPosition.y > 2:
        rend.camPosition.y = 2

    rend.angle -= cursorposition[0] * 10 * deltaTime
    # ----------------------------------------------------------------

    rend.target.y = rend.camPosition.y

    rend.camPosition.x = rend.target.x + \
        sin(radians(rend.angle)) * rend.camDistance
    rend.camPosition.z = rend.target.z + \
        cos(radians(rend.angle)) * rend.camDistance

    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime
    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime

    # -------------------CHANGE SHADER WITH NUMBER KEYBOARD-------------------
    if keys[K_1]:
        rend.setShaders(vertex_shader, fragment_shader)
    elif keys[K_2]:
        rend.setShaders(vertex_shader, fragment_shader_toon)
    elif keys[K_3]:
        rend.setShaders(vertex_shader, fragment_shader_termal)
    elif keys[K_4]:
        rend.setShaders(vertex_shader_expand, fragment_shader_rainbow)
    elif keys[K_5]:
        rend.setShaders(vertex_shader, fragment_shader_toonpop)
    elif keys[K_6]:
        rend.setShaders(vertex_shader, fragment_shader_tooncrazy)

    # --------------------------MUSIC-----------------------------------------------
    if keys[K_p]:
        pygame.mixer.music.play()

    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
