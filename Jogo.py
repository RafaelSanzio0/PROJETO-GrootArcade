import pygame, sys
from pygame.locals import *

import menuJogoGroot as menu


import random


class meteoro:
    image = pygame.image.load("imagem/meteoro.png")
    

class Recs:

    def __init__(self, numeroinicial):
        self.lista = []
        for x in range(numeroinicial):
            leftrandom = random.randrange(2,980)
            toprandom = random.randrange(-960,-10)

            width = random.randrange(5,15)
            height = random.randrange(5,15)
            self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))

    def mover(self):
        for meteoro in self.lista:
            meteoro.move_ip(1,7)

    def cor(self,superficie):
        for meteoro in self.lista:
            meteoroImagem =  pygame.image.load("imagem/meteoro2.png")
            screen.blit(meteoroImagem, meteoro)

    def recriar(self):

        for x in range(len(self.lista)):
            if self.lista[x].top > 901:
                leftrandom = random.randrange(2,980)
                toprandom = random.randrange(-960,-10)
                width = random.randrange(20,25)
                height = random.randrange(20,35)
                self.lista[x] = (pygame.Rect(leftrandom,toprandom,width,height))


class Player (pygame.sprite.Sprite):

    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (100,200)

    def movimento(self):
            if self.rect.left <= 0:
                self.rect.left = 0

            elif self.rect.right > 900:
                self.rect.right = 900

    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)

    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)

def colisao(player,recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False

def main():

        import pygame
        pygame.init()
        tela = pygame.display.set_mode((900,600))
        pygame.display.set_caption("Groot Arcade")

        sair = False
        relogio = pygame.time.Clock()

        img_groot = pygame.image.load("imagem/Baby_Groot3.png").convert_alpha()
        jogador = Player(img_groot)

        img_fundo = pygame.image.load("imagem/fundo2.jpg")
        img_explosao = pygame.image.load("imagem/explosao2.png")

        pygame.mixer.music.load("som/musica.mp3")
        pygame.mixer.music.play(3)

        som_sad = pygame.mixer.Sound("som/audio.wav")

        vx, vy = 0, 0
        velocidade = 10
        leftpress, rightpress, uppress, downpress = False, False, False, False

        texto = pygame.font.SysFont("Arial",30,True,False)

        ret = Recs(7)
        colidiu = False

        fonte_padrao = font = pygame.font.get_default_font()  # FONTE PADRAO
        fonte_perdeu = pygame.font.SysFont(fonte_padrao, 45)


        while sair != True:
            jogador.movimento()
            relogio.tick(120)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sair = True

                if colidiu == False:

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_LEFT:
                            leftpress = True
                            vx = - velocidade
                        if event.key == pygame.K_RIGHT:
                            rightpress = True
                            vx = velocidade
                        if event.key == pygame.K_UP:
                            uppress = True
                            vy = - velocidade
                        if event.key == pygame.K_DOWN:
                            downpress = True
                            vy = velocidade

                    if event.type == pygame.KEYUP:

                        if event.key == pygame.K_LEFT:
                            leftpress = False
                            if rightpress:
                                vx = velocidade
                            else:
                                vx = 0

                        if event.key == pygame.K_RIGHT:
                            rightpress = False
                            if leftpress:
                                vx = - velocidade
                            else:
                                vx = 0

                        if event.key == pygame.K_UP:
                            uppress = False
                            if downpress:
                                vx = velocidade
                            else:
                                vy = 0

                        if event.key == pygame.K_DOWN:
                            downpress = False
                            if uppress:
                             vx = - velocidade
                            else:
                                vy = 0

           


            if colisao(jogador,ret): # PEGA OS PARAMETROS JOGARDO E OS OBJ = HOUVE COLISAO
                
                tela.blit(img_fundo, (0, 0))
                text = fonte_perdeu.render("VOCE PERDEU :(", 1, (255,255,255))
                tela.blit(text, (300, 250))
                
                
                pygame.display.update()
                contador = texto.render("Pontuação: {}".format(segundos),0,(255,255,255))   # GUARDA A PONTUAÇÃO AO PERDER
                tela.blit(contador, (680, 10))
                colidiu = True
                jogador.imagem = img_explosao
                pygame.mixer.music.stop()
                som_sad.play()
                som_sad.set_volume(0.4)  # CONTROLA O VOLUME DO AUDIO
                
                #pygame.display.update()

                escolherOpcao = menu.menuJogo(tela, ['Jogar Novamente', 'Voltar para o menu', 'Sair do Jogo'], 62,500,None,32,1.4,white,white)

                if escolherOpcao == 0:
                    main()
                elif escolherOpcao == 1:
                    
                    pygame.display.set_caption("Groot Arcade")
                    som_sad.set_volume(0.0)
                    size = width, height = 900, 400
                    screen = pygame.display.set_mode(size)
                    backgroundGroot = background.get_rect()
                    screen.blit(background, backgroundGroot)
                    pygame.display.update()
                    pygame.key.set_repeat(500,30)
                    
                    choose = menu.menuJogo(screen, [

                            'Iniciar',
                            'Manual do Jogo',
                            'Sair'], 350,150,None,32,1.4,white,white)

                    


                    if choose == 0:
                        main()
                    elif choose == 1:
                        manualJogo()
                    elif choose == 2:
                        pygame.quit()
                elif escolherOpcao == 2:
                    pygame.quit()                
                    
                
            
                
                
            if colidiu == False:
                ret.mover()
                jogador.mover(vx, vy)
                tela.blit(img_fundo, (0, 0))
                segundos = pygame.time.get_ticks() / 1000
                segundos = str(segundos)
                contador = texto.render("Pontuação: {}".format(segundos),0,(255,255,255))  # CONTADOR DOS MEUS PONTOS
                tela.blit(contador, (680, 10))

            
            ret.cor(tela)
            ret.recriar()
            jogador.update(tela)

            


            
            
            pygame.display.update()

                    

        #pygame.quit()
        



#menu


red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0, 255
white = 255, 255, 255
brown = 205,170,125
pygame.init()
size = width, height = 900, 400
screen = pygame.display.set_mode(size)
screen2 = pygame.display.set_mode(size)
background = pygame.image.load('imagem/menuBackground.png')

backgroundGroot = background.get_rect()
screen.blit(background, backgroundGroot)
pygame.display.update()
pygame.key.set_repeat(500,30)


def iniciar():
    pygame.display.set_caption("Groot Arcade")
    backgroundGroot = background.get_rect()
    screen.blit(background, backgroundGroot)
    pygame.display.update()
    pygame.key.set_repeat(500,30)       
    choose = menu.menuJogo(screen, [

                            'Iniciar',
                            'Manual do Jogo',
                            'Sair'], 350,150,None,32,1.4,white,white)


    if choose == 0:
        main()
    elif choose == 1:
        manualJogo()
    elif choose == 2:
        pygame.quit()




def manualJogo():
    tela = pygame.display.set_mode((900, 400))
    pygame.display.set_caption("Groot Arcade")

    background = pygame.image.load('menuBackground.png')
    backgroundGroot = background.get_rect()
    screen.blit(background, backgroundGroot)
    

    fonte = pygame.font.SysFont(None, 32)
    texto = fonte.render("Instruções:", 1, (white))
    texto2 = fonte.render("- Utilize as setas do teclado para movimentar o Groot", 1, (white))
    texto3 = fonte.render("- Uma chuva de meteoros irá cair sob o Groot,", 1, (white))
    texto4 = fonte.render("  Seu objetivo é desviar dos meteoross durante", 1, (white))
    texto5 = fonte.render("  o maior tempo possível", 1, (white))
    
    screen.blit(texto, (50,50))
    screen.blit(texto2, (50,90))
    screen.blit(texto3, (50,120))
    screen.blit(texto4, (50,150))
    screen.blit(texto5, (50,180))

    pygame.display.update()

    escolha = menu.menuJogo(screen, [

                        'Começar a jogar', 'Voltar'], 62,300,None,32,1.4,white,white)


    if escolha == 0:
        main()
    elif escolha == 1:
        iniciar()    

    pygame.display.update()
    
def iniciarJogo():
    if choose == 0:
        main()
    elif choose == 1:
        manualJogo()
    elif choose == 2:
        pygame.quit()



    
  
iniciar()
    




