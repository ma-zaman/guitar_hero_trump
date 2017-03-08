from Tkinter import *
import pygame

pygame.mixer.init()

pygame.mixer.music.load("audio/song.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)







root = Tk()
root.title('GUITAR HERO TRUMP')

Canevas = Canvas(root, width = 667, height =500, bg='Black')
Canevas.focus_set()

back = PhotoImage(file="pictures/trump.gif")
item = Canevas.create_image(0,0,anchor=NW, image=back)

Canevas.pack()

root.mainloop()
