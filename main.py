import pygame
from sys import exit
import Kugel
import Brick
import Block
from unbreakable_block import unbreakable_block
from explosive_block import explosive_block
from prismen_block import prismen_block
import powerUp_block

#Quellen:
#Pygame-Tutorial:https://www.youtube.com/watch?v=AY9MnQ4x3zk / https://www.youtube.com/watch?v=4TfZjhw0J-8&t=6s
#Musik: https://opengameart.org/content/5-chiptunes-action
#Grafik/Bilder: https://opengameart.org/content/breakout-brick-breaker-tile-set-free
#https://opengameart.org/content/breakout-game-assets
#Hintergrund: https://www.pinterest.de/pin/532972937153703127/
#https://www.pygame.org/docs/tut/newbieguide.html
#heart: https://www.pngwing.com/en/free-png-veink
#Fonts: https://www.fontspace.com/super-pixel-font-f112028 / https://www.fontspace.com/pixel-game-font-f121080
#Gif: https://www.reddit.com/r/PixelArt/comments/19a2cv1/explosion/
#soundeffect: https://pixabay.com/de/users/pixabay-1/
#https://samplefocus.com/samples/8-bit-explosion
#https://www.101computing.net/breakout-tutorial-using-pygame-adding-a-bouncing-ball/



# Diese Funktion initialisiert alle importierten Pygame-Module,
# die für die Interaktion mit Ihrem Computersystem benötigt werden.
pygame.init()

#Musik
pygame.mixer.init()

#Fenstergröße
screen = pygame.display.set_mode((800, 600))  

#convert: Das Bild wird einmalig in das passende Pixelformat umgewandelt. Danach kann es schneller gezeichnet werden.
background_surf = pygame.image.load('Bilder/hintergrund.png').convert() #Hintergrundbild
background_surf = pygame.transform.scale(background_surf, (800,600))

#Schriftarten
font_score = pygame.font.Font("Fonts/PIXEL.ttf", 22)
font_title = pygame.font.Font('Fonts/SuperPixel.ttf', 80) 
font_title2 = pygame.font.Font('Fonts/SuperPixel.ttf', 60) 
font_button = pygame.font.Font('Fonts/SuperPixel.ttf', 20) 
font_button2 = pygame.font.Font('Fonts/SuperPixel.ttf', 15) 
font_text = pygame.font.Font("Fonts/PIXEL.ttf", 40)
font_title_won = pygame.font.Font('Fonts/SuperPixel.ttf', 80) 
font_score2 = pygame.font.Font("Fonts/PIXEL.ttf", 45)

#Herz
heart_surf = pygame.image.load("Bilder/heart.png").convert_alpha()
heart_surf = pygame.transform.scale(heart_surf, (35,35))

#Stern
star_surf = pygame.image.load("Bilder/stern.png").convert_alpha()
star_surf = pygame.transform.scale(star_surf, (80,80))
star_surf2 = pygame.transform.scale(star_surf, (25,25))

# Globale Variable um den höchsten Sternenwert zu speichern
max_stars_level_1 = 0
max_stars_level_2 = 0
max_stars_level_3 = 0
max_stars_level_4 = 0

#Texte
text_start = font_score.render("Press SPACE to start the game", False, (255, 255, 255)).convert()
text_start_rect = text_start.get_rect(center =(400,300))

game_over_text = font_title.render("GAME OVER", False, (255, 0, 31)).convert()
game_over_text_rect = game_over_text.get_rect(center =(400,250))

restart_text = font_score.render("Press SPACE to restart", False, (243, 255, 0)).convert()
restart_text_rect = restart_text.get_rect(center =(400,340))

won_text = font_title2.render("LEVEL COMPLETE", False, (236, 255, 0)).convert()
won_text_rect = won_text.get_rect(center =(400,150))

return_text = font_score.render("Press ESC to return to the Level Menu", False,(37, 220, 0)).convert()
return_text_rect = return_text.get_rect(center = (400,430))

return_text2 = font_score.render("Press ESC to return to the Level Menu", False,(0, 155, 255 )).convert()
return_text_rect2 = return_text.get_rect(center = (400,340))

no_star_text = font_text.render("NO STARS ACHIEVED",False,(255, 0, 0)).convert()
no_star_text_rect = no_star_text.get_rect(center = (400,260))

#Frame 
clock = pygame.time.Clock()  #framerate 60

#God Mode Switch 
god_mode = 0  # 0 = off und 1 = on

volume = 1.0 #Lautstärke am Anfang

#Funktionen
#Farbe wir nach der Kollision Lila
def collide_button(rect, pos, button_name):

    if rect.collidepoint(pos):

        return font_score.render(button_name, False, (0, 147, 255)).convert()
    
    else:

        return font_score.render(button_name, False, (255, 255, 255)).convert()
    
#Musik wird dadurch nicht zurückgesetzt wenn Musik bereits läuft
def start_music():

    if not pygame.mixer.music.get_busy():  # Überprüfenob Musik bereits läuft

        pygame.mixer.music.load("Music/Menü.wav")
        pygame.mixer.music.play(-1)  #Musik in Endlosschleife abspielen


def start_game():

    #Listen mit Sternen
    star_rects_level_1 = [
    star_surf2.get_rect(topleft = (320,200)),
    star_surf2.get_rect(topleft = (350,200)),
    star_surf2.get_rect(topleft = (380,200))
    ]
    star_rects_level_2 = [
    star_surf2.get_rect(topleft = (320,250)),
    star_surf2.get_rect(topleft = (350,250)),
    star_surf2.get_rect(topleft = (380,250))
    ]
    star_rects_level_3 = [
    star_surf2.get_rect(topleft = (320,300)),
    star_surf2.get_rect(topleft = (350,300)),
    star_surf2.get_rect(topleft = (380,300))
    ]
    star_rects_level_4 = [
    star_surf2.get_rect(topleft = (320,350)),
    star_surf2.get_rect(topleft = (350,350)),
    star_surf2.get_rect(topleft = (380,350))
    ]

    clock = pygame.time.Clock()  # framerate 60
    pygame.display.set_caption("START-GAME")  # Titel

    #LEVEL-1-BUTTON
    level_1_surf = font_score.render("Level 1", False, (255, 255, 255)).convert()
    level_1_rect = level_1_surf.get_rect(topleft = (200,200))

    #LEVEL-2-BUTTON
    level_2_surf = font_score.render("Level 2", False, (255, 255, 255)).convert()
    level_2_rect = level_2_surf.get_rect(topleft = (200,250))

    #LEVEL-3-BUTTON
    level_3_surf = font_score.render("Level 3", False, (255, 255, 255)).convert()
    level_3_rect = level_3_surf.get_rect(topleft = (200,300))

    #LEVEL-4-BUTTON
    level_4_surf = font_score.render("Level 4", False, (255, 255, 255)).convert()
    level_4_rect = level_4_surf.get_rect(topleft = (200,350))

    #Musik laden und abspielen
    start_music()


    while True:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Das QUIT-Ereignis tritt auf, wenn der Benutzer versucht, das Pygame-Fenster zu schließen. Dies kann geschehen, indem der Benutzer auf das “X” in der Ecke des Fensters klickt
            if event.type == pygame.QUIT:
                pygame.quit()  # Es wird nicht richtig beendet (Error)
                exit()  # endet die while schleife (break)
            
            #Hier wird überprüft, ob die Maus auf die Button klickt
            if event.type == pygame.MOUSEBUTTONDOWN:

                #Wenn Level 1 angeklickt wurde, dann wird die level_1() funktion aufgerufen
                if level_1_rect.collidepoint(event.pos):
                    level_1()

                if level_2_rect.collidepoint(event.pos):
                    level_2()

                if level_3_rect.collidepoint(event.pos):
                    level_3()

                if level_4_rect.collidepoint(event.pos):
                    level_4()

            #Wenn wir ESCAPE drücken, kommen wir wieder ins Menü
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   main_menu()


        #Hintergrund anzeigen
        screen.blit(background_surf,(0,0))

        #Hier werden die Sterne angezeigt und überprüft, wie viele erreicht wurden
        #Level-1
        if max_stars_level_1 == 3:
            counter_stars = star_rects_level_1[:3] #Entnehme alle aus der Liste
            for rects in counter_stars:
                screen.blit(star_surf2, rects)

        if max_stars_level_1 == 2:
            counter_stars = star_rects_level_1[:2] #Entnehme 2 aus der Liste
            for rects in counter_stars:
                screen.blit(star_surf2, rects)

        if max_stars_level_1 == 1:
            counter_stars = star_rects_level_1[:1] #Entnehme 1 aus der Liste
            for rects in counter_stars:
                screen.blit(star_surf2, rects)

        #Level-2
        if max_stars_level_2 == 3:
            counter_stars = star_rects_level_2[:3]
            for rects in counter_stars:
                screen.blit(star_surf2, rects)
 
        if max_stars_level_2 == 2:
            counter_stars = star_rects_level_2[:2]
            for rects in counter_stars:
                screen.blit(star_surf2, rects)

        if max_stars_level_2 == 1:
            counter_stars = star_rects_level_2[:1]
            for rects in counter_stars:
                screen.blit(star_surf2, rects)

        #Level-3
        if max_stars_level_3 == 3:
            counter_stars = star_rects_level_3[:3]
            for rects in counter_stars:
                screen.blit(star_surf2, rects)

        if max_stars_level_3 == 2:
            counter_stars = star_rects_level_3[:2]
            for rects in counter_stars:
                screen.blit(star_surf2, rects)

        if max_stars_level_3 == 1:
            counter_stars = star_rects_level_3[:1]
            for rects in counter_stars:
                screen.blit(star_surf2, rects)

        #Level-4
        if max_stars_level_4 == 3:
            counter_stars = star_rects_level_4[:3]
            for rects in counter_stars:
                screen.blit(star_surf2, rects)

        if max_stars_level_4 == 2:
            counter_stars = star_rects_level_4[:2]
            for rects in counter_stars:
                screen.blit(star_surf2, rects)

        if max_stars_level_4 == 1:
            counter_stars = star_rects_level_4[:1]
            for rects in counter_stars:
                screen.blit(star_surf2, rects)

    
        #Hier werden die Buttons durch die Kollision der Maus Lila
        level_1_surf = collide_button(level_1_rect, mouse_pos, "Level 1")
        level_2_surf = collide_button(level_2_rect, mouse_pos, "Level 2")
        level_3_surf = collide_button(level_3_rect, mouse_pos, "Level 3")
        level_4_surf = collide_button(level_4_rect, mouse_pos, "Level 4")

        #Hier werden die Levels-Texte angezeigt
        screen.blit(level_1_surf,level_1_rect)
        screen.blit(level_2_surf,level_2_rect)
        screen.blit(level_3_surf,level_3_rect)
        screen.blit(level_4_surf,level_4_rect)

        pygame.display.update()
        clock.tick(60)  #nicht schneller als 60 mal pro sekunde


def main_menu():

    pygame.display.set_caption("Breakout") #Titel
    clock = pygame.time.Clock() 

    #Titel
    text_title_surf = font_title.render("Breakout", False, (255, 255, 255)).convert()
    text_title_rect = text_title_surf.get_rect(center = (400,140))

    #START-GAME-BUTTON
    startgame_title_surf = font_button.render("START GAME", False, (255, 255, 255)).convert()
    startgame_title_rect = startgame_title_surf.get_rect(center = (400,270))

    #SURVIVALMODE-BUTTON
    survival_title_surf = font_button.render("SURVIVAL-MODE", False, (255, 255, 255)).convert()
    survival_title_rect = survival_title_surf.get_rect(center = (400,310))

    #SETTINGS_BUTTON
    setting_title_surf = font_button.render("SETTINGS", False, (255, 255, 255)).convert()
    setting_title_rect = setting_title_surf.get_rect(center = (400,350))

    #TUTORIAL-BUTTON
    tutorial_title_surf = font_button.render("TUTORIAL", False, (255, 255, 255)).convert()
    tutorial_title_rect = tutorial_title_surf.get_rect(center = (400,390))

    #QUIT-BUTTON
    quit_title_surf = font_button.render("QUIT", False, (255, 255, 255)).convert()
    quit_title_rect = quit_title_surf.get_rect(center = (400,430))

    #Musik
    start_music()


    while True:

        #Mouse-Position
        mouse_pos = pygame.mouse.get_pos()

        # pygame.event.get(): ist eine Funktion, die eine Liste aller Ereignisse zurückgibt, die seit dem letzten Aufruf der Funktion aufgetreten sind.
        # Ereignisse können Dinge wie Tastendrücke, Mausbewegungen oder Klicks, das Schließen des Fensters und so weiter sein.
        # Und for event: ist eine Schleife, die über jedes Ereignis in dieser Liste geht.
        for event in pygame.event.get():
            # Das QUIT-Ereignis tritt auf, wenn der Benutzer versucht, das Pygame-Fenster zu schließen. Dies kann geschehen, indem der Benutzer auf das “X” in der Ecke des Fensters klickt
            if event.type == pygame.QUIT:
                pygame.quit()  # Es wird nicht richtig beendet (Error)
                exit()  # endet die while schleife (break)

            #Wenn mit der Maus auf die Buttons geklickt wurde, werden die Funktionen aufgerufen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_title_rect.collidepoint(event.pos):
                    pygame.quit() 
                    exit()  

                if startgame_title_rect.collidepoint(event.pos):
                    start_game()

                if survival_title_rect.collidepoint(event.pos):
                    survival_mode()

                if setting_title_rect.collidepoint(event.pos):
                    settings()

                if tutorial_title_rect.collidepoint(event.pos):
                    tutorial()


        #Hier überprüfen ob die Maus über dem Button ist
        quit_title_surf = collide_button(quit_title_rect, mouse_pos, "QUIT")
        startgame_title_surf = collide_button(startgame_title_rect, mouse_pos, "START GAME")
        survival_title_surf = collide_button(survival_title_rect,mouse_pos,"SURVIVAL-MODE")
        setting_title_surf = collide_button(setting_title_rect, mouse_pos, "SETTINGS")
        tutorial_title_surf = collide_button(tutorial_title_rect,mouse_pos,"TUTORIAL")

       #Main-Menu Texte
        screen.blit(background_surf, (0,0))
        screen.blit(text_title_surf,text_title_rect)
        screen.blit(startgame_title_surf,startgame_title_rect)
        screen.blit(survival_title_surf,survival_title_rect)
        screen.blit(setting_title_surf,setting_title_rect)
        screen.blit(tutorial_title_surf,tutorial_title_rect)
        screen.blit(quit_title_surf,quit_title_rect)


        #Die Funktion pygame.display.update() nimmt diesen “Hintergrund” und kopiert ihn auf den Bildschirm, so dass die Änderungen sehen können.
        pygame.display.update()
        clock.tick(60) 


def level_1():

    #god-mode
    global god_mode 
    global max_stars_level_1 #Wie viele Sterne wurden erreicht

    #Level-1-Text
    text_level = font_score.render(f"Level 1", False, (0,0,0)).convert()
    text_level_rect = text_level.get_rect(midbottom = (400,590))

    #Liste (Herzen)
    heart_rects = [
    heart_surf.get_rect(bottomright = (780,590)),  
    heart_surf.get_rect(bottomright = (745,590)),
    heart_surf.get_rect(bottomright = (710,590))  
    ]
    #Liste (Sternen)
    star_rects = [
    star_surf.get_rect(center = (300,255)),
    star_surf.get_rect(center = (400,255)),
    star_surf.get_rect(center = (500,255))
    ]

    #Groups erstellen
    #Group-Kugel-Brick
    kugel = Kugel.Kugel()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(kugel)
    brick = Brick.Brick()
    all_sprites.add(brick)

    #Group-Block
    blocks_group = pygame.sprite.Group()
    block = Block.Block(0,0)
    blocks = block.create_field()
    blocks_group.add(blocks)
    
    #Titel
    pygame.display.set_caption("Level 1") 
    
    #Variablen
    pause_game = 1 #Switche zwischen den Bildschirmen, also Game-over und win...
    current_score = 0 #Score ist am anfang 0
    counter_stars = 0 #Wie viele Sterne wurden erreicht

    #Musik
    pygame.mixer.music.load("Music/Level_1.wav")
    pygame.mixer.music.play(-1) #endlosschleife

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                exit()  

            #Sobald SPACE gedrueckt wird
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_SPACE:
                    
                    #Herzen werden nur bei einem Game-over oder Win zurückgesetzt 
                    if pause_game == 3 or pause_game == 4:
                        heart_rects = [
                            heart_surf.get_rect(bottomright = (780,590)),  
                            heart_surf.get_rect(bottomright = (745,590)),
                            heart_surf.get_rect(bottomright = (710,590))  
                           ]
                        
                        #Alles zurücksetzen
                        blocks_group.empty() #Feld leeren
                        blocks_group = block.create_field() #Neues Feld erstellen #FEHLER
                        brick.reset_pos() #Reset Brick pos
                        current_score = 0  #Reset Score
                        kugel.rect.y = 400  #Reset Kugel-Position
                        kugel.rect.x = 400

                        #Reset Bahn
                        kugel.x_val = -5 
                        kugel.y_val = -5
                        
                        #Starte wieder das eigentliche Game
                        pause_game = 2
      
                    #Startet das Game durch Space im Start Fenster
                    if pause_game == 1:
                        pause_game = 2 #Startet das eigentliche game

            #Wenn Escape gedrückt wurde dann, gehe zurück
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop() #musik stoppen
                        start_game()
                        


        #Hintergrund und Texte anzeigen
        screen.blit(background_surf, (0,0))
        screen.blit(text_level,text_level_rect)
        
        #Gruppen anzeigen lassen
        all_sprites.draw(screen) #Kugel und Brick anzeigen
        blocks_group.draw(screen) #Alle Blöcke anzeigen

        #Herzen durchgehen und anzeigen
        for rect in heart_rects:
            screen.blit(heart_surf, rect)

        #SCORE aktuell anzeigen lassen am Anfang
        text_score = font_score.render(f"YOUR SCORE: {current_score} ", False, (0, 0, 0)).convert()
        text_score_rect = text_score.get_rect(bottomleft = (10,590))
        screen.blit(text_score,text_score_rect)

        #1--Start-Bildschirm
        if pause_game == 1:
            #Text: Das spiel mit der Space taste starten
            screen.blit(text_start,text_start_rect)
            screen.blit(return_text2,return_text_rect2)
        
        #2--Startet das eigentliche Game
        if pause_game == 2:

            #brick bewegen
            brick.move_brick() 

            #Kollision mit Kugel
            brick.collision(kugel)

            #Wenn Kugel Boden berührt und Herz verliert und Score verliert
            game_status = kugel.apply_gravity_del_heart_del_score(heart_rects,god_mode=god_mode)

            #Score wird abgezogen wenn -1 zurückgegeben
            if game_status == -1:
                current_score -= 1000 

            #Game-Over wenn 3 zurückgegeben
            if game_status == 3:
                pause_game = 3

            #Prüft welcher Block mit der Kugel kollidiert und alles durchgehen in der Gruppe
            for block in blocks_group:
                block.collision_kugel(kugel) #wurde block getroffen?
                current_score = block.return_score(kugel,current_score)


        #3--Game-Over
        if pause_game == 3:

            #Text anzeigen
            screen.blit(game_over_text,game_over_text_rect)
            screen.blit(restart_text,restart_text_rect)
            screen.blit(return_text,return_text_rect)


        #4--Level-Complete-Bildschirm
        #Prüfen, ob keine Blöcke mehr vorhanden sind und Herzen übrig sind
        if len(blocks_group) == 0 and len(heart_rects) > 0:
            pause_game = 4

        #Win Win Fenster
        if pause_game == 4:
                
                #Text anzeigen
                screen.blit(won_text,won_text_rect)
                screen.blit(return_text,return_text_rect)    
                screen.blit(restart_text,restart_text_rect)

                #Score groß anzeigen lassen
                text_score2 = font_text.render(f"SCORE: {current_score} ", False, (255, 255, 255)).convert()
                text_score_rect2 = text_score2.get_rect(center = (400,380))
                screen.blit(text_score2,text_score_rect2)

                #Prüfe Score und Sterne anzeigen
                #3-Sterne
                if current_score >= 5610:
                    star_rects = star_rects[:3] #entnehme 3 aus der liste
                    counter_stars = 3           

                #2-Sterne
                if 4620 <= current_score < 5610:
                    star_rects = star_rects[:2] #entnehme 2 aus der liste
                    counter_stars = 2     

                #1-Stere
                if 3300 <= current_score < 4620:
                    star_rects = star_rects[:1] #entnehme 1 aus der liste
                    counter_stars = 1

                #0-Stere
                if current_score < 3300:
                    star_rects = star_rects[:0]
                    counter_stars = 0  
                    screen.blit(no_star_text,no_star_text_rect)

                #Speichern des höchsten erreichten Sternenwert
                if counter_stars > max_stars_level_1:
                    max_stars_level_1 = counter_stars

                #Sterne anzeigen lassen
                for rect in star_rects:
                    screen.blit(star_surf, rect)

    
        pygame.display.update()
        clock.tick(60)  


def level_2():

    global god_mode
    global max_stars_level_2 #Sterne speichern


    text_level = font_score.render(f"Level 2", False, (0,0,0)).convert() 
    text_level_rect = text_level.get_rect(midbottom = (400,590)) #Level-Text

    #Liste (Herzen)
    heart_rects = [
    heart_surf.get_rect(bottomright = (780,590)),  
    heart_surf.get_rect(bottomright = (745,590)),
    heart_surf.get_rect(bottomright = (710,590))  
    ]
    #Liste (Sternen)
    star_rects = [
    star_surf.get_rect(center = (300,255)),
    star_surf.get_rect(center = (400,255)),
    star_surf.get_rect(center = (500,255))
    ]

    pygame.display.set_caption("Level 2") #Titel

    #Groups erstellen
    #Group-Kugel-Brick
    kugel = Kugel.Kugel()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(kugel)
    brick = Brick.Brick()
    all_sprites.add(brick)

    #Group-Block
    blocks_group = pygame.sprite.Group()
    block = Block.Block(0,0)
    blocks = block.create_field_level_2()
    blocks_group.add(blocks)

    #Variablen
    pause_game = 1 #Switche zwischen den Bildschirmen, also Game-over und win...
    current_score = 0 #Score ist am anfang 0
    counter_stars = 0 #Wie viele Sterne wurden erreicht

    #Musik
    pygame.mixer.music.load("Music/Level_2.wav")
    pygame.mixer.music.play(-1) #endlos

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                exit()

            #Sobald SPACE gedrueckt wird
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_SPACE:
                    
                    #Herzen werden nur bei einem Game-over zurückgesetzt
                    if pause_game == 3 or pause_game == 4:
                        heart_rects = [
                            heart_surf.get_rect(bottomright = (780,590)),  
                            heart_surf.get_rect(bottomright = (745,590)),
                            heart_surf.get_rect(bottomright = (710,590))  
                           ]
                        
                        #Alles zurücksetzen
                        blocks_group.empty() #Feld leeren
                        blocks_group = block.create_field_level_2() #Neues Feld erstellen 
                        brick.reset_pos() #Reset Brick pos
                        current_score = 0 #Reset Score
                        kugel.rect.y = 400 #Reset Kugel-Position
                        kugel.rect.x = 400

                        #reset bahn
                        kugel.x_val = -5
                        kugel.y_val = -5
                        
                        pause_game = 2
      
                    if pause_game == 1:
                        pause_game = 2 #Startet das eigentliche game

            #Wenn Escape zurück zum Level-Menü
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        start_game()


        #Bildschirm
        screen.blit(background_surf, (0,0))
        screen.blit(text_level,text_level_rect)


        #Gruppen anzeigen lassen
        all_sprites.draw(screen) #Kugel und Brick anzeigen
        blocks_group.draw(screen) #Alle Blöcke anzeigen

        #Herzen
        for rect in heart_rects:
            screen.blit(heart_surf, rect)

        #SCORE aktuell anzeigen
        text_score = font_score.render(f"YOUR SCORE: {current_score} ", False, (0, 0, 0)).convert()
        text_score_rect = text_score.get_rect(bottomleft = (10,590))
        screen.blit(text_score,text_score_rect)

        #1--Start-Bildschirm
        if pause_game == 1:
            #Text: Das spiel mit der Space taste starten
            screen.blit(text_start,text_start_rect)
            screen.blit(return_text2,return_text_rect2)


        #2--Startet das eigentliche Game
        if pause_game == 2:

            #brick bewegen
            brick.move_brick() 

            #Kollision mit Kugel
            brick.collision(kugel)

            #Wenn Kugel Boden berührt und Herz verliert und Score verliert
            game_status = kugel.apply_gravity_del_heart_del_score(heart_rects,god_mode=god_mode)

            #Score wird abgezogen wenn -1 zurückgegeben
            if game_status == -1:
                current_score -= 1000 

            #Game-Over wenn 3 zurückgegeben
            if game_status == 3:
                pause_game = 3

            #Prüft welcher Block mit der Kugel kollidiert
            for block in blocks_group:
                block.collision_kugel(kugel)
                if isinstance(block, unbreakable_block):
                    continue
                current_score = block.return_score(kugel, current_score)


        #3--Game-Over
        if pause_game == 3:

            #Text anzeigen
            screen.blit(game_over_text,game_over_text_rect)
            screen.blit(restart_text,restart_text_rect)
            screen.blit(return_text,return_text_rect)


         #4--Level-Complete-Bildschirm
        if len(blocks_group) == 4 and len(heart_rects) > 0:
            pause_game = 4

        if pause_game == 4:
                
                #Text anzeigen
                screen.blit(won_text,won_text_rect)
                screen.blit(return_text,return_text_rect)    
                screen.blit(restart_text,restart_text_rect)

                #Score groß anzeigen lassen
                text_score2 = font_text.render(f"SCORE: {current_score} ", False, (255, 255, 255)).convert()
                text_score_rect2 = text_score2.get_rect(center = (400,380))
                screen.blit(text_score2,text_score_rect2)

                #Prüfe Score und Sterne anzeigen
                #3-Sterne
                if current_score >= 5210:
                    star_rects = star_rects[:3]
                    counter_stars = 3           

                #2-Sterne
                if 4220 <= current_score < 5210:
                    star_rects = star_rects[:2]
                    counter_stars = 2     

                #1-Stere
                if 2900 <= current_score < 4220:
                    star_rects = star_rects[:1]
                    counter_stars = 1

                #0-Stere
                if current_score < 2900:
                    star_rects = star_rects[:0]
                    counter_stars = 0  
                    screen.blit(no_star_text,no_star_text_rect)

                # Speichern des höchsten erreichten Sternenwerts
                if counter_stars > max_stars_level_2:
                    max_stars_level_2 = counter_stars 

                #Sterne anzeigen lassen
                for rect in star_rects:
                    screen.blit(star_surf, rect)
        

        pygame.display.update()
        clock.tick(60)  


def level_3():

    global god_mode 
    global max_stars_level_3 #Sterne speichern

    #Text
    text_level = font_score.render(f"Level 3", False, (0,0,0)).convert()
    text_level_rect = text_level.get_rect(midbottom = (400,590))


    #Liste (Herzen)
    heart_rects = [
    heart_surf.get_rect(bottomright = (780,590)),  
    heart_surf.get_rect(bottomright = (745,590)),
    heart_surf.get_rect(bottomright = (710,590))  
    ]

    #Liste (Sternen)
    star_rects = [
    star_surf.get_rect(center = (300,255)),
    star_surf.get_rect(center = (400,255)),
    star_surf.get_rect(center = (500,255))
    ]

    pygame.display.set_caption("Level 3") #Titel

    #Groups erstellen
    #Group-Kugel-Brick
    kugel = Kugel.Kugel()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(kugel)
    brick = Brick.Brick()
    all_sprites.add(brick)
    explosion_group = pygame.sprite.Group()

    #Group-Block
    blocks_group = pygame.sprite.Group()
    block = Block.Block(0,0)
    blocks = block.create_field_level_3()
    blocks_group.add(blocks)

    #Variablen
    pause_game = 1 #Switche zwischen den Bildschirmen, also Game-over und win...
    current_score = 0 #Score ist am anfang 0
    counter_stars = 0 #Wie viele Sterne wurden erreicht

    #Musik
    pygame.mixer.music.load("Music/Level_3.wav")
    pygame.mixer.music.play(-1) #endlos

    while True:

        dt = clock.tick(60)  
        dt = dt / 1000 #in Sekunden umzurechnen.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                exit()

            #Sobald SPACE gedrueckt wird
            if event.type == pygame.KEYDOWN:  

                if event.key == pygame.K_SPACE:
                    
                    #Herzen werden nur bei einem Game-over zurückgesetzt
                    if pause_game == 3 or pause_game == 4:
                        heart_rects = [
                            heart_surf.get_rect(bottomright = (780,590)),  
                            heart_surf.get_rect(bottomright = (745,590)),
                            heart_surf.get_rect(bottomright = (710,590))  
                           ]
                        
                        #Alles zurücksetzen
                        blocks_group.empty() #Feld leeren
                        blocks_group = block.create_field_level_3() #Neues Feld erstellen 
                        brick.reset_pos() #Reset Brick pos
                        current_score = 0  #Reset Score
                        kugel.rect.y = 400  #Reset Kugel-Position
                        kugel.rect.x = 400

                        #Bahn reseten
                        kugel.x_val = -5
                        kugel.y_val = -5
                        
                        #Startet wieder das game
                        pause_game = 2

                    #Start-Bildschirm
                    if pause_game == 1:
                        pause_game = 2 #Startet das eigentliche game

            #Wenn wir Escape drücken kommen wir ins Level-Menü und musik stoppt
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
     
                        pygame.mixer.music.stop()
                        start_game()


        #Bildschirm
        screen.blit(background_surf, (0,0))
        screen.blit(text_level,text_level_rect)

        #Gruppen anzeigen lassen
        all_sprites.draw(screen) #Kugel und Brick anzeigen
        blocks_group.draw(screen) #Alle Blöcke anzeigen

        #Explosionen anzeigen
        explosion_group.draw(screen)
        explosion_group.update(dt)


        #Herzen
        for rect in heart_rects:
            screen.blit(heart_surf, rect)

        #SCORE aktuell anzeigen
        text_score = font_score.render(f"YOUR SCORE: {current_score} ", False, (0, 0, 0)).convert()
        text_score_rect = text_score.get_rect(bottomleft = (10,590))
        screen.blit(text_score,text_score_rect)

        

        #1--Start-Bildschirm
        if pause_game == 1:
            #Text: Das spiel mit der Space taste starten
            screen.blit(text_start,text_start_rect)
            screen.blit(return_text2,return_text_rect2)


        #2--Startet das eigentliche Game
        if pause_game == 2:

            #brick bewegen
            brick.move_brick() 

            #Kollision mit Kugel
            brick.collision(kugel)

            #Wenn Kugel Boden berührt und Herz verliert und Score verliert
            game_status = kugel.apply_gravity_del_heart_del_score(heart_rects,god_mode=god_mode)

            #Score wird abgezogen wenn -1 zurückgegeben
            if game_status == -1:
                current_score -= 1000 

            #Game-Over wenn 3 zurückgegeben
            if game_status == 3:
                pause_game = 3

            #Prüft welcher Block mit der Kugel kollidiert
            for block in blocks_group:
                if isinstance(block, explosive_block):
                    current_score = block.collision_kugel(kugel, blocks_group, explosion_group, current_score)
                elif isinstance(block, prismen_block):
                    current_score = block.collision_kugel(kugel,current_score)  # Übergebe current_time nur bei prismen_block
                else:
                    block.collision_kugel(kugel)  # Andere Blöcke erhalten nur kugel

                if hasattr(block, 'return_score'):  # Prüfen, ob der Block die Methode hat
                    current_score = block.return_score(kugel, current_score)
                                

        #3--Game-Over
        if pause_game == 3:

            #Text anzeigen
            screen.blit(game_over_text,game_over_text_rect)
            screen.blit(restart_text,restart_text_rect)
            screen.blit(return_text,return_text_rect)

            #Score anzeigen und zurücksetzen
            #current_score = block.return_score(kugel,screen,current_score,font_score)

         #4--Level-Complete-Bildschirm
        if len(blocks_group) == 0 and len(heart_rects) > 0:
            pause_game = 4

        if pause_game == 4:
                
                #Text anzeigen
                screen.blit(won_text,won_text_rect)
                screen.blit(return_text,return_text_rect)    
                screen.blit(restart_text,restart_text_rect)

                #Score anzeigen
                text_score2 = font_text.render(f"SCORE: {current_score} ", False, (255, 255, 255)).convert()
                text_score_rect2 = text_score2.get_rect(center = (400,380))
                screen.blit(text_score2,text_score_rect2)

                #Prüfe Score und Sterne anzeigen
                #3-Sterne
                if current_score >= 5610:
                    star_rects = star_rects[:3]
                    counter_stars = 3           

                #2-Sterne
                if 4620 <= current_score < 5610:
                    star_rects = star_rects[:2]
                    counter_stars = 2     

                #1-Stere
                if 3300 <= current_score < 4620:
                    star_rects = star_rects[:1]
                    counter_stars = 1

                #0-Stere
                if current_score < 3300:
                    star_rects = star_rects[:0]
                    counter_stars = 0  
                    screen.blit(no_star_text,no_star_text_rect)

                # Speichern des höchsten erreichten Sternenwerts
                if counter_stars > max_stars_level_3:
                    max_stars_level_3 = counter_stars 

                #Sterne anzeigen lassen
                for rect in star_rects:
                    screen.blit(star_surf, rect)
        
        pygame.display.update()
     
    
def level_4():

    #Global zum speichern
    global god_mode
    global max_stars_level_4

    text_level = font_score.render(f"Level 4", False, (0,0,0)).convert()
    text_level_rect = text_level.get_rect(midbottom = (400,590)) 

    #Liste (Herzen)
    heart_rects = [
    heart_surf.get_rect(bottomright = (780,590)),  
    heart_surf.get_rect(bottomright = (745,590)),
    heart_surf.get_rect(bottomright = (710,590))  
    ]
    #Liste (Sternen)
    star_rects = [
    star_surf.get_rect(center = (300,255)),
    star_surf.get_rect(center = (400,255)),
    star_surf.get_rect(center = (500,255))
    ]

    #Titel
    pygame.display.set_caption("Level 4") 

    #Groups erstellen
    #Group-Kugel-Brick
    kugel = Kugel.Kugel()
    all_sprites = pygame.sprite.Group()
    #all_sprites.add(kugel)
    brick = Brick.Brick()
    all_sprites.add(brick)
    explosion_group = pygame.sprite.Group()

    #Group-Kugel
    kugeln = pygame.sprite.Group()
    kugeln.add(kugel)

    #Group-Block
    blocks_group = pygame.sprite.Group()
    block = Block.Block(0,0)
    blocks = block.create_field_level_4()
    blocks_group.add(blocks)

    #Variablen
    pause_game = 1 #Switche zwischen den Bildschirmen, also Game-over und win...
    current_score = 0 #Score ist am anfang 0
    counter_stars = 0 #Wie viele Sterne wurden erreicht

    #Musik
    pygame.mixer.music.load("Music/Level_4.wav")
    pygame.mixer.music.play(-1) #endlos

    while True:

        dt = clock.tick(60)  #nicht schneller als 60 mal pro sekunde
        dt = dt / 1000  #in sek

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                exit()

            #Sobald SPACE gedrueckt wird
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    
                    #Herzen werden nur bei einem Game-over zurückgesetzt
                    if pause_game == 3 or pause_game == 4:
                        heart_rects = [
                            heart_surf.get_rect(bottomright = (780,590)),  
                            heart_surf.get_rect(bottomright = (745,590)),
                            heart_surf.get_rect(bottomright = (710,590))  
                           ]
                        
                        #Alles zurücksetzen
                        blocks_group.empty() #Feld leeren
                        blocks_group = block.create_field_level_4() #Neues Feld erstellen 
                        brick.reset_pos() # Reset Brick pos
                        current_score = 0  # Reset Score
                        kugel.rect.y = 400  # Reset Kugel-Position
                        kugel.rect.x = 400

                        #Bahn reset
                        kugel.x_val = -5
                        kugel.y_val = -5
                        
                        pause_game = 2
      
                    if pause_game == 1:
                        pause_game = 2 #Startet das eigentliche game

            #Wenn wir escape drücken, gehe ein fenster zurück 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        start_game()
                        


        #Bildschirm
        screen.blit(background_surf, (0,0))
        screen.blit(text_level,text_level_rect)

        #Gruppen anzeigen lassen
        all_sprites.draw(screen) #Kugel und Brick anzeigen
        blocks_group.draw(screen) #Alle Blöcke anzeigen
        kugeln.draw(screen)

        #explosion anzeigen
        explosion_group.draw(screen)
        explosion_group.update(dt)


        #Herzen anzeigen und durchgehen
        for rect in heart_rects:
            screen.blit(heart_surf, rect)

        #SCORE aktuell anzeigen lassen
        text_score = font_score.render(f"YOUR SCORE: {current_score} ", False, (0, 0, 0)).convert()
        text_score_rect = text_score.get_rect(bottomleft = (10,590))
        screen.blit(text_score,text_score_rect)

        

        #1--Start-Bildschirm
        if pause_game == 1:
            #Text: Das spiel mit der Space taste starten
            screen.blit(text_start,text_start_rect)
            screen.blit(return_text2,return_text_rect2)


        #2--Startet das eigentliche Game
        if pause_game == 2:

            #brick bewegen
            brick.move_brick() 

            #Kollision mit Kugel
            for kugel in kugeln: #Alle Kugeln prüfen
                brick.collision(kugel)

                #Wenn Kugel Boden berührt und Herz verliert und Score verliert
                game_status = kugel.apply_gravity_del_heart_del_score(heart_rects,len(kugeln),god_mode=god_mode)

                #Score wird abgezogen wenn -1 zurückgegeben
                if game_status == -1:
                    current_score -= 1000 

                #Game-Over wenn 3 zurückgegeben
                if game_status == 3:
                    pause_game = 3


            #Prüft welcher Block mit der Kugel kollidiert
            for block in blocks_group:
                for kugel in kugeln:
                    if isinstance(block, powerUp_block.PowerUpBlock):
                        block.collision_kugel(kugel, brick, kugeln,current_score)
                    elif isinstance(block, explosive_block):
                        current_score = block.collision_kugel(kugel, blocks_group, explosion_group, current_score)
                    elif isinstance(block, prismen_block):
                        current_score = block.collision_kugel(kugel, current_score)
                    else:
                        block.collision_kugel(kugel)

                    if hasattr(block, 'return_score'):  # Prüfen, ob der Block die Methode hat
                        current_score = block.return_score(kugel, current_score)
                                

        #3--Game-Over
        if pause_game == 3:

            #Text anzeigen
            screen.blit(game_over_text,game_over_text_rect)
            screen.blit(restart_text,restart_text_rect)
            screen.blit(return_text,return_text_rect)


         #4--Level-Complete-Bildschirm
        if len(blocks_group) == 0 and len(heart_rects) > 0:
            pause_game = 4

        if pause_game == 4:
                
                #Text anzeigen
                screen.blit(won_text,won_text_rect)
                screen.blit(return_text,return_text_rect)    
                screen.blit(restart_text,restart_text_rect)

                #Score groß anzeigen
                text_score2 = font_text.render(f"SCORE: {current_score} ", False, (255, 255, 255)).convert()
                text_score_rect2 = text_score2.get_rect(center = (400,380))
                screen.blit(text_score2,text_score_rect2)

                #Prüfe Score und Sterne anzeigen
                #3-Sterne
                if current_score >=  6710:
                    star_rects = star_rects[:3]
                    counter_stars = 3           

                #2-Sterne
                if 5720 <= current_score < 6710:
                    star_rects = star_rects[:2]
                    counter_stars = 2     

                #1-Stere
                if 4400 <= current_score < 5720:
                    star_rects = star_rects[:1]
                    counter_stars = 1

                #0-Stere
                if current_score < 4400:
                    star_rects = star_rects[:0]
                    counter_stars = 0  
                    screen.blit(no_star_text,no_star_text_rect)

                # Speichern des höchsten erreichten Sternenwerts
                if counter_stars > max_stars_level_4:
                    max_stars_level_4 = counter_stars 

                #Sterne anzeigen lassen
                for rect in star_rects:
                    screen.blit(star_surf, rect)
        
        pygame.display.update()
        
#Score anzeigen lassen als Sekunden
#Quelle: https://www.youtube.com/watch?v=AY9MnQ4x3zk
def display_Score(start_time):
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = font_score.render(f"Score: {current_time}", False, (255, 255, 255 ))
    score__rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score__rect)
    return current_time


def survival_mode():

    global god_mode #godmode

    text_level = font_score.render(f"survival_mode", False, (0,0,0)).convert()
    text_level_rect = text_level.get_rect(midbottom = (400,590))

    #Liste (Herzen)
    heart_rects = [
    heart_surf.get_rect(bottomright = (780,590)),  
    heart_surf.get_rect(bottomright = (745,590)),
    heart_surf.get_rect(bottomright = (710,590))  
    ]

    #Titel
    pygame.display.set_caption("Survival_mode")  

    #Groups erstellen
    #Group-Kugel-Brick
    kugel = Kugel.Kugel()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(kugel)
    brick = Brick.Brick()
    all_sprites.add(brick)
  
    #Variablen
    pause_game = 1 #Switche zwischen den Bildschirmen, also Game-over und win...
    start_time = 0
    best_score = 0

    last_speed_increase_time = 0  #steige geschwindigkeit

    #Musik
    pygame.mixer.music.load("Music/Level_4.wav")
    pygame.mixer.music.play(-1) #endlos

    while True:

        dt = clock.tick(60) # nicht schneller als 60 mal pro sekunde,
        dt = dt / 1000 #in sek

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                exit()

            #Sobald SPACE gedrueckt wird
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_SPACE:
                    
                    #Herzen werden nur bei einem Game-over zurückgesetzt
                    if pause_game == 3:
                        heart_rects = [
                            heart_surf.get_rect(bottomright = (780,590)),  
                            heart_surf.get_rect(bottomright = (745,590)),
                            heart_surf.get_rect(bottomright = (710,590))  
                           ]
                        
                        #Alles zurücksetzen
                        brick.reset_pos() # Reset Brick pos
                        kugel.rect.y = 400  # Reset Kugel-Position
                        kugel.rect.x = 400

                        #Bahn reseten
                        kugel.x_val = -5
                        kugel.y_val = -5

                        #Score reseten
                        start_time = 0
                        start_time = int(pygame.time.get_ticks() / 1000)
                        
                        #Startet das eigentlich game
                        pause_game = 2
      
                    if pause_game == 1:
                        pause_game = 2 #Startet das eigentliche game

            #Wenn escape gedrückt wird, gehe ein fenster zurück
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        main_menu()


        #Bildschirm
        screen.blit(background_surf, (0,0))
        screen.blit(text_level,text_level_rect)

        #Gruppen anzeigen lassen
        all_sprites.draw(screen) #Kugel und Brick anzeigen
       
        #Herzen
        for rect in heart_rects:
            screen.blit(heart_surf, rect)

        #1--Start-Bildschirm
        if pause_game == 1:
            #Text: Das spiel mit der Space taste starten
            screen.blit(text_start,text_start_rect)
            screen.blit(return_text2,return_text_rect2)


        #2--Startet das eigentliche Game
        if pause_game == 2:

             #Start time initialisieren wenn das Spiel beginnt
            if start_time == 0:
                start_time = int(pygame.time.get_ticks() / 1000)

            #brick bewegen
            brick.move_brick() 

            #Kollision mit Kugel
            brick.collision_without_maxspeed(kugel)

            #Wenn Kugel Boden berührt und Herz verliert und Score verliert
            game_status = kugel.apply_gravity_del_heart_del_score(heart_rects,god_mode=god_mode)

    
            #Game-Over wenn 3 zurückgegeben
            if game_status == 3:
                pause_game = 3

            #Mehr Geschwindigkeit alle 1 Sekunde
            current_time = int(pygame.time.get_ticks() / 1000)

            #Geschwindigkeit wieder immer wieder erhöht wenn Zeit wächst
            if current_time > last_speed_increase_time:            

                #Achte auf Vorzeichen
                if kugel.x_val > 0:
                        kugel.x_val += 0.3
                else:
                        kugel.x_val -= 0.3

                if kugel.y_val > 0:         
                        kugel.y_val += 0.3
                else:
                        kugel.y_val -= 0.3

                last_speed_increase_time = current_time #aktualisieren

            #SCORE
            score = display_Score(start_time)

            #Besten Score aktualisieren
            if score > best_score:
                best_score = score


        #3--Game-Over
        if pause_game == 3:

            #Text anzeigen
            screen.blit(restart_text,restart_text_rect)
            screen.blit(return_text,return_text_rect)

            #Besten Score anzeigen lassen und Texte
            score_message = font_score2.render(f"your best score: {best_score}", False, (255,255,255))
            score_message_rect = score_message.get_rect(center=(400, 250))
            screen.blit(score_message, score_message_rect)

        
        pygame.display.update()
        

def settings():

    global volume
    global god_mode
    
    pygame.mixer.music.set_volume(volume) #Lautsärke anpassen

    #Texte 
    volume_surf = font_score.render("VOLUME:",False,(255, 255, 255)).convert()
    volume_surf_rect = volume_surf.get_rect(topleft = (200,200))

    left_arrow_surf = font_score.render("<",False,(255, 255, 255)).convert()
    left_arrow_surf_rect = left_arrow_surf.get_rect(topleft = (310,200))

    right_arrow_surf = font_score.render(">",False,(255, 255, 255)).convert()
    right_arrow_surf_rect = right_arrow_surf.get_rect(topleft = (430,200))

    volume_value_surf = font_score.render(f"{int(volume * 100)}%", False, (255, 255, 255)).convert()
    volume_value_rect = volume_value_surf.get_rect(topleft=(350, 200))

    god_mode_surf = font_score.render("God-Mode:",False,(255, 255, 255)).convert()
    god_mode_surf_rect = god_mode_surf.get_rect(topleft = (200,250))

    on_surf = font_score.render("ON",False,(255, 255, 255)).convert()
    on_surf_rect = on_surf.get_rect(topleft = (350,250))

    off_surf = font_score.render("OFF",False,(255, 255, 255)).convert()
    off_surf_rect = off_surf.get_rect(topleft = (350,250))

    pygame.display.set_caption("Settings") 
    
    #Musik
    start_music()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                exit()

            #Godmode per Mausklick ändern
            if event.type == pygame.MOUSEBUTTONDOWN:
                if god_mode_surf_rect.collidepoint(event.pos):
                    # Umschalten zwischen ON und OFF
                    if god_mode == 0:
                        god_mode = 1
                    else:
                        god_mode = 0


                #Lautstärke verringern
                if left_arrow_surf_rect.collidepoint(event.pos) and volume > 0.0:
                    volume = max(0.0, volume - 0.1)  #Lautstärke in Schritten von 0.1 verringern und neheme das größte
                    pygame.mixer.music.set_volume(volume) #aktualisiere

                #Lautstärke erhöhen
                if right_arrow_surf_rect.collidepoint(event.pos) and volume < 1.0:
                    volume = min(1.0, volume + 0.1)  #Lautstärke in Schritten von 0.1 erhöhen und nehme das kleinste
                    pygame.mixer.music.set_volume(volume) #aktualisiere

            #Gehe ein Fenster zurück wenn Escape
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        #Volume anzeigen lassen
        volume_value_surf = font_score.render(f"{int(volume * 100)}%", False, (255, 255, 255)).convert()

        #Texte anzeigen
        screen.blit(background_surf, (0, 0))
        screen.blit(volume_surf, volume_surf_rect)
        screen.blit(god_mode_surf, god_mode_surf_rect)

        #Pfeile
        screen.blit(left_arrow_surf,left_arrow_surf_rect)
        screen.blit(right_arrow_surf,right_arrow_surf_rect)
        screen.blit(volume_value_surf, volume_value_rect)

        #Gofmode anzeigen
        if god_mode == 0:
            screen.blit(off_surf, off_surf_rect)
        else:
            screen.blit(on_surf, on_surf_rect)


        pygame.display.update()
        clock.tick(60)


def tutorial():

    #Bild
    tutorial_pic_surf = pygame.image.load('Bilder/tutorial_pic.png').convert() 
    tutorial_pic_surf = pygame.transform.scale( tutorial_pic_surf, (450,350))
    tutorial_pic_surf_rect = tutorial_pic_surf.get_rect(center = (400,150))

    #Texte
    text_surf = font_button2.render("Das Ziel ist es, mit einem Schläger eine Kugel abzuwehren",False,(255, 255, 255)).convert()
    text_surf_rect = text_surf.get_rect(center = (400,370))

    text_surf2 = font_button2.render("und damit alle Blöcke zu zerstören. Wenn die Kugel den Boden",False,(255, 255, 255)).convert()
    text_surf2_rect = text_surf2.get_rect(center = (400,395))

    text_surf3 = font_button2.render("berührt, verlierst du ein Herz. Das Spiel ist vorbei, wenn alle",False,(255, 255, 255)).convert()
    text_surf3_rect = text_surf3.get_rect(center = (400,420))
    
    text_surf4 = font_button2.render("Herzen verloren sind.",False,(255, 255, 255)).convert()
    text_surf4_rect = text_surf4.get_rect(center = (400,445))

    left_arrow_surf = font_score.render("<",False,(255, 255, 255)).convert()
    left_arrow_surf_rect = left_arrow_surf.get_rect(topleft = (300,500))

    right_arrow_surf = font_score.render(">",False,(255, 255, 255)).convert()
    right_arrow_surf_rect = right_arrow_surf.get_rect(topleft = (500,500))

    #Blöcke
    block2_surf = pygame.image.load("Bilder/Normal_Block_2Hit.png").convert_alpha()
    block2_surf = pygame.transform.scale(block2_surf, (200, 60))
    block2_surf_rect = block2_surf.get_rect(center = (400,100))

    unbreakable_b_surf = pygame.image.load("Bilder/Unzerbrechlicher_Block.png").convert_alpha()
    unbreakable_b_surf = pygame.transform.scale(unbreakable_b_surf, (200, 60))
    unbreakable_b_surf_rect = unbreakable_b_surf.get_rect(center = (400,100))

    explosive_surf = pygame.image.load("Bilder/Explosiver_Block.png").convert_alpha()
    explosive_surf = pygame.transform.scale(explosive_surf, (200, 60))
    explosive_surf_rect = explosive_surf.get_rect(center = (400,100))

    prismen_surf = pygame.image.load("Bilder/Prismen_Block.png").convert_alpha()
    prismen_surf = pygame.transform.scale(prismen_surf, (200, 60))
    prismen_surf_rect = prismen_surf.get_rect(center = (400,100))

    powerup_surf = pygame.image.load("Bilder/PowerUpBlock.png").convert_alpha()
    powerup_surf = pygame.transform.scale(powerup_surf, (200, 60))
    powerup_surf_rect = powerup_surf.get_rect(center = (400,100))

    #Texte
    text_block_surf = font_button2.render("Der Block_2 ist ein besonderer Block in deinem Spiel. Im Gegensatz",False,(255, 255, 255)).convert()
    text_block_surf_rect = text_block_surf.get_rect(center = (400,300))

    text_block_surf2 = font_button2.render("zu normalen Blöcken, die nur einen Treffer brauchen, um zerstört",False,(255, 255, 255)).convert()
    text_block_surf2_rect = text_block_surf2.get_rect(center = (400,325))

    text_block_surf3 = font_button2.render("zu werden, muss dieser Block zweimal getroffen werden.",False,(255, 255, 255)).convert()
    text_block_surf3_rect = text_block_surf3.get_rect(center = (400,350))

    text_unbreakable_surf = font_button2.render("Der Unzerbrechliche Block ist ein spezieller Block in deinem Spiel,",False,(255, 255, 255)).convert()
    text_unbreakable_surf_rect = text_unbreakable_surf.get_rect(center = (400,300))

    text_unbreakable_surf2 = font_button2.render("der nicht zerstört werden kann.",False,(255, 255, 255)).convert()
    text_unbreakable_surf2_rect = text_unbreakable_surf2.get_rect(center = (400,325))

    text_explosive_surf = font_button2.render("Der Explosive Block ist ein spezieller Block, der beim",False,(255, 255, 255)).convert()
    text_explosive_surf_rect = text_explosive_surf.get_rect(center = (400,300))

    text_explosive2_surf = font_button2.render("Zerstören explodiert und dabei alle benachbarten Blöcke zerstört.",False,(255, 255, 255)).convert()
    text_explosive2_surf_rect = text_explosive2_surf.get_rect(center = (400,325))


    text_prismen_surf = font_button2.render("Der Prismen Block ist ein besonderer Block, der den ",False,(255, 255, 255)).convert()
    text_prismen_surf_rect = text_prismen_surf.get_rect(center = (400,300))

    text_prismen2_surf = font_button2.render("Spielverlauf beeinflusst, indem er die",False,(255, 255, 255)).convert()
    text_prismen2_surf_rect = text_prismen2_surf.get_rect(center = (400,325))

    text_prismen3_surf = font_button2.render("Geschwindigkeit der Kugel für kurze Zeit erhöht.",False,(255, 255, 255)).convert()
    text_prismen3_surf_rect = text_prismen3_surf.get_rect(center = (400,350))

    text_powerup_surf = font_button2.render("Der PowerUp Block lässt beim Zerstören eine zweite Kugel",False,(255, 255, 255)).convert()
    text_powerup_surf_rect = text_powerup_surf.get_rect(center = (400,300))

    text_powerup2_surf = font_button2.render("erscheinen und verlängert deinen Schläger, wodurch",False,(255, 255, 255)).convert()
    text_powerup2_surf_rect = text_powerup2_surf.get_rect(center = (400,325))

    text_powerup3_surf = font_button2.render("du mehr Blöcke schneller zerstören kannst.",False,(255, 255, 255)).convert()
    text_powerup3_surf_rect = text_powerup3_surf.get_rect(center = (400,350))

    pygame.display.set_caption("Tutorial") #Titel

    start_music()

    seite = 1 #beginne mit seite 1

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                exit()

            #Wenn Escape, gehe ein fenster zurück
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

            #Wechsel Seiten
            if event.type == pygame.MOUSEBUTTONDOWN:
                if right_arrow_surf_rect.collidepoint(event.pos):
                        if seite >= 1 and seite <= 5:
                            seite += 1

                if left_arrow_surf_rect.collidepoint(event.pos):
                        if seite <= 6 and seite >= 2:
                            seite -= 1


        #Schwarzen hintergrund
        screen.fill((0,0,0))

        #Pfeile
        screen.blit(left_arrow_surf,left_arrow_surf_rect)
        screen.blit(right_arrow_surf,right_arrow_surf_rect)

        #Aktuelle Seite anzeigen
        seite_surf = font_score.render(f"{seite}",False,(255, 255, 255)).convert()
        seite_surf_rect = seite_surf.get_rect(center = (408,512))
        screen.blit(seite_surf,seite_surf_rect)

        #Inhalte der Seiten anzeigen lassen
        if seite == 1:
            screen.blit(tutorial_pic_surf,tutorial_pic_surf_rect)
            screen.blit(text_surf,text_surf_rect)
            screen.blit(text_surf2,text_surf2_rect)
            screen.blit(text_surf3,text_surf3_rect)
            screen.blit(text_surf4,text_surf4_rect)

        if seite == 2:
            screen.blit(block2_surf,block2_surf_rect)
            screen.blit(text_block_surf,text_block_surf_rect)
            screen.blit(text_block_surf2,text_block_surf2_rect)
            screen.blit(text_block_surf3,text_block_surf3_rect)

        if seite == 3:
            screen.blit(unbreakable_b_surf,unbreakable_b_surf_rect)
            screen.blit(text_unbreakable_surf,text_unbreakable_surf_rect)
            screen.blit(text_unbreakable_surf2,text_unbreakable_surf2_rect)

        if seite == 4:
            screen.blit(explosive_surf,explosive_surf_rect)
            screen.blit(text_explosive_surf,text_explosive_surf_rect)
            screen.blit(text_explosive2_surf,text_explosive2_surf_rect)

        if seite == 5:
            screen.blit(prismen_surf,prismen_surf_rect)
            screen.blit(text_prismen_surf,text_prismen_surf_rect)
            screen.blit(text_prismen2_surf,text_prismen2_surf_rect)
            screen.blit(text_prismen3_surf,text_prismen3_surf_rect)

        if seite == 6:
            screen.blit(powerup_surf,powerup_surf_rect)
            screen.blit(text_powerup_surf,text_powerup_surf_rect)
            screen.blit(text_powerup2_surf,text_powerup2_surf_rect)
            screen.blit(text_powerup3_surf,text_powerup3_surf_rect)

        pygame.display.update()
        clock.tick(60)

main_menu()







