print("Загрузка...")
import pyglet
import os
import ctypes
import ffmpeg
import sys
from tkinter import filedialog
ctypes.windll.kernel32.SetConsoleTitleA(b"koloc_player by koloc232")
os.system('mode con: cols=43 lines=5')
os.system('cls' if os.name == 'nt' else 'clear')
print("Выбери фаил для того чтобы прослушать вашу музыку")
x = filedialog.askopenfilename(title="Выберите музыку:", initialdir="C://",filetypes=[("Популярные:", "*.mp3 *.wav *.ogg"), ("Все офф. проверенные:", "*.mp3 *.wma *.asf *.sami *.smi *.aac *.adts *.flac *.ogg *.au *.mp2 *.wav") , ("All files", "*")])
u = len(x)
if u == 0:
 sys.exit()
sound = pyglet.media.load(x, streaming=True)
os.system('mode con: cols=43 lines=12')
os.system('cls' if os.name == 'nt' else 'clear')
sound.play()
print()
print(x)
print("="*16+"(player)"+"="*19)
print()
print("="*10+"(Идёт проигрывание)"+"="*14)
print("_-_-_-_-_-_-_-_-v2.4._-_-_-_-_-_-_-_-_-_-_-_")
print("="*10+"(Создано Koloc232)"+"="*15)




