from operator import truediv
import pygame
import sys
import time


pygame.init()
WIDTH = 1920
HEIGHT = 1010
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("The Cube Games")

Blue = (0, 120, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
White = (255, 255, 255)
Yellow = (255, 210, 150)
Dark_Blue = (50, 55, 180)

width = 50
height = 50
width1 = 20
height1 = 20

#User_Ship = pygame.image.load('1Square.png')
#User_Ship1 = pygame.transform.scale(User_Ship, (width, height))           #(pygame.transform.rotate --- ,90)

x = 930
y = 480
vel = 9

x1 = 200
y1 = 200
vel1 = 12

Display_RW = []
pygame.display.update

Big_Cube = pygame.draw.rect(WINDOW, (20, 70, 190), (x, y, 50, 50))
Small_Cube = pygame.draw.rect(WINDOW, (255, 0, 0), (x1, y1, 20, 20))
length = 50

SPEED  = 7

all_bullets  = []

#_______________________________________________________________________________

def main():

    #UserRect = pygame.Rect(930, 480, 200, 50)
    clock = pygame.time.Clock()

    RelDel = 0

    RelDel1 = RelDel//2

    RelDelCheck = False

    AnotherFlag = True

    LoopCheck = 0

    BPS = 30

    BPSCheck = True

    run = True

    RWins = 0

    BWins = 0

    x = 930
    y = 480
    
    SPEED  = 7

    vel = 9

    vel1 = 12

    x1 = 200

    y1 = 200

    show_displayR = False
    show_displayB = False
    SpawnBullet  = True

    InFont = pygame.font.Font("dpcomic.ttf", 200)
    UseInFont = InFont.render("The Cube Games", False, White)

    fontLN = pygame.font.Font(None, 134)
    textLN = fontLN.render("Loading..", False, White)
    textRectLN = textLN.get_rect()
    textRectLN.center = (10, 10)

    fontL2 = pygame.font.Font(None, 134)
    textL2 = fontL2.render("Loading..", False, White)
    textRectL2 = textL2.get_rect()
    textRectL2.center = (10, 10)

    fontL3 = pygame.font.Font(None, 134)
    textL3 = fontL3.render("Loading...", False, White)
    textRectL3 = textL3.get_rect()
    textRectL3.center = (10, 10)

    fontL1 = pygame.font.Font(None, 134)
    textL1 = fontL1.render("Loading.", False, White)
    textRectL1 = textL1.get_rect()
    textRectL1.center = (10, 10)


    WINDOW.fill(Blue)
    pygame.display.flip()
    pygame.display.update()
    time.sleep(0.5)

    WINDOW.blit(UseInFont, (290, 330))

    WINDOW.blit(textL1, (680, 700))
    pygame.display.flip()
    pygame.display.update()
    time.sleep(1.5)

    WINDOW.blit(textL2, (680, 700))
    pygame.display.flip()
    pygame.display.update()
    time.sleep(1.5)

    WINDOW.blit(textL3, (680, 700))
    pygame.display.flip()
    pygame.display.update()
    time.sleep(1.8)

    
    
    
    while run:
        clock.tick(60)

        
        for event in pygame.event.get():

            
            
            #S = True
            #if S == True:
                #menuscreen
                #time.sleep(7)
                #keys = pygame.key.get_pressed()

                #if keys[pygame.K_c]:
                    #S = False
            

            start_can = pygame.math.Vector2(x + 25, y + 25)
            end = start_can

            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()
        
        
            if keys[pygame.K_q]:
                run = False
                



            elif event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                end = start_can + (mouse - start_can).normalize() * length
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BPSCheck == True:
                    mouse = pygame.mouse.get_pos()
                    distance = mouse - start_can
                    position = pygame.math.Vector2(x + 25, y + 25) # duplicate # start position in start of canon
                #position = pygame.math.Vector2(end)   # duplicate # start position in end of canon
                    speed = distance.normalize() * SPEED
                    all_bullets.append([position, speed])
                    BPS -= 1



        
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_LEFT] and x>0:
            x = x - vel

        if keys[pygame.K_RIGHT] and x<1885-width1:
            x += vel
            
        if keys[pygame.K_UP] and y>0:
            y -= vel
          
        if keys[pygame.K_DOWN] and y<980-height1:
            y += vel

     #_________________________________________________
        
        if keys[pygame.K_a] and x1>5:
            x1 -= vel1
            
        if keys[pygame.K_d] and x1<1920-width1:
            x1 += vel1
        
        if keys[pygame.K_w] and y1>0:
            y1 -= vel1
            
        if keys[pygame.K_s] and y1<1000-height1:
            y1 += vel1
        
      #  _______________________________________________

        fontRel = pygame.font.Font(None, 32)
        textRel = fontRel.render('' + str(RelDel1) + '%', False, White)
        textRectRel = textRel.get_rect()
        textRectRel.center = (0, 0)

        if BPS == 0:
                RelDel = 0
                RelDel1 = RelDel//2
                BPSCheck = False
                BPS = ('Hold ENTER on keypad to reload    ' + str(RelDel1) + '%')
                RelDelCheck = True

        keys = pygame.key.get_pressed()
        if RelDelCheck == True:
            if keys [pygame.K_KP_ENTER]:
                RelDel = RelDel + 1
                RelDel1 = RelDel//2
                BPS = ('Hold ENTER on keypad to reload    ' + str(RelDel1) + '%')
                AnotherFlag = True
            
        if AnotherFlag == True:
            if RelDel1  == 100:
                BPSCheck = True
                BPS = 30
                RelDelCheck = False
                AnotherFlag = False

        
            #bps_time = time.time()
            #time.sleep(3)
            #time_elapsed = time.time() - bps_time
            #print(time_elapsed)
            
                #GunReload1 = pygame.mixer.Sound('GunShotLight.mp3')
                #pygame.mixer.Sound.play(GunReload1)
            

            

        #if keys[pygame.K_KP_ENTER]:
            #pygame.draw.rect(WINDOW, (255, 200, 150), (Big_Cube.x - 100, Big_Cube.y - 100, 10, 10))
            #print('Yes')
            #pygame.display.update()
        
        

        
        font = pygame.font.Font(None, 32)
        text = font.render("Red Cube Speed: " + str(vel1) + " ", False, Red)
        textRect = text.get_rect()
        textRect.center = (10, 10)

        fontEx = pygame.font.Font(None, 40)
        textEx = fontEx.render("Press Q to Exit", False, White)
        textRectEx = textEx.get_rect()
        textRectEx.center = (10, 10)

        #fontRel = pygame.font.Font(None, 32)
        #textRel = fontRel.render('' + str(RelDel1) + '%', False, White)
        #textRectRel = textRel.get_rect()
        #textRectRel.center = (0, 0)

        font1 = pygame.font.Font(None, 32)
        text1 = font1.render('''Press K on the keyboard to continue    Press Q on the keyboard to quit''', False, White)
        textRect1 = text1.get_rect()
        textRect1.center = (10, 10)

        font2 = pygame.font.Font(None, 32)
        text2 = font2.render('''RED CUBE WON!!!''', False, Red)
        textRect2 = text2.get_rect()
        textRect2.center = (10, 10)

        font3 = pygame.font.Font(None, 32)
        text3 = font3.render('''BLUE CUBE WON!!!''', False, Dark_Blue)
        textRect3 = text3.get_rect()
        textRect3.center = (10, 10)

        fontR = pygame.font.Font(None, 32)
        textR = fontR.render("Blue Wins: " + str(BWins), False, White)
        textRectR = textR.get_rect()
        textRectR.center = (10, 10)

        fontW = pygame.font.Font(None, 32)
        textW = fontW.render("Red Wins: " + str(RWins), False, White)
        textRectW = textW.get_rect()
        textRectW.center = (10, 10)

        fontMenu = pygame.font.Font(None, 25)
        textMenu = fontMenu.render("Hold M for Instructions", False, Yellow)
        textRectMenu = textMenu.get_rect()
        textRectMenu.center = (10, 10)

        fontBPS = pygame.font.Font(None, 32)
        textBPS = fontBPS.render("Ammo: " + str(BPS) + " ", False, Dark_Blue)
        textRectBPS = textBPS.get_rect()
        textRectBPS.center = (10, 10)


        
        WINDOW.fill(Blue)
        
        WINDOW.blit(textEx, (1700, 1040))
        #WINDOW.blit(backround, (0, 0)

        WINDOW.blit(text, (10, 10))

        WINDOW.blit(textBPS, (1400, 10))

        WINDOW.blit(textR, (700, 10))
        WINDOW.blit(textW, (1000, 10))
        WINDOW.blit(textMenu, (850, 1050))
        
        Big_Cube = pygame.draw.rect(WINDOW, (20, 70, 190), (x, y, 50, 50))
        Small_Cube = pygame.draw.rect(WINDOW, (255, 0, 0), (x1, y1, 20, 20))


        
        Big_Cube = pygame.draw.rect(WINDOW, (20, 70, 190), (x, y, 50, 50))
        Small_Cube = pygame.draw.rect(WINDOW, (255, 0, 0), (x1, y1, 20, 20))

        #WINDOW.blit(textRel, (x, y))
        
        
        
        #x11 = x1.range(20)
        #Big_Cords = Big_Cube(x11, y11)
        #if Big_Cords


        for position, speed in all_bullets:
            position += speed

        
        if SpawnBullet == True:
            pygame.draw.line(WINDOW, (Red), start_can, end)

            for position, speed in all_bullets:
                
                pos_x = int(position.x)
                pos_y = int(position.y)
                Line_bullet = pygame.draw.rect(WINDOW, (255, 255, 255), (pos_x, pos_y, 5, 5))
                


                collision_tolerance = 20
                if Small_Cube.colliderect(Line_bullet):
                    if abs(Line_bullet.left - Small_Cube.right) < collision_tolerance:
                        vel1 = vel1 - 0.5
                        if vel1 == 8:
                            time.sleep(1)
                            SpawnBullet = False
                            x1 = 200
                            y1 = 200
                            x = 930
                            y = 480
                            vel1 = 0
                            vel = 0
                            SPEED = 0
                            show_displayB = True
                            BWins += 1
                            RelDelCheck = False


        if show_displayB == True:
                
            WINDOW.blit(text1, (560, 350))
            WINDOW.blit(text3, (850, 200))
        
            if keys[pygame.K_k]:
                show_displayB = False
                vel1 = 12
                vel = 9
                SPEED  = 7
                SpawnBullet = True
                BPS = 30
                
                BPSCheck = True
                        
            if keys[pygame.K_q]:
                run = False

        collision_tolerance1 = 100
        if Small_Cube.colliderect(Big_Cube):
            if abs(Big_Cube.top - Small_Cube.bottom) < collision_tolerance1:
                time.sleep(1)
                x1 = 200
                y1 = 200
                x = 930
                y = 480
                vel1 = 0
                vel = 0
                SPEED  = 0
                #Display_RW.append(WINDOW.blit(text1, (500, 500)))
                show_displayR = True
                SpawnBullet = False
                RWins += 1
                RelDelCheck = False


        if show_displayR == True:
            
            WINDOW.blit(text1, (560, 350))
            WINDOW.blit(text2, (850, 200))
            if keys[pygame.K_k]:
                show_displayR = False
                vel1 = 12
                vel = 9
                SPEED  = 7
                SpawnBullet = True
                BPS = 30
                
                BPSCheck = True
                

            if keys[pygame.K_q]:
                run = False

        
        if keys[pygame.K_m]:
            Start_Menu = True
            if Start_Menu == True:
                Inst = pygame.image.load('Instructions.png')
                Inst1 = pygame.transform.scale(Inst, (1000, 700))
                WINDOW.blit(Inst1, (450, 200))

        
        pygame.display.flip()

        pygame.display.update()

                #vel=0
                #GO_TEXT = pygame.image.load('GameOverText.png')
                #GO_TEXT1 = pygame.transform.scale(GO_TEXT, (200, 200))
                #WINDOW.blit(GO_TEXT1, (0, 0))
        
    pygame.quit()


if __name__ == "__main__":
    main()