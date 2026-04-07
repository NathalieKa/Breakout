import pygame


class prismen_block(pygame.sprite.Sprite):
    def __init__(self,x,y):
            super().__init__()

            self.image = pygame.image.load("Bilder/Prismen_Block.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (68,25))
            self.rect = self.image.get_rect(center = (x,y))

            self.side = 0 #Von welcher Seite wurde kollidiert

    #Quelle: https://www.101computing.net/breakout-tutorial-using-pygame-adding-a-bouncing-ball/
    def collision_kugel(self,kugel,current_score):

        if self.rect.colliderect(kugel.rect):
            
            #Kugel trifft von unten
            if kugel.rect.centery > self.rect.centery:  
                if kugel.rect.centerx < self.rect.centerx: #linke Seite, dann diagonal links nach unten   
                    kugel.y_val = abs(kugel.y_val)  
                    kugel.x_val = -abs(kugel.x_val) 
                    self.side = 1

                else: #rechte Seite, Rechts diagional unten
                    kugel.y_val = abs(kugel.y_val)  
                    kugel.x_val = abs(kugel.x_val)  
                    self.side = 2

            else:  #Kugel trifft von oben
                if kugel.rect.centerx < self.rect.centerx:  #linke Seite, diagonal oben links
                    kugel.y_val = -abs(kugel.y_val)  
                    kugel.x_val = -abs(kugel.x_val) 
                    self.side = 3
                    
                else:  #rechte Seite, Rechts diagional oben 
                    kugel.y_val = -abs(kugel.y_val) 
                    kugel.x_val = abs(kugel.x_val)  
                    self.side = 4

            #Booste kugel
            kugel.apply_speed_boost(self.side)

            #Score hiznufügen
            current_score += 100  

            #Zerstöre block
            self.kill()
        
        return current_score
    

    

       


            
              


