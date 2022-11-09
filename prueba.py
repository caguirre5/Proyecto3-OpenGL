import pygame
import pygame_menu

width = 1080
height = 720

# ------------------------INITS--------------------------------------
pygame.init()
# --------------------------------------------------------------


def hola():
    print("done")


screen = pygame.display.set_mode(
    (width, height))
clock = pygame.time.Clock()


menu = pygame_menu.Menu('Welcome', 400, 300,
                        theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name: ', default='')
menu.add.button('Play', hola)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
