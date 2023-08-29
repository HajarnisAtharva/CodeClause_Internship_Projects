import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print("Shanti - Millind Gaba")
    mixer.music.load('Shanti - Millind Gaba.mp3')
    songstatus.set("PLAYING")
    mixer.music.play()
def pausesong():
    songstatus.set("PAUSED")
    mixer.music.pause()
def stopsong():
    songstatus.set("STOPPED")
    mixer.music.stop()
def resumesong():
    songstatus.set("RESUME")
    mixer.music.unpause()
    
root=Tk()
#root.iconbitmap("play_music.ico")
root.title("Ariana's Music Player")
#root.image=PhotoImage( file = "music.png")
root.image=Frame(root,height=618,width=1366)
root.c=Canvas(root.image,height=618,width=1366)
root.c.pack()
root.back=PhotoImage(file="music.png")
        

mixer.init()
songstatus=StringVar()
songstatus.set("CHOOSING")
#playlist---------------
playlist=Listbox(root,selectmode=SINGLE,bg="red",fg="black",font=('arial',15),width=40)
playlist.grid(columnspan=5)
os.chdir(r'D:\CodeClause Internship\Player Ariana')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)
    playbtn=Button(root,text="Play",command=playsong)
    playbtn.config(font=('arial',20),bg="cyan",fg="black",padx=8,pady=8)
    playbtn.grid(row=1,column=0)
    pausebtn=Button(root,text="Pause",command=pausesong)
    pausebtn.config(font=('arial',20),bg="cyan",fg="black",padx=8,pady=8)
    pausebtn.grid(row=1,column=1)
    stopbtn=Button(root,text="Stop",command=stopsong)
    stopbtn.config(font=('arial',20),bg="cyan",fg="black",padx=8,pady=8)
    stopbtn.grid(row=1,column=2)
    Resumebtn=Button(root,text="Resume",command=resumesong)
    Resumebtn.config(font=('arial',20),bg="cyan",fg="black",padx=8,pady=8)
    Resumebtn.grid(row=1,column=3)
    mainloop()









