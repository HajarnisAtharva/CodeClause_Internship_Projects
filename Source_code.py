#Project 1 (Music Player in Python)

# In this project we are creating a GUI based MP3 player using python libraries

# Step-1 : Importing all necessory python libraries
from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os

# Step-2 : Initializing pygame.mixer
mixer.init()

# Step-3 : Initializing the root window
# Creating GUI 
root = Tk ()
root.geometry ('700x200')
root.title ('CodeClause Music Player')
root.resizable(0,0)
root.update()
root.mainloop()

# Step-4 : Introducing the Load, Play, Pause & Resume functions in the player
# Load Function
def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))
    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)

# Play Function
def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))
    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()
    status.set("Song PLAYING")

# Pause Function
def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")

# Resume Function
def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")

# Step-5 : Creating the LabelFrames and StringVar variables
# Setting all the frames
song_frame = LabelFrame(root, text='Current Song', bg='LightBlue', width=400, height=80)
song_frame.place(x=0, y=0)
button_frame = LabelFrame(root, text='Control Buttons', bg='Turquoise', width=400, height=120)
button_frame.place(y=80)
listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue')
listbox_frame.place(x=400, y=0, height=200, width=300)

# Setting all StringVar variables
current_song = StringVar(root, value='<Not selected>')
song_status = StringVar(root, value='<Not Available>')

# Step-6 : Placing all the widgets in all the three LabelFrames
# Playlist ListBox
playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)

# SongFrame Labels
Label(song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)
song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25)
song_lbl.place(x=150, y=20)

# Buttons in the main screen
pause_btn = Button(button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=7, command=lambda: pause_song(song_status))
pause_btn.place(x=15, y=10)

play_btn = Button(button_frame, text='Play', bg='Aqua', font=("Georgia", 13), width=7, command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, text='Resume', bg='Aqua', font=("Georgia", 13), width=7, command=lambda: resume_song(song_status))
resume_btn.place(x=285, y=10)

load_btn = Button(button_frame, text='Load Directory', bg='Aqua', font=("Georgia", 13), width=35, command=lambda: load(playlist))
load_btn.place(x=10, y=55)

# Step-7 : Creating the final Label that will display the status of the song
# Label at the bottom that displays the state of the music
Label(root, textvariable=song_status, bg='SteelBlue', font=('Times', 9), justify=LEFT).pack(side=BOTTOM, fill=X)