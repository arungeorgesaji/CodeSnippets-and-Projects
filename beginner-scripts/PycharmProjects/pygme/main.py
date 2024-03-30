import pygame
pygame.init()
screen =pygame.display.set_mode((800,600))
running =True
pygame.display.set_caption("impossible run")
icon =pygame.image.load('WIN_20211105_09_35_49_Pro.jpg')
pygame.display.set_icon(icon)
playerimg =pygame.image.load('spaceship.png')
playerX =370
playerY =480
playerX_change =0
def player(x,y):
   screen.blit(playerimg, (x,y))
while True:
   screen.fill((0, 0, 0))

   for event in pygame.event.get():
    if event.type ==pygame.QUIT:
        running =False

        if event.type ==pygame.KEYDOWN:

            if event.type ==pygame.K_l:
                playerX_change = -0.3
            if event.type ==pygame.K_r:
                playerX_change = 0.3
        if event.type ==pygame.KEYUP:
         if event.type ==pygame.K_l or event.type ==pygame.K_r:
          playerX_change = 0


    playerX +=playerX_change
    player(playerX,playerY)
    pygame.display.update()
