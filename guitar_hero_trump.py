from Tkinter import *
import pygame
import random

pygame.mixer.init()

pygame.mixer.music.load("audio/song.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

america_great = pygame.mixer.Sound("audio/america_great_again.wav")
america_great.set_volume(0.3)

great_wall = pygame.mixer.Sound("audio/great_wall.wav")
great_wall.set_volume(1)

great_great_wall = pygame.mixer.Sound("audio/great_great_wall.wav")
great_great_wall.set_volume(1)

def Keyboard(event):
    global x,y,r,head,test,america_great,great_wall
    Canevas.delete(head)
    key = event.char
    key = key.lower()
    if key == 'a' or key == 'q':
        if test == 0 and y>=422 and y<=497:
            great_wall.play()


    elif key == 'z' or key == 'w':
        if test == 1 and y>=422 and y<=497:
            america_great.play()

    elif key == 'e':
        if test == 2 and y>=422 and y<=497:
            great_great_wall.play()

    ball_creation()


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

def main():
    global x,y,r,head,test
    y+=1
    if test == 0:
        r+=0.08
        x-=0.18
        Canevas.coords(head,x-r, y-r, x+r, y+r)

    elif test == 1:
        r+=0.08
        Canevas.coords(head,x-r, y-r, x+r, y+r)

    elif test == 2:
        r+=0.08
        x+=0.18
        Canevas.coords(head,x-r, y-r, x+r, y+r)

    root.after(5,main)



def line():
    global trump1,trump2,trump3
    Canevas.create_line(290,100,180,475,width=10,fill='Firebrick')
    Canevas.create_image(235,460,anchor=CENTER, image=trump2)
    Canevas.create_line(320,100,280,475,width=10,fill='Orange Red')
    Canevas.create_image(330,460,anchor=CENTER, image=trump1)
    Canevas.create_line(350,100,380,475,width=10,fill='Forest Green')
    Canevas.create_image(425,460,anchor=CENTER, image=trump3)
    Canevas.create_line(380,100,480,475,width=10,fill='Royal Blue')



test = 3
r=0
y=0

root = Tk()
root.title('GUITAR HERO TRUMP')

Canevas = Canvas(root, width = 667, height =500, bg='Black')
Canevas.focus_set()
Canevas.bind('<Key>',Keyboard)

back = PhotoImage(file="pictures/trump.gif")
trump1 = PhotoImage(file="pictures/trump0.gif")
trump2 = PhotoImage(file="pictures/trump1.gif")
trump3 = PhotoImage(file="pictures/trump2.gif")
Canevas.create_image(0,0,anchor=NW, image=back)


line()
main()
ball_creation()

Canevas.pack()

root.mainloop()
