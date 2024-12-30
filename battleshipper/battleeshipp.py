import pygame 
import os
from pygame import mixer
import sys 
import random
import csv


pygame.init()
wind=pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Ship Finding Simulator")
font=pygame.font.SysFont("bahnschrift", 45)
fontss=pygame.font.SysFont("bahnschrift", 35)

user_text=''
b4=['4 Ship Coordinates - ']
b3=['3 Ship Coordinates - ']
b21=['2 Ship Coordinates - ']
b22=['2 Ship Coordinates - ']
b23=['2 Ship Coordinates - ']




FPS=60
#importing all images
start1img=pygame.image.load(os.path.join('assets','start.png'))
start1img=pygame.transform.scale(start1img, (330, 100))
exitimg=pygame.image.load(os.path.join('assets', 'exit.png'))
exitimg=pygame.transform.scale(exitimg, (330, 100))
loginimg=pygame.image.load(os.path.join('assets', 'login.png'))
loginimg=pygame.transform.scale(loginimg, (330, 100))
signimg=pygame.image.load(os.path.join('assets', 'signup.png'))
signimg=pygame.transform.scale(signimg, (330, 100))

menuimg=pygame.image.load(os.path.join('assets', 'menu.png'))
menu2=pygame.image.load(os.path.join('assets', 'menu2.png'))
menu3=pygame.image.load(os.path.join('assets', 'menu3.png'))

ship2=pygame.image.load(os.path.join('assets', '2ship.png'))
ship2=pygame.transform.scale(ship2, (300, 300))
ship3=pygame.image.load(os.path.join('assets', '3ship.png'))
ship3=pygame.transform.scale(ship3, (300, 300))
ship4=pygame.image.load(os.path.join('assets', '4ship.png'))
ship4=pygame.transform.scale(ship4, (300, 300))

dot=pygame.image.load(os.path.join('assets', 'dot.png'))
dot=pygame.transform.scale(dot, (50, 50))
dotnot=pygame.image.load(os.path.join('assets', 'dotnot.png'))
dotnot=pygame.transform.scale(dotnot, (50, 50))

board=pygame.image.load(os.path.join('assets', 'board.png'))
board=pygame.transform.scale(board, (1200, 1200))

table=pygame.image.load(os.path.join('assets', 'table.png'))

#SOUND

buttonsnd=mixer.Sound(os.path.join('assets', 'buttonsound.mp3'))
boom=mixer.Sound(os.path.join('assets', 'explosion.mp3'))
bgm=mixer.Sound(os.path.join('assets', 'backgroundtrack.mp3'))
bgm.play()
bgm.set_volume(0.4)

                
#button
class button():
    def __init__(self, x, y, image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked=False
    def draw(self):
        action =False
        #mouse
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked=True
                action=True
                buttonsnd.play()
                
                
                
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False
        wind.blit(self.image, (self.rect.x, self.rect.y))
        return action

 
class InputBox():
    def __init__(self, x, y):
        self.font = pygame.font.SysFont("bahnschrift", 35)
        self.inputBox = pygame.Rect(x, y, 140, 40)
        self.colourInactive = pygame.Color('lightskyblue3')
        self.colourActive = pygame.Color(36, 64, 98)
        self.colour = self.colourInactive
        self.text = ''

        self.active = False
        self.isBlue = True

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.inputBox.collidepoint(event.pos)
            self.colour = self.colourActive if self.active else self.colourInactive
            buttonsnd.play()
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    a.append(self.text)                   
                    self.text = ''
                    global usern
                    usern=a
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        txtSurface = self.font.render(self.text, True, self.colour)
        width = max(200, txtSurface.get_width()+10)
        self.inputBox.w = width
        screen.blit(txtSurface, (self.inputBox.x+5, self.inputBox.y+5))
        pygame.draw.rect(screen, self.colour, self.inputBox, 2)
        
        if self.isBlue:
            self.color = (0, 128, 255)
        else:
            self.color = (255, 100, 0)



start1=button(470,350,start1img)
exit=button(470,600,exitimg)
loginin=button(470,300,loginimg)
signupin=button(470,450,signimg)
#                                                               VARIABLES
wi4=[]#[[50, 60]]60 55
wi3=[]#[[35,60]]60 55
wi21=[]#[[15, 90]]60 55
wi22=[]
wi23=[]
hl=[]
array=[]
x, y = 75, 170
y1=55
x1=60
c=0
global j
j=0
h=0
fo=4
th=3
tw1, tw2, tw3=2, 2, 2

def forgotpassw():
    while True: 
        global a
        a=[]
        buttonsnd.play()         
        name=font.render("Enter Username:", True, (36, 64, 98))
        password=font.render("Enter New Password:", True, (36, 64, 98))
        esc=fontss.render("Press ESCAPE to Menu", True, (36, 64, 98))
        
        input1 = InputBox(450, 200)
        input2 = InputBox(550, 500) 
        pygame.display.update()        
        while True:
            for event in pygame.event.get():               
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        j=0
                        main()   
                      
                
                input1.handle(event)
                input2.handle(event)
            wind.blit(menu3, (0,0))
            wind.blit(name, (50, 200))
            wind.blit(esc, (0, 0))
            
            input1.draw(wind)
            
            if len(a)==1:
                with open("LoginInfo.csv", 'r', newline='\n') as loginfo:
                    logwriter=csv.reader(loginfo)
                    for i in logwriter:
                        if i[0]==a[0]:
                            wind.blit(menu3, (0, 0))
                            wind.blit(password, (50, 500))
                            wind.blit(esc, (0, 0))
                            input2.draw(wind)
                        
                            
            if len(a)==2:
                loginfo=open("LoginInfo.csv", 'r', newline='\n')
                temp=open("temp.csv", 'w', newline='\n')
                logre=csv.reader(loginfo)
                tempwr=csv.writer(temp) 
                for i in logre:
                    if i[0]!=a[0]:
                        tempwr.writerow(i)
                    else:
                        tempwr.writerow(a)                              
                loginfo.close()
                temp.close()
                os.replace('temp.csv', 'LoginInfo.csv')   
                main()                     
            pygame.display.flip()

def signup():
    global j 
    j=1
    while True: 
        global a
        a=[]
        buttonsnd.play()         
        name=font.render("Enter Your Name:", True, (36, 64, 98))
        password=font.render("Enter a Password:", True, (36, 64, 98))
        esc=fontss.render("Press ESCAPE to Menu", True, (36, 64, 98))
        input1 = InputBox(450, 200)
        input2 = InputBox(550, 500) 
        
        
        pygame.display.update()        
        while True:
            for event in pygame.event.get():               
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        j=0
                        main()          
                
                input1.handle(event)
                input2.handle(event)
            wind.blit(menu3, (0,0))
            wind.blit(name, (50, 200))
            wind.blit(password, (50, 500))
            wind.blit(esc, (0, 0))
            input1.draw(wind)
            input2.draw(wind)
            if len(a)==2:
                with open("LoginInfo.csv", 'a+', newline='\n') as loginfo:
                    logwriter=csv.writer(loginfo)
                    logwriter.writerow(a)
                main()                          
            pygame.display.flip()

def login(h):
    global j
    j=1
    while True: 
        global a
        a=[]
        buttonsnd.play()         
        name=font.render("Enter Your Name:", True, (36, 64, 98))
        password=font.render("Enter Your Password:", True, (36, 64, 98))
        esc=fontss.render("Press ESCAPE to Menu", True, (36, 64, 98))
        forgot=font.render("If forgot Password Press RSHIFT", True, (36, 64, 98))
        input1 = InputBox(450, 200)
        input2 = InputBox(550, 500) 
        
          
        pygame.display.update()        
        while True:
            for event in pygame.event.get():               
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RSHIFT:
                        forgotpassw() 
                    if event.key==pygame.K_ESCAPE:
                        j=0
                        main()      
                
                input1.handle(event)
                input2.handle(event)
            wind.blit(menu3, (0,0))
            if h!=0:
                error=font.render("Username/Password Wrong Try Again", True, ("red"))
                wind.blit(error, (200, 660))
            
            wind.blit(name, (50, 200))
            wind.blit(password, (50, 500))
            wind.blit(forgot,(300, 600) )
            wind.blit(esc, (0, 0))
            input1.draw(wind)
            input2.draw(wind)
            if len(a)==2:
                
            
                with open("LoginInfo.csv", 'r+', newline='\n') as loginfo:
                    logwriter=csv.reader(loginfo)
                    for lines in logwriter:
                        if a==lines:
                            main()
                            global c
                            c=1
                if c!=1:
                    login(h=4)
                                           
            pygame.display.flip()


def singlemenu():
    global wl
    wl=0
    while True: 
        wind.blit(menu2, (0,0))
        file=open("Rules.txt", 'r')
        rules=file.readlines()        
        wind.blit(menu2, (0,0))
        for i in range(len(rules)):
            rule=fontss.render(rules[i].rstrip('\n'), True, (36, 64, 98))
            if i==5:
                wind.blit(rule, (555, 550))
            elif i==6:
                wind.blit(rule, (440, 600))
            else:
                wind.blit(rule, (110, 50+(100*i))) 

        file.close()
        pygame.display.update()
        while True:
            for event in pygame.event.get(): 
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        buttonsnd.play()
                        playsingle()
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            
def shipplacement():
    x4=random.randrange(50, 230, 60)
    y4=random.randrange(60, 400, 55)
    global wi4
    global wi3
    global wi21
    global wi22
    global wi23

    a=[]                        #ship4 list
    a.append(x4)
    a.append(y4)
    wi4.append(a)
        
    for i in range(1,4):
        a=[]
        a.append(x4+(60*i))
        a.append(y4)
        wi4.append(a)
    x3=random.randrange(35, 275, 60)
    y3=random.randrange(60, 400, 55)
    while y3==y4:
        y3=random.randrange(60, 400, 55)
        if y3!=y4:
            break
        
    
                    
    a=[]                    #ship3 list
    a.append(x3)
    a.append(y3)
    wi3.append(a)
    for i in range(1,3):
        a=[]
        a.append(x3+(60*i))
        a.append(y3)
        wi3.append(a)
    
               
        
         # placing of wi2
    x21=random.randrange(15, 315, 60)
    y21=random.randrange(90, 400, 55)
    x22=random.randrange(15, 315, 60)
    y22=random.randrange(90, 400, 55)    
    x23=random.randrange(15, 315, 60)
    y23=random.randrange(90, 400, 55)        
        
    while y21==y22 or y22==y23 or y21==y23 or (y21-30)==y3 or (y22-30)==y3 or (y23-30)==y3 or (y21-30)==y4 or (y22-30)==y4 or (y23-30)==y4:
        y21=random.randrange(90, 400, 55)           
        y22=random.randrange(90, 400, 55)
        y23=random.randrange(90, 400, 55)
        if y21!=y22 and y22!=y23 and y21!=y23 and (y21-30)==y3 and (y22-30)==y3 and (y23-30)==y3 and (y21-30)==y4 and (y22-30)==y4 and (y23-30)==y4:                         
            break  


    a=[]     #ship21 list
    a.append(x21)
    a.append(y21)
    wi21.append(a)
    a=[]
    a.append(x21+60)
    a.append(y21)
    wi21.append(a) 
       

    a=[]     #ship22 list
    a.append(x22)
    a.append(y22)
    wi22.append(a)
    a=[]
    a.append(x22+60)
    a.append(y22)
    wi22.append(a)
       

    a=[]     #ship23 list
    a.append(x23)
    a.append(y23)
    wi23.append(a)
    a=[]
    a.append(x23+60)
    a.append(y23)
    wi23.append(a)

def shiptextfile():
                                 #text file coordinates
    s4y=chr((wi4[0][1] // 55)+64)
    s3y=chr((wi3[0][1] // 55)+64)
    s21y=chr(((wi21[0][1]-30) // 55)+64)
    s22y=chr(((wi22[0][1]-30) // 55)+64)
    s23y=chr(((wi23[0][1]-30) // 55)+64)
    s4x=((wi4[0][0] +10)// 60)
    s3x=((wi3[0][0]+25) // 60)
    s21x=((wi21[0][0]+45) // 60)
    s22x=((wi22[0][0]+45) // 60)
    s23x=((wi23[0][0]+45) // 60)
        
    for i in range(4):
        syx=s4x+i
        syx=str(syx)
        bo=s4y+syx
        b4.append(bo)
        b4.append(' ')
    b4.append('\n')
    for i in range(3):
        syx=s3x+i
        syx=str(syx)
        bo=s3y+syx
        b3.append(bo)
        b3.append(' ')
    b3.append('\n')
    for i in range(2):
        syx=s21x+i
        syx=str(syx)
        bo=s21y+syx
        b21.append(bo)
        b21.append(' ')
    b21.append('\n')
    for i in range(2):
        syx=s22x+i
        syx=str(syx)
        bo=s22y+syx
        b22.append(bo)
        b22.append(' ')
    b22.append('\n')
    for i in range(2):
        syx=s23x+i
        syx=str(syx)
        bo=s23y+syx
        b23.append(bo)
        b23.append(' ')
    b23.append('\n')
        
    shipcords=open("ShipCoordinates.txt", 'w+')
    shipcords.writelines(b4)
    shipcords.writelines(b3)
    shipcords.writelines(b21)
    shipcords.writelines(b22)
    shipcords.writelines(b23)
    shipcords.close()

def shipstatus():
    #checking what square
    swet=user_text
    swet=list(swet)
    ny=swet[0]
    ny=ny.upper()
    nx=int(swet[1])
    a=ord(ny)-65
    ny=170+(55*a)
    nx=75+(60*(nx-1))
                        
    #if hit or miss and what ship
    if ((nx-25)==wi4[0][0] and (ny-110)==wi4[0][1]) or ((nx-25)==wi4[1][0] and (ny-110)==wi4[1][1]) or ((nx-25)==wi4[2][0] and (ny-110)==wi4[2][1]) or ((nx-25)==wi4[3][0] and (ny-110)==wi4[3][1]):    
        wind.blit(dot, (nx, ny))
        global fo
        global th
        global tw1
        global tw2
        global tw3
        fo-=1
        if fo==0:
            wind.blit(ship4, (770, 130))
        if fo==th==tw1==tw2==tw3==0:
            singleendwin()

    elif ((nx-40)==wi3[0][0] and (ny-110)==wi3[0][1]) or ((nx-40)==wi3[1][0] and (ny-110)==wi3[1][1]) or ((nx-40)==wi3[2][0] and (ny-110)==wi3[2][1]):
        wind.blit(dot, (nx, ny))       
        th-=1
        if th==0:
            wind.blit(ship3, (770, 210))
        if fo==th==tw1==tw2==tw3==0:
            singleendwin()                         
    elif ((nx-60)==wi21[0][0] and (ny-80)==wi21[0][1]) or ((nx-60)==wi21[1][0] and (ny-80)==wi21[1][1]):
        wind.blit(dot, (nx, ny))
        tw1-=1
        if tw1==0:
            wind.blit(ship2, (700, 330)) 
        if fo==th==tw1==tw2==tw3==0:
            singleendwin()
    elif ((nx-60)==wi22[0][0] and (ny-80)==wi22[0][1]) or ((nx-60)==wi22[1][0] and (ny-80)==wi22[1][1]):
        wind.blit(dot, (nx, ny))
        tw2-=1
        if tw2==0:
            wind.blit(ship2, (760, 280))         
        if fo==th==tw1==tw2==tw3==0:
            singleendwin()                           
    elif ((nx-60)==wi23[0][0] and (ny-80)==wi23[0][1]) or ((nx-60)==wi23[1][0] and (ny-80)==wi23[1][1]):
        wind.blit(dot, (nx, ny))
        tw3-=1
        if tw3==0:
            wind.blit(ship2, (860, 330))
        if fo==th==tw1==tw2==tw3==0:
            singleendwin()
                                                   
    else:
        wind.blit(dotnot, (nx, ny))
                 
        
        
    pygame.display.update()    
def playsingle():
    while True: 
        wind.blit(menu2, (0,0))
        wind.blit(board, (0,-100))
        welcstring="User : " + a[0] 
        welc=font.render(welcstring, True, (36, 64, 98))
        wind.blit(welc, (10, 650))
        input_rect = pygame.Rect(750, 510, 100, 60)
        input_rectscore = pygame.Rect(1130, 20, 50, 40)
        
        
        shipplacement()
        shiptextfile()

        pygame.display.update()
      #input THE coords
        global user_text
        user_text=""
        global score
        score=30       
        while True:
            for event in pygame.event.get():     
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key==pygame.K_RETURN:
                        score=int(score)
                        score-=1
                        if score==0:
                            singleendlose()
                        boom.set_volume(0.3)
                        boom.play()
                        
                        shipstatus()
                        user_text=""
                           
                    else:
                        user_text += event.unicode
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.draw.rect(wind, (211,211,211), input_rect)
            text_surface = font.render(user_text, True, (36, 64, 98))
            wind.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, text_surface.get_width()+10)
            
            pygame.draw.rect(wind, (211,211,211), input_rectscore)
            scoresurf = font.render(str(score), True, (36, 64, 98))
            scores=font.render("Score: ",True, (36, 64, 98))
            wind.blit(scores, (1000, 20))
            wind.blit(scoresurf, (input_rectscore.x, input_rectscore.y))
            
            
            pygame.display.flip()
            


               
def singleendwin():
    global text
    
    while True: 
        buttonsnd.play()
        wind.blit(menu2, (0,0))
        w="YOU WIN!  " + a[0]
        win=font.render(w, True, ("RED"))
        win1=font.render("Thank you for playing", True, (36, 64, 98))
        win2=font.render("PRESS SPACE for Leaderboard", True, (36, 64, 98))        
        win3=font.render("Press RSHIFT to Quit", True, (36, 64, 98)) 
        wind.blit(win, (500, 100))
        wind.blit(win1, (100, 200))
        wind.blit(win2, (100, 300))
        wind.blit(win3, (100, 400))
        
        
        pygame.display.update()
        text=''
        
        while True:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key == pygame.K_SPACE:
                        print("saduiudf")
                        insert()
                        disp()
                    elif event.key==pygame.K_RSHIFT:
                        disp()
                        pygame.quit()
                        sys.exit()
                    
                    else:
                        text += event.unicode
                        
                        
                
                
                
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()       
            
            pygame.display.flip()
        
        

def singleendlose():
    global text
    while True:
        #disp()
        buttonsnd.play()
        wind.blit(menu2, (0,0))
        w="YOU LOSE! " + a[0]
        win=font.render(w, True, ("RED"))
        win1=font.render("Thank you for playing", True, (36, 64, 98))
        win2=font.render("PRESS SPACE for Leaderboard", True, (36, 64, 98))        
        win3=font.render("Press RSHIFT to Quit", True, (36, 64, 98)) 
        wind.blit(menu2, (0,0))
        wind.blit(win, (500, 100))
        wind.blit(win1, (100, 200))
        wind.blit(win2, (100, 300))
        wind.blit(win3, (100, 400))
                        
        
        pygame.display.update()
        
        
        while True:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:          
                    if event.key==pygame.K_SPACE:
                        disp()
                    
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()   
                        

            pygame.display.flip()
    
        
            

def insert():
    nam = a[0]
    scor = score
    kl=[nam, scor]
    with open("scores.csv", 'a', newline='\n') as file:          #appending
        play = csv.writer(file)
        play.writerow(kl)
    with open("scores.csv", 'r', newline='\n') as file:         #decending order sorting
        play = csv.reader(file)
        for i in play:
            bl=int(i[1])
            i=[i[0], bl]
            array.append(i)
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):      
            if array[j][1] < array[j + 1][1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    with open("scores.csv", 'w', newline='\n') as file:   #ordered
        play = csv.writer(file)
        play.writerows(array)
    
                
def disp():
    global point
    x=110
    y=100
    with open("scores.csv", 'r', newline='\n') as playinfo:
        play=csv.reader(playinfo)
        for i in play:
            hl.append(i)
        
    while True:
        rule24=fontss.render("SCOREBOARD", True, ("RED"))
        wind.blit(menu2, (0,0))
        wind.blit(rule24, (110,50))
        wind.blit(table,(x,y))
        pygame.display.update()
        f=[]
        g=[]
        for k in hl:
            f.append(k[0])
            g.append(k[1])
            
        for i in range(0,len(f)):
            n=str(f[i])
            p=str(g[i])
            nam=fontss.render(n , True, (36, 64, 98))
            pts=fontss.render(p , True, (36, 64, 98))
            wind.blit(nam, (x,y))
            wind.blit(pts, (x+200,y))
            y+=50
            pygame.display.update()
        win1=font.render("Thank you for playing", True, (36, 64, 98))
        wind.blit(win1, (500,110))
        txt1=fontss.render("Enter right shift to quit", True, (36,64,98))
        wind.blit(txt1, (x,y))
        while True:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RSHIFT:
                        pygame.quit()
                        sys.exit()
           
            pygame.display.flip()
        

def main_menu():
    wind.blit(menuimg, (0,0))
    if exit.draw()==True: 
        pygame.quit()
        sys.exit()
    if j==0:
        if signupin.draw()==True:
            signup()
        if loginin.draw()==True:
            h=0
            login(h)  
    else:
        if start1.draw()==True:
            singlemenu()      
    
    
    pygame.display.update()

                                                            #MAIIIIIIIIIIIN 
def main():
    clock=pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()                
        main_menu()
        


      
if __name__=="__main__":
    main()
