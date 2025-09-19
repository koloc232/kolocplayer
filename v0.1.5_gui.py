import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.messagebox import showerror, showwarning, showinfo
from pyglet.media import Player
import pyglet
import webbrowser
homuak = 0

hj = Player()

sor= None

sound = None
h = "en"
x = None
sor = None
q = 0

def callback(event):
    webbrowser.open_new(r"https://github.com/koloc232/kolocplayer")

def vollll():
    ij= vol.get()
    print(ij)
    hj.volume = float(ij)

def hel():
    showinfo(title="helper", message="''PLAY''-Вклюючить музыку; ''load''-Загрузить музыку; ''pause''-остановка музыки; 'Кликер'- ку и так понятно,'volume'- громкость.,'reset'- останавливает и сбрасывает музыку(есть баг что надо нажать несколько раз для отановки (!музыка сбрасывается!) из-за испоьзования паузы)")

def play():
    global h,x,s,sound,sor,q,hj,sor

    sound = pyglet.media.load(x)
    hj.queue(sound)
    
    g=root.winfo_width()
    y=root.winfo_height()

    if g != 512:
     showwarning(title="Внимание!", message="Ширина окна неверна .")
    if y != 256:
            showwarning(title="Внимание!", message="Высотра окна неверна .")
            
    if x == None:
        mb.showerror("Ошибка",
                     "Выбери музыку кнопока (load)")
    if x == "":
        mb.showerror("Ошибка",
                     "Выбери музыку кнопока (load)")

    q = q+1
    if q == 2:
        mb.showerror("Ошибка",
                     "Используйте только 1 play!")
    q = 1
    
    sor = hj.play()

def lo():
    global x,q
    q=q-1
   
    x = filedialog.askopenfilename(title="Выберите музыку:", initialdir="C://",filetypes=[("Популярные:", "*.mp3 *.wav *.ogg"), ("Все офф. проверенные:", "*.mp3 *.wma *.asf *.sami *.smi *.aac *.adts *.flac *.ogg *.au *.mp2 *.wav") , ("All files", "*")])
    mesto["text"] = x

def ho():
    global homuak
    homuak += 1
    hom["text"] = f"{homuak}"

def pause():
    global hj,q
    q= q-1
    print(hj)
    hj.pause()
    
def delh():
    hj.on_eos()

    
root = Tk()
root.geometry("512x256")
root.title("kolocplayer")
root.resizable(False, False)

vol= IntVar(value=100)

root.configure(bg='grey')

label = ttk.Label(text="v0.1.5a_gui")
label.pack(anchor="nw")

gh = Label(root, text="Official Github",font=(10), fg = "blue", cursor="hand2")
gh.place(x=0, y=235)
gh.bind("<Button-1>", callback)

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

de = de = ttk.Button(text="pause", command=pause)
de.pack(anchor=SE, expand=1)

tap = de = ttk.Button(text="Кликер", command=ho)
tap.pack(anchor=SW)

hel = ttk.Button(text="help", command=hel)
hel.pack(anchor=SE, expand=1)

vol = ttk.Spinbox(from_=0.1, to=1, state="readonly", increment=0.1, width= 5)
vol.place(x= 0,y= 100)

voll= ttk.Label(text="volume")
voll.place(x= 50,y =100)

volll=ttk.Button(text="Принять", command=vollll)
volll.place(x=0, y= 125)

resr=ttk.Button(text="reset", command=delh)
resr.place(x=400, y= 50)

mainloop()


