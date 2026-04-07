import pygame

class explosion_animation(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.frames = [] #Liste mit Frames

        for i in range(1, 7): #Insgesamt 6 Frames
            frame = pygame.image.load(f"Bilder/explosion/frame_0{i}_delay-0.1s.png").convert_alpha()
            frame = pygame.transform.scale(frame, (80, 80))  #Skaliere  Bild 
            self.frames.append(frame) #Alle Frames in eine Liste packen

        self.index = 0 #index, um die liste durchzugehen

        self.image = self.frames[self.index] #erstes Frame anwenden

        self.rect = self.image.get_rect(center=(x, y)) #frames richtig an den explosiven blöcken platzieren
        
        self.animation_speed = 0.1 #Geschwindigkeit der Animation sek
        self.current_time = 0

    def update(self, dt):

        self.current_time += dt 

        if self.current_time >= self.animation_speed: #immer bei 0.1 sek ändert sich der frame

            self.current_time = 0
            self.index += 1

            if self.index >= len(self.frames):

                self.kill() #Entfernt die explosion, wenn die Animation vorbei ist

            else:

                #Wechsel Frame
                self.image = self.frames[self.index]