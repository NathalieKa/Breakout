import pygame
import Kugel



class PowerUpBlock(pygame.sprite.Sprite):
    def __init__(self,x,y):
            super().__init__()

            #Bild
            self.image = pygame.image.load("Bilder/PowerUpBlock.png").convert_alpha()

            #Skalierung
            self.image = pygame.transform.scale(self.image, (68,25))

            #Postion
            self.rect = self.image.get_rect(center = (x,y))


    #Quelle: https://www.101computing.net/breakout-tutorial-using-pygame-adding-a-bouncing-ball/
    def collision_kugel(self,kugel,brick,kugeln_group,current_score):

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

            self.kill()

            brick.expand_brick(150) #expande den brick
            self.extra_ball(kugel, kugeln_group) #Füge extra ball hinzu

            current_score += 100  

        return current_score

    #Kugel erstellt
    def extra_ball(self, kugel,kugeln):

        #Alles wird von der ersten Kugel übernommen
        new_ball = Kugel.Kugel()
        new_ball.rect.x = kugel.rect.x
        new_ball.rect.y = kugel.rect.y
        new_ball.x_val = kugel.x_val
        new_ball.y_val = -kugel.y_val

        #Und in die Gruppe hinzugefügt
        kugeln.add(new_ball)
        

