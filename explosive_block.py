import pygame
import explosive_animation


class explosive_block(pygame.sprite.Sprite):
    def __init__(self,x,y):
            super().__init__()

            self.image = pygame.image.load("Bilder/Explosiver_Block.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (68,25))
            self.rect = self.image.get_rect(center = (x,y))

            self.explosion_soundeffect = pygame.mixer.Sound("Music/explosion_sound.wav")


    #Quelle: https://www.101computing.net/breakout-tutorial-using-pygame-adding-a-bouncing-ball/
    def collision_kugel(self, kugel, blocks_group, explosion_group, current_score):
        if self.rect.colliderect(kugel.rect):

            self.explosion_soundeffect.play() #soundeffekt

            #https://stackoverflow.com/questions/66798261/i-dont-know-when-i-have-to-use-centerx-and-centry
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
                    
            #Startet die Explosion an der Position 
            explosion = explosive_animation.explosion_animation(self.rect.centerx, self.rect.centery)
            explosion_group.add(explosion)

            self.kill()

            #Explodiert und aktualisiert den Score
            current_score = self.explode(blocks_group, current_score)
            current_score += 100  # Punkte für den explosiven Block selbst

        return current_score
    
    #Quelle: https://stackoverflow.com/questions/66624936/pygame-i-want-to-calculate-the-distance-between-the-player-sprite-and-enemy1
    def explode(self, blocks_group, current_score):
        explosion_radius = 76  #Radius der Explosion 
        nearby_blocks = [] 

        for block in blocks_group:
            if pygame.math.Vector2(block.rect.center).distance_to(self.rect.center) < explosion_radius: #Sind die blöcke innerhalb radius?
                nearby_blocks.append(block) #Dann in die Gruppe hinzufügen

        for block in nearby_blocks: #Dann zerstöre sie und rechne Score dazu
            block.kill()
            current_score += 100  # Punkte für jeden zerstörten benachbarten Block

        return current_score