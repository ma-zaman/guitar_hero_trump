from Tkinter import *
import pygame
import random
import tkFont

pygame.mixer.init()

pygame.mixer.music.load("audio/song.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

america_great = pygame.mixer.Sound("audio/america_great_again.wav")
america_great.set_volume(0.1)

great_wall = pygame.mixer.Sound("audio/great_wall.wav")
great_wall.set_volume(15)

great_great_wall = pygame.mixer.Sound("audio/great_great_wall.wav")
great_great_wall.set_volume(15)

youre_fired = pygame.mixer.Sound("audio/youre_fired.wav")
youre_fired.set_volume(15)

what_the_hell = pygame.mixer.Sound("audio/what_the_hell.wav")
what_the_hell.set_volume(5)

def Keyboard(event):
    global x,y,r,head,test,america_great,great_wall,score,size,scoretext,putx,puty,itemputin,putin,speed
    Canevas.delete(head)
    key = event.char
    key = key.lower()
    if key == 'a' or key == 'q':
        if test == 0 and y>=422 and y<=497:
            great_wall.play()
            score+=1

        else:
            error()


    elif key == 'z' or key == 'w':
        if test == 1 and y>=422 and y<=497:
            america_great.play()
            score+=1

        else:
            error()

    elif key == 'e':
        if test == 2 and y>=422 and y<=497:
            great_great_wall.play()
            score+=1

        else:
            error()

    else:
        error()

    if score/10.0 == score/10 and score != 0:
        speed+=1
        itemputin = Canevas.create_image(putx,puty,anchor=CENTER, image=putin)
        putine()

    Canevas.delete(scoretext)
    scoretext = Canevas.create_text(333,60,anchor=CENTER,text=str(score),width=100,font=size)
    ball_creation()

def error():
    global score,speed
    score-=1
    if score<0:
        score=0
    rand = random.randint(0,1)
    if rand == 0:
        youre_fired.play()

    else:
        what_the_hell.play()

def ball_creation():
    global x,y,r,head,test
    test=random.randint(0,2)
    r=10
    y=100
    if test == 0:
        x = 300

    elif test == 1:
        x = 330

    else:
        x = 365

    head = Canevas.create_oval(x-r, y-r, x+r, y+r, fill='Salmon')

def putine():
    global putx,puty,putin,itemputin,mov,testa
    Canevas.delete(itemputin)
    putx-=mov
    itemputin = Canevas.create_image(putx,puty,anchor=CENTER, image=putin)
    if putx >- 150 and mov>0:
        root.after(5,putine)

    elif putx < 680 and mov<0:
        root.after(5,putine)

    else:
        mov = -mov
        if testa == 0:
            putin = PhotoImage(file="pictures/putin_bear1.gif")
            testa=1

        else:
            putin = PhotoImage(file="pictures/putin_bear.gif")
            testa=0





def main():
    global x,y,r,head,test,scoretext,speed
    y+=speed
    if test == 0:
        r+=0.08*speed
        x-=0.18*speed
        Canevas.coords(head,x-r, y-r, x+r, y+r)

    elif test == 1:
        r+=0.08*speed
        Canevas.coords(head,x-r, y-r, x+r, y+r)

    elif test == 2:
        r+=0.08*speed
        x+=0.18*speed
        Canevas.coords(head,x-r, y-r, x+r, y+r)

    if y > 550:
        error()
        Canevas.delete(scoretext)
        scoretext = Canevas.create_text(333,60,anchor=CENTER,text=str(score),width=100,font=size)
        Canevas.delete(head)
        ball_creation()

    root.after(10,main)



def line():
    global trump1,trump2,trump3
    Canevas.create_line(290,100,180,475,width=10,fill='Firebrick')
    Canevas.create_image(235,460,anchor=CENTER, image=trump1)
    Canevas.create_line(320,100,280,475,width=10,fill='Orange Red')
    Canevas.create_image(330,460,anchor=CENTER, image=trump2)
    Canevas.create_line(350,100,380,475,width=10,fill='Forest Green')
    Canevas.create_image(425,460,anchor=CENTER, image=trump3)
    Canevas.create_line(380,100,480,475,width=10,fill='Royal Blue')



test = 3
r=0
y=0
score=0
putx=750
puty=450
testa=0
mov=2
speed=1

root = Tk()
root.title('GUITAR HERO TRUMP')

Canevas = Canvas(root, width = 667, height =500, bg='Black')
Canevas.focus_set()
Canevas.bind('<Key>',Keyboard)

back = PhotoImage(file="pictures/trump.gif")
trump1 = PhotoImage(file="pictures/trump0.gif")
trump2 = PhotoImage(file="pictures/trump1.gif")
trump3 = PhotoImage(file="pictures/trump2.gif")
putin = PhotoImage(file="pictures/putin_bear.gif")
Canevas.create_image(0,0,anchor=NW, image=back)

size = tkFont.Font(size=50)
scoretext = Canevas.create_text(333,60,anchor=CENTER,text=str(score),width=100,font=size)


line()
main()
ball_creation()

Canevas.pack()

root.mainloop()
