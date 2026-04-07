import pygame


class Block_2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        #Bilder
        self.image1 = pygame.image.load("Bilder/Normal_Block_2Hit.png").convert_alpha()
        self.image2 = pygame.image.load("Bilder/Normal_Block_2Hit_2.png").convert_alpha()

        #Skalieren der Bilder
        self.image1 = pygame.transform.scale(self.image1, (68, 25))
        self.image2 = pygame.transform.scale(self.image2, (68, 25))

        #Setze das Startbild 
        self.image = self.image1
        self.rect = self.image.get_rect(center=(x, y))

        #Wie oft getroffen?
        self.hit = 0

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

            #Trefferzähler erhöhen
            self.hit += 1

            # Wechsel zu Bild 2 beim ersten Treffer
            if self.hit == 1:
                self.image = self.image2
                self.rect = self.image.get_rect(center=self.rect.center)  #Position beibehalten

            # Entfernen des Blocks beim zweiten Treffer
            elif self.hit >= 2:
                self.kill()


    #Score zurückgeben
    def return_score(self,kugel,current_score):

        if self.rect.colliderect(kugel.rect):
            if self.hit >=2:
                current_score += 100

        return current_score