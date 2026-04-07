import pygame
import random


class unbreakable_block(pygame.sprite.Sprite):
    def __init__(self,x,y):
            super().__init__()

            #Bild
            self.image = pygame.image.load("Bilder/Unzerbrechlicher_Block.png").convert_alpha()

            #Skalierung
            self.image = pygame.transform.scale(self.image, (68,25))

            #Position
            self.rect = self.image.get_rect(center = (x,y))


    #Quelle: https://www.101computing.net/breakout-tutorial-using-pygame-adding-a-bouncing-ball/
    def collision_kugel(self,kugel):

        if self.rect.colliderect(kugel.rect):
            
            #Kugel trifft von unten
            if kugel.rect.centery > self.rect.centery: 

                if kugel.rect.centerx < self.rect.centerx: #linke Seite, dann diagonal links nach unten
                    kugel.y_val = abs(kugel.y_val)  
                    kugel.x_val = -abs(kugel.x_val)  

                else:  #rechte Seite, Rechts diagional unten
                    kugel.y_val = abs(kugel.y_val)  
                    kugel.x_val = abs(kugel.x_val)

            else:  #Kugel trifft von oben
                if kugel.rect.centerx < self.rect.centerx: #linke Seite, diagonal oben links
                    kugel.y_val = -abs(kugel.y_val)  
                    kugel.x_val = -abs(kugel.x_val)  

                else:  #rechte Seite, Rechts diagional oben 
                    kugel.y_val = -abs(kugel.y_val)  
                    kugel.x_val = abs(kugel.x_val)  

            #Abprallwinkel ändern, damit es nicht stecken bleibt
            kugel.x_val += random.choice([-0.3, 0.3])
            kugel.y_val += random.choice([-0.3, 0.3])


