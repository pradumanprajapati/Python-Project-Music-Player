# Group 7 (Music Player)

# Sachin pal
# Praduman Kumar Prajapati



from pygame import mixer
from tkinter import *
import os
from pygame import *

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing\\n")
    mixer.music.play()

root=Tk()
root.title('Music player')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\Praduman Kumar\OneDrive\Desktop\New folder')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="play",command=playsong)
playbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

mainloop()