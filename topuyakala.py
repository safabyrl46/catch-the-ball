import pygame
import sys
pygame.init()

#Renkeler
siyah = (0,0,0)
beyaz = (255,255,255)
kırmızı = (255,0,0)
koyu_yesil = (50,160,50)
yesil = (0,255,0)
mavi = (0,0,255)

#Ekran
A = 800
B = 700
ekran = pygame.display.set_mode((A,B))
pygame.display.set_caption("Topu Yakala!")

#Yazılar
font = pygame.font.SysFont('arial',18)
font2 = pygame.font.SysFont('arial',80)

#Top ve Hareketi
resim = pygame.image.load("top.png").convert()
arkaplan = pygame.image.load("saha2.jpg").convert()
FPS = 40
fpsClock = pygame.time.Clock()
topututma = 0
can = 50
x_hiz = 8
y_hiz = 8
rx = 380
ry = 480
resim = pygame.transform.scale(resim,(150,150))
arkaplan = pygame.transform.scale(arkaplan,(800,700))
pygame.display.update()

#Ana kısım
calistirma = True
while calistirma:
    ekran.fill(siyah)
    yazi = font.render("SKOR:" + str(topututma),True,(0,255,0),(0,0,0))
    yazi2 = font.render("CAN:" + str(can),True,(0,255,0),(0,0,0))
    yazi3 = font2.render("OYUN BİTTİ!",True,(0,255,0),(0,0,0)) 
    resim_konum = ekran.blit(resim,(rx,ry))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calistirma = False
            pygame.quit()
            sys.exit()
    #Topumuza hareketlilik veriyoruz
    rx += x_hiz
    ry += y_hiz
    if rx > 650 or rx < 0:
        x_hiz *=-1
    if ry > 550 or ry < 0:
        y_hiz *= -1
    keys = pygame.key.get_pressed()
    #Tıklama olayı gerçekleştiğinde neler olacağını belirtiyoruz
    if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos_x = pos[0]
            pos_y = pos[1]
            if resim_konum.collidepoint(pos_x,pos_y):
                print(str(pos_x)+ " " + str(pos_y))
                print("Topu Buldunuz!")
                topututma += 1
            else:
                print("Topu Tutturamadın!")
                can -= 1
                if can == 0:
                    ekran.blit(yazi3,(220,275))
                    ekran.blit(yazi,(222,360))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    calistirma = False
    fpsClock.tick(FPS) 
    ekran.blit(yazi,(700,20))
    ekran.blit(yazi2,(700,50))
    if keys[pygame.K_ESCAPE]:
        calistirma = False    
    pygame.display.update()
pygame.quit()