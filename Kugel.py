import pygame

class Kugel(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Bilder/Kugel.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (15,15)) #Kugel verkleinern
        self.rect = self.image.get_rect(center = (400,400))

        #Vertikal test, dann x = 0
        #Startwerte und geschwindigkeit und Richtung
        self.x_val = -6
        self.y_val = -6

        self.speed_boost_time = 0 #Zeit Anfangswert
        self.boosted = False  #Zustand, Boost oder nicht?

        self.side_1 = 0 #Seite anfangswert

    def apply_gravity_del_heart_del_score(self,heart_rects,kugeln = 1,god_mode=0):

        #Damit sich die Kugel bewegt in Schritten
        self.rect.y = self.rect.y + self.y_val
        self.rect.x = self.rect.x + self.x_val

        #Wie viel speed soll entfernt werden?
        speed = 3

        #Reset der Geschwindigkeit nach 3 Sekunden
        if self.boosted and pygame.time.get_ticks() - self.speed_boost_time >= 5000: #Wenn 5 sek vergangen

            #Ändere geschwindigkeit
            if self.side_1 == 1:
                self.x_val -= speed
                self.y_val += speed

            if self.side_1 == 2:
                self.x_val += speed
                self.y_val += speed

            if self.side_1 == 3:
                self.x_val -= speed
                self.y_val -= speed

            if self.side_1 == 4:
                self.x_val += speed
                self.y_val -= speed

           
            self.boosted = False #Kein Boost mehr aktiv

        #TEST
        #if abs(self.x_val) < 2:
          #  self.x_val += 0.3 if self.x_val > 0 else -0.3

        #if abs(self.y_val) < 2:
           # self.y_val += 0.3 if self.y_val > 0 else -0.3

        #print("x: " ,self.x_val)
        #print("y: " ,self.y_val)

        #Wenn die Kugel den Boden berührt
        if self.rect.bottom >= 600:

            #Wenn wir zwei Kugeln haben, dann einen Löschen
            if kugeln == 2:
                self.kill()
            
            #Fliegt wieder oben diagonal rechts
            self.x_val = abs(self.x_val)
            self.y_val = -abs(self.y_val)

            #position zuruecksetzen
            self.rect.y = 400 
            self.rect.x = 400

            #God-Mode verhindert Herzverlust
            if god_mode == 1:
                return 0  # Keine Herzen verlieren und kein Game Over

            #Herzen überprüft
            if len(heart_rects) <= 1:
                del heart_rects[0] #Damit keine herzen mehr angezeigt werden, weil sonst einer übrig bleibt angezeigt
                return 3  #Game Over keine Herzen mehr

            # Herz wird hier entfernt und Score wird reduziert
            if heart_rects:  #Prüfen ob Herzen vorhanden sind

                del heart_rects[0]  # Entferne das oberste Herz

                return -1  # Punkte verlieren 
            
        
        # Kollision mit der linken Wand
        if self.rect.left <= 0: #Schauen, ob die linke seite der Kugel 0 ist
            self.x_val = abs(self.x_val) #Dann vorzeigen ändern
       
        # Kollision mit der oberen Wand
        if self.rect.top <= 0: #Schauen, ob die obere seite der Kugel 0 ist
            self.y_val = abs(self.y_val) #Dann vorzeigen ändern
   
        # Kollision mit der rechten Wand
        if self.rect.right >= 800: #Schauen, ob die rchte seite der Kugel 800 ist, also ganz rechts
            self.x_val = -abs(self.x_val) #Dann vorzeigen ändern

        #Test
        #print(self.x_val)
    
    
    #Speed-Boost hinzufügen
    def apply_speed_boost(self,side):
        
        #Auf welcher Seite
        self.side_1 = side

        speed = 3

        #Geschwindigkeit ändern
        if self.side_1 == 1:
            self.x_val -= speed
            self.y_val += speed

        if self.side_1 == 2:
            self.x_val += speed
            self.y_val += speed

        if self.side_1 == 3:
            self.x_val -= speed
            self.y_val -= speed

        if self.side_1 == 4:
            self.x_val += speed
            self.y_val -= speed
        
    
        self.speed_boost_time = pygame.time.get_ticks() #den Start speichern Zeit
        self.boosted = True #Der Boost ist aktiviert!

        


    



