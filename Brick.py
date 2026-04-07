import pygame
import random

class Brick(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Bilder/brick.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,20)) #Kugel verkleinern
        self.rect = self.image.get_rect(center = (400,500))

        self.collision_soundeffect = pygame.mixer.Sound("Music/brick_sound.mp3")

    
    #BALKEN-IDEE Quelle: https://stackoverflow.com/questions/48913087/get-just-the-x-or-y-pos-with-pygame-mouse-get-pos
    def move_brick(self):
        mouse_x = pygame.mouse.get_pos()[0]
        self.rect.centerx = mouse_x

    #Quelle: https://www.101computing.net/breakout-tutorial-using-pygame-adding-a-bouncing-ball/
    def collision(self, kugel):
        if self.rect.colliderect(kugel.rect):

            self.collision_soundeffect.play()
            
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


            #Abprallwinkels aber nicht die Geschwindigkeit komplett verändern
            kugel.x_val += random.choice([-0.2, 0.2])

            #Begrenzung der maximalen Geschwindigkeit
            max_speed = 9
            kugel.x_val = max(-7, min(max_speed, kugel.x_val))
            kugel.y_val = max(-7, min(max_speed, kugel.y_val))


    #Quelle: https://www.101computing.net/breakout-tutorial-using-pygame-adding-a-bouncing-ball/
    def collision_without_maxspeed(self, kugel):
        if self.rect.colliderect(kugel.rect):

            self.collision_soundeffect.play()
            
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

            #Abprallwinkels aber nicht die Geschwindigkeit komplett verändern
            kugel.x_val += random.choice([-0.2, 0.2])


    #Reset Position
    def reset_pos(self):
        self.rect = self.image.get_rect(center = (400,500))
        self.image = pygame.transform.scale(self.image, (100, 20))
            
    #Brick expanden
    def expand_brick(self, new_width):
        self.image = pygame.transform.scale(self.image, (new_width, self.rect.height))
        self.rect = self.image.get_rect(center=self.rect.center)  #Position beibehalten

        