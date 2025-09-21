import os
import webbrowser
import pyglet
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
from tkinter import ttk
from pyglet.media import Player

# Инициализация плеера
player = Player()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.song_path = None
        self.play_count = 0
        self.volume_level = 1
        self.vol= None
        
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("512x256")
        self.root.title("kolocplayer")
        self.root.resizable(False, False)
        self.root.configure(bg='grey')

        self.create_widgets()

    def create_widgets(self):
        
        self.label = ttk.Label(text="v0.2.0a_gui")
        self.label.pack(anchor="nw")

        self.github_link = Label(self.root, text="Official Github", font=(10), fg="blue", cursor="hand2")
        self.github_link.place(x=0, y=235)
        self.github_link.bind("<Button-1>", self.open_github)

        self.by_label = ttk.Label(text="by koloc")
        self.by_label.place(x=460, y=0)

        self.song_label = ttk.Label(text="")
        self.song_label.pack(anchor="sw")

        self.click_count_label = ttk.Label(text="0")
        self.click_count_label.place(x=250, y=185)

        self.play_button = ttk.Button(text="PLAY", command=self.play_music , )
        self.play_button.pack(anchor=CENTER, expand=1)

        self.load_button = ttk.Button(text="load", command=self.load_music)
        self.load_button.pack(anchor=SE, expand=1)

        self.pause_button = ttk.Button(text="pause", command=self.pause_music)
        self.pause_button.pack(anchor=SE, expand=1)

        self.clicker_button = ttk.Button(text="Кликер", command=self.increment_click_count)
        self.clicker_button.place(x=120, y= 182)

        self.help_button = ttk.Button(text="help", command=self.show_help)
        self.help_button.pack(anchor=SE, expand=1)

        self.volume_control = ttk.Spinbox(from_=10, to=200, increment=10, width=5, justify="right")
        self.volume_control.place(x=0, y=100)

        self.proc = ttk.Label(text="%")
        self.proc.place(x=50, y=100)
        
        self.volume_lab = ttk.Label(text="volume")
        self.volume_lab.place(x=70, y=100)

        self.set_volume_button = ttk.Button(text="Принять", command=self.set_volume)
        self.set_volume_button.place(x=0, y=125)

        self.reset_button = ttk.Button(text="reset", command=self.reset_music)
        self.reset_button.place(x=400, y=50)
        
        

    def open_github(self, event):
        webbrowser.open_new("https://github.com/koloc232/kolocplayer")

    def set_volume(self):
        volume = self.volume_control.get()
        player.volume = float(volume)/100

    def show_help(self):
        help_message = (
            "'PLAY' - Включить музыку; "
            "'load' - Загрузить музыку; "
            "'pause' - остановка музыки; "
            "'Кликер' - ку и так понятно; "
            "'volume' - громкость; "
            "'reset' - останавливает и сбрасывает музыку."
        )
        mb.showinfo(title="helper", message=help_message)

    def play_music(self):
        if not self.validate_window_size():
            return

        if self.song_path is None or self.song_path == "":
            mb.showerror("Ошибка", "Выбери музыку кнопкой (load)")
            return

        if self.play_count >= 1:
            mb.showerror("Ошибка", "Используйте только 1 play!")
            return
            

        self.play_song()

    def validate_window_size(self):
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        if width != 512:
            mb.showwarning(title="Внимание!", message="Ширина окна неверна. (Приложение не будет работать)")
            return False
        if height != 256:
            mb.showwarning(title="Внимание!", message="Высота окна невера. (Приложение не будет работать)")
            return False

        return True

    def play_song(self):
        sound = pyglet.media.load(self.song_path)
        player.queue(sound)
        player.play()
        self.play_count += 1


    def load_music(self):
        self.song_path = filedialog.askopenfilename(
            title="Выберите музыку:", 
            initialdir="C://",
            filetypes=[("Популярные:", "*.mp3 *.wav *.aac *.aiff *.wma"), ("Все файлы", "*")]
        )
        self.song_label["text"] = self.song_path
        

    def increment_click_count(self):
        self.click_count_label["text"] = str(int(self.click_count_label["text"]) + 1)

    def pause_music(self):
        if player.playing:
            player.pause()
            self.play_count -= 1
            
    def reset_music(self):
        player.on_eos()
        self.play_count -= 1

def main():
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()