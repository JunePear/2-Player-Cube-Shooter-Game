import pygame
import sys
import time

pygame.init()
WIDTH = 1920
HEIGHT = 1010
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
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

x = 930
y = 480
vel = 9

x1 = 200
y1 = 200
vel1 = 12

Display_RW = []

# Fixed structural canvas definitions
length = 50
SPEED = 7
all_bullets = []

#_______________________________________________________________________________

def main():
    global all_bullets, SPEED, x, y, x1, y1, vel, vel1
    clock = pygame.time.Clock()

    RelDel = 0
    RelDel1 = RelDel // 2
    RelDelCheck = False
    AnotherFlag = True
    BPS = 30
    BPSCheck = True
    run = True
    RWins = 0
    BWins = 0

    x = 930
    y = 480
    SPEED = 7
    vel = 9
    vel1 = 12
    x1 = 200
    y1 = 200

    show_displayR = False
    show_displayB = False
    SpawnBullet = True

    # Modified font definitions to fallback to system standard if file missing
    try:
        InFont = pygame.font.Font("dpcomic.ttf", 200)
    except:
        InFont = pygame.font.SysFont("arial", 150)
        
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
    time.sleep(0.5)

    WINDOW.blit(UseInFont, (290, 330))
    WINDOW.blit(textL1, (680, 700))
    pygame.display.flip()
    time.sleep(0.5)  # Decreased slightly for testing comfort

    WINDOW.blit(textL2, (680, 700))
    pygame.display.flip()
    time.sleep(0.5)

    WINDOW.blit(textL3, (680, 700))
    pygame.display.flip()
    time.sleep(0.5)

    while run:
        clock.tick(60)

        start_can = pygame.math.Vector2(x + 25, y + 25)
        end = start_can

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                distance = mouse - start_can
                if distance.length() > 0:
                    end = start_can + distance.normalize() * length
                else:
                    end = start_can
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BPSCheck == True:
                    mouse = pygame.mouse.get_pos()
                    distance = mouse - start_can
                    if distance.length() > 0:
                        position = pygame.math.Vector2(x + 25, y + 25)
                        speed = distance.normalize() * SPEED
                        all_bullets.append([position, speed])
                        BPS -= 1

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and x > 0:
            x = x - vel
        if keys[pygame.K_RIGHT] and x < 1885 - width1:
            x += vel
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < 980 - height1:
            y += vel

        if keys[pygame.K_a] and x1 > 5:
            x1 -= vel1
        if keys[pygame.K_d] and x1 < 1920 - width1:
            x1 += vel1
        if keys[pygame.K_w] and y1 > 0:
            y1 -= vel1
        if keys[pygame.K_s] and y1 < 1000 - height1:
            y1 += vel1

        if BPS == 0:
            RelDel = 0
            RelDel1 = RelDel // 2
            BPSCheck = False
            BPS = 0
            RelDelCheck = True

        if RelDelCheck == True:
            if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:  # Added fallback system enter key
                RelDel = RelDel + 1
                RelDel1 = RelDel // 2
                AnotherFlag = True
            
        if AnotherFlag == True:
            if RelDel1 == 100:
                BPSCheck = True
                BPS = 30
                RelDelCheck = False
                AnotherFlag = False

        font = pygame.font.Font(None, 32)
        text = font.render("Red Cube Speed: " + str(vel1) + " ", False, Red)

        fontEx = pygame.font.Font(None, 40)
        textEx = fontEx.render("Press Q to Exit", False, White)

        font1 = pygame.font.Font(None, 32)
        text1 = font1.render("Press K on the keyboard to continue    Press Q on the keyboard to quit", False, White)

        font2 = pygame.font.Font(None, 32)
        text2 = font2.render("RED CUBE WON!!!", False, Red)

        font3 = pygame.font.Font(None, 32)
        text3 = font3.render("BLUE CUBE WON!!!", False, Dark_Blue)

        fontR = pygame.font.Font(None, 32)
        textR = fontR.render("Blue Wins: " + str(BWins), False, White)

        fontW = pygame.font.Font(None, 32)
        textW = fontW.render("Red Wins: " + str(RWins), False, White)

        fontMenu = pygame.font.Font(None, 25)
        textMenu = fontMenu.render("Hold M for Instructions", False, Yellow)

        fontBPS = pygame.font.Font(None, 32)
        # Fixed potential string conversion error by handling the visual label context safely
        ammo_text = f"Reloading: {RelDel1}%" if RelDelCheck else f"Ammo: {BPS}"
        textBPS = fontBPS.render(ammo_text, False, Dark_Blue)

        WINDOW.fill(Blue)
        WINDOW.blit(textEx, (1700, 950))  # Moved within window parameters from 1040
        WINDOW.blit(text, (10, 10))
        WINDOW.blit(textBPS, (1400, 10))
        WINDOW.blit(textR, (700, 10))
        WINDOW.blit(textW, (1000, 10))
        WINDOW.blit(textMenu, (850, 950))  # Moved within window bounds
        
        Big_Cube = pygame.draw.rect(WINDOW, (20, 70, 190), (x, y, 50, 50))
        Small_Cube = pygame.draw.rect(WINDOW, (255, 0, 0), (x1, y1, 20, 20))

        for position, speed in all_bullets:
            position.x += speed.x
            position.y += speed.y

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
                        if vel1 <= 8:
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
                SPEED = 7
                SpawnBullet = True
                BPS = 30
                BPSCheck = True
                        
            if keys[pygame.K_q]:
                run = False

        collision_tolerance1 = 100
        if Small_Cube.colliderect(Big_Cube):
            time.sleep(1)
            x1 = 200
            y1 = 200
            x = 930
            y = 480
            vel1 = 0
            vel = 0
            SPEED = 0
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
                SPEED = 7
                SpawnBullet = True
                BPS = 30
                BPSCheck = True

            if keys[pygame.K_q]:
                run = False
        
        if keys[pygame.K_m]:
            try:
                Inst = pygame.image.load('Instructions.png')
                Inst1 = pygame.transform.scale(Inst, (1000, 700))
                WINDOW.blit(Inst1, (450, 200))
            except:
                pass

        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()
