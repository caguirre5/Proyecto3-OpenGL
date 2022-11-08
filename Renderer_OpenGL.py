from pickle import TRUE
import pygame
from pygame.locals import *

from shaders import *

from gl import Renderer, Model

from math import cos, sin, radians

width = 1080
height = 720

deltaTime = 0.0

ctrl = 2

pygame.init()

screen = pygame.display.set_mode(
    (width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

icon = pygame.image.load("Logo_Cristian_Color.png")
bg = pygame.image.load("bg.png").convert()

rend = Renderer(screen, 0.145, 0.588, 0.745)

rend.setShaders(vertex_shader, fragment_shader)

rend.target.z = -5

mod = Model("Teddy.obj", "Teddy.bmp")

# Positioning MODEL
mod.position.z -= 5
mod.position.y -= 1
mod.scale.x = 2
mod.scale.y = 2
mod.scale.z = 2
mod.rotation.y = 90

rend.pointLight.x -= 10

rend.scene.append(mod)

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
                if ctrl == 1:
                    rend.setShaders(vertex_shader, fragment_shader)
                elif ctrl == 2:
                    rend.setShaders(vertex_shader, fragment_shader_toon)
                elif ctrl == 3:
                    rend.setShaders(vertex_shader, fragment_shader_pop)
                elif ctrl == 4:
                    rend.setShaders(vertex_shader_expand, fragment_shader_red)
                elif ctrl == 5:
                    rend.setShaders(vertex_shader, fragment_shader_toonpop)
                ctrl += 1
                if ctrl == 6:
                    ctrl = 1

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
        rend.setShaders(vertex_shader, fragment_shader_pop)
    elif keys[K_4]:
        rend.setShaders(vertex_shader_expand, fragment_shader_red)
    elif keys[K_5]:
        rend.setShaders(vertex_shader, fragment_shader_toonpop)

    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
