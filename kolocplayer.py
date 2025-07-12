import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as mb
import ffmpeg
import pyglet
from tkinter.messagebox import showerror, showwarning, showinfo

homuak = 0

sound = None
h = "en"
x = None
sor = None
q = 0

def hel():
    showinfo(title="helper", message="''PLAY''-Вклюючить музыку; ''load''-Загрузить музыку; ''restart''-останвка музыки + перемотка до начала; 'Кликер'- ку и так понятно")

def play():
    global h
    global x
    global s
    global sound
    global sor
    global q
    if x == None:
        mb.showerror("Ошибка",
                     "Выбери музыку кнопока (load)")
    if x == "":
        mb.showerror("Ошибка",
                     "Выбери музыку кнопока (load)")
        
    sound = pyglet.media.load(x, streaming=True)
    q = q+1
    if q == 2:
        mb.showerror("Ошибка",
                     "Используйте только 1 play! Перезапуск.")
    q = 1
    sor = sound.play()

def lo():
 global x
 x = filedialog.askopenfilename(title="Выберите музыку:", initialdir="C://",filetypes=[("Популярные:", "*.mp3 *.wav *.ogg"), ("Все офф. проверенные:", "*.mp3 *.wma *.asf *.sami *.smi *.aac *.adts *.flac *.ogg *.au *.mp2 *.wav") , ("All files", "*")])
 mesto["text"] = x
def de():
    global sor
    global q
    q = 0
    sor.delete()

def ho():
    global homuak
    homuak += 1
    hom["text"] = f"{homuak}"
    
    
root = Tk()
root.geometry("512x256")
root.title("kolocplayer")
root.resizable(False, False)

root.configure(bg='grey')

label = ttk.Label(text="v0.1.2a_gui")
label.pack(anchor="nw")

tg = ttk.Label(text="https://t.me/kolocer")
tg.place(x=0, y=235)

by = ttk.Label(text="by koloc")
by.place(x=460, y=0)

mesto = ttk.Label(text=x)
mesto.pack(anchor="sw")

hom = ttk.Label(text=homuak,)
hom.place(x=250, y=185)

play = ttk.Button(text="PLAY", command=play, state=[h])
play.pack(anchor=CENTER, expand=1)

lo = ttk.Button(text="load", command=lo)
lo.pack(anchor=SE, expand=1)

de = de = ttk.Button(text="restart", command=de)
de.pack(anchor=SE, expand=1)

tap = de = ttk.Button(text="Кликер", command=ho)
tap.pack(anchor=SW)

hel = de = ttk.Button(text="help", command=hel)
hel.pack(anchor=SE, expand=1)

mainloop()
