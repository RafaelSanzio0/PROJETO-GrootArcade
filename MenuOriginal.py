import pygame
import menuJogoGroot as menu
pygame.init()

# Just a few static variables
red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0, 255
white = 255, 255, 255
brown = 205,170,125

size = width, height = 900, 400
screen = pygame.display.set_mode(size)
background = pygame.image.load('menuBackground.png')

backgroundGroot = background.get_rect()
screen.blit(background, backgroundGroot)
pygame.display.update()
pygame.key.set_repeat(500,30)

choose = menu.menuJogo(screen, [

                        'Start Game',
                        'Options',
                        'Manual',
                        'Quit Game'], 350,150,None,32,1.4,brown,brown)

if choose == 0:
    print("You choose 'Start Game'.")
elif choose == 1:
    print( "You choose 'Options'.")
elif choose == 2:
    print("You choose 'Manual'.")
elif choose == 3:
    print("You choose 'Quit Game'.")
pygame.quit()
exit()
