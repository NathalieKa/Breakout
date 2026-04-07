import pygame
import Block_2
import unbreakable_block
import explosive_block
import prismen_block
import powerUp_block

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        #Bild
        self.image = pygame.image.load("Bilder/Normal_Block.png").convert_alpha()

        #Skalierung
        self.image = pygame.transform.scale(self.image, (68,25))

        #Platzierung
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


            self.kill() #entferne Block
            
    
    #Geben Score zurück
    def return_score(self, kugel, current_score):
    
        #Überprüfe, ob die Kugel mit dem Block kollidiert
        if self.rect.colliderect(kugel.rect):
                current_score += 100  #Punkte hinzufügen  

        return current_score
            

    
#--------------Felder erstellen---------------------

    #--Für Level-1 --Erstelltes Feld--
    def create_field(self):
        self.blocks = pygame.sprite.Group()
        x = 50
        y = 20

        for i in range(6):
            for k in range(11):
    
                #Block_2 hinzufügen
                if i <= 2:
                    block_2 = Block_2.Block_2(x,y)
                    self.blocks.add(block_2)

                #Block hinzufügen
                else:
                    block = Block(x,y)
                    self.blocks.add(block)
                x += 70

            y += 28
            x = 50 #reseten
            
        return self.blocks
    

    def create_field_level_2(self):

        blocks_group = pygame.sprite.Group() #Erstelle Gruppe

        #Layout mit 6 Reihen
        layout = [
            ['B','B' ,'B' ,'B' ,'B','B','B' ,'B' ,'B' ,'B','B'],  
            ['B','B2' ,'B2' ,'B2' ,'B','B','B' ,'B2' ,'B2' ,'B2','B'],
            ['B','B2' ,'U' ,'B2' ,'B','B','B','B2' ,'U' ,'B2','B'],
            ['B','B2' ,'U' ,'B2' ,'B','B','B' ,'B2' ,'U' ,'B2','B'],
            ['B','B2' ,'B2' ,'B2' ,'B','B','B' ,'B2' ,'B2' ,'B2','B'],
            ['B','B' ,'B' ,'B' ,'B','B','B' ,'B' ,'B' ,'B','B']
           
        ]

        x_start = 50  #Start
        y_start = 20  #Start
        x_offset = 70  #Abstand X-Richtung
        y_offset = 28  #Abstand Y-Richtung

        for row_index, row in enumerate(layout): #Iteriere durch die Zeilen und Reihen
            for col_index, block_type in enumerate(row): #Reihe iterieren
                x = x_start + col_index * x_offset #Koordinaten berechnen
                y = y_start + row_index * y_offset

                if block_type == 'B':
                    block = Block(x, y) #Platziere den Block an der Koordinate

                elif block_type == 'B2':
                    block = Block_2.Block_2(x, y)

                elif block_type == 'U':
                    block = unbreakable_block.unbreakable_block(x, y)

                elif block_type == 'E':   
                    block = explosive_block.explosive_block(x, y)

                blocks_group.add(block)

        return blocks_group
    

    def create_field_level_3(self):
        blocks_group = pygame.sprite.Group()

        #Layout mit 6 Reihen
        layout = [
            ['B','B' ,'B2' ,'B' ,'B','B2','B' ,'B' ,'B2' ,'B','B'],  
            ['B','B' ,'B2' ,'B' ,'B','B2','B' ,'B' ,'B2' ,'B','B'],
            ['B','B' ,'B2' ,'B' ,'B','B2','B' ,'B' ,'B2' ,'B','B'],
            ['B','B2' ,'E' ,'B2' ,'B2','P','B2' ,'B2' ,'E' ,'B2','B'],
            ['B','B' ,'B2' ,'B' ,'B','B2','B' ,'B' ,'B2' ,'B','B'],
            ['B','B' ,'B' ,'B' ,'B','B','B' ,'B' ,'B' ,'B','B'] 
        ]

        x_start = 50  #Start
        y_start = 20  #Start
        x_offset = 70  #Abstand X-Richtung
        y_offset = 28  #Abstand Y-Richtung

        for row_index, row in enumerate(layout): #Iteriere durch die Zeilen und Reihen
            for col_index, block_type in enumerate(row): #Reihe iterieren
                x = x_start + col_index * x_offset #Koordinaten berechnen
                y = y_start + row_index * y_offset

                #Platziere den Block an der Koordinate
                if block_type == 'B':
                    block = Block(x, y)
                elif block_type == 'B2':
                    block = Block_2.Block_2(x, y)
                elif block_type == 'U':
                    block = unbreakable_block.unbreakable_block(x, y)
                elif block_type == 'E':
                    block = explosive_block.explosive_block(x, y)
                elif block_type == 'P':
                    block = prismen_block.prismen_block(x, y)
                

                blocks_group.add(block)

        return blocks_group



    def create_field_level_4(self):
        blocks_group = pygame.sprite.Group()

        #Layout mit 6 Reihen
        layout = [
            ['B','B' ,'B' ,'B' ,'B','B','B' ,'B' ,'B' ,'B','B'],  # Reihe 1 (oben)
            ['B','B2' ,'B2' ,'B2' ,'B2','B2','B2' ,'B2' ,'B2' ,'B2','B'],
            ['B','B2' ,'B' ,'B' ,'B','P','B' ,'B' ,'B' ,'B2','B'],
            ['B','E' ,'B' ,'B' ,'B','P2','B' ,'B' ,'B' ,'E','B'],
            ['B','B2' ,'B' ,'B' ,'B','B','B' ,'B' ,'B' ,'B2','B'],
            ['B','B2' ,'B2' ,'B2' ,'B2','B2','B2' ,'B2' ,'B2' ,'B2','B'],
            ['B','B' ,'B' ,'B' ,'B','B','B' ,'B' ,'B' ,'B','B']
        ]

        x_start = 50  #Start
        y_start = 20  #Start
        x_offset = 70  #Abstand X-Richtung
        y_offset = 28  #Abstand Y-Richtung

        for row_index, row in enumerate(layout): #Iteriere durch die Zeilen und Reihen
            for col_index, block_type in enumerate(row): #Reihe iterieren
                x = x_start + col_index * x_offset #Koordinaten berechnen
                y = y_start + row_index * y_offset


                #Platziere den Block an der Koordinate
                if block_type == 'B':
                    block = Block(x, y)
                elif block_type == 'B2':
                    block = Block_2.Block_2(x, y)
                elif block_type == 'U':
                    block = unbreakable_block.unbreakable_block(x, y)
                elif block_type == 'E':
                    block = explosive_block.explosive_block(x, y)
                elif block_type == 'P':
                    block = prismen_block.prismen_block(x, y)
                elif block_type == 'P2':
                    block = powerUp_block.PowerUpBlock(x,y)
                

                blocks_group.add(block)

        return blocks_group
            

                    