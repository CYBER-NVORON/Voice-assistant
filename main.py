from tkinter import *
from tkinter import ttk
from ttkwidgets import TickScale
from PIL import Image, ImageTk
from platform import system
from music import Music
from logic import Voice_assistant
import webbrowser
from configparser import ConfigParser

music = Music()
alice = Voice_assistant()
window = Tk()

count_slider=1

#При закрытии главного окна
def on_closing():
    with open("config.ini","r+") as file:
        config.write(file)
    window.destroy()


#При нажатии кнопки button
def button_act(self):
    music.background_music.pause()
    alice.makeSomething(alice.command())
    music.background_music.unpause()


#При нажатии кнопки settings
def settings_act(self):

    def background(_=None):
        music.background_music.set_volume(volume_background_music.get()/100)
        config.set("Volume", "background_volume", str(int(volume_background_music.get())))

        
    #При закрытии окна настроек
    def on_closing_settings():
        #Сохранение громкости в файл
        config.set("Volume", "background_volume", str(int(volume_background_music.get())))
        settings_window.destroy()

    settings_window = Toplevel(window)
    settings_window.geometry("300x500")
    settings_window.resizable(False, False)
    settings_window.title("Settings")
    settings_window.wm_attributes("-topmost", True)
    settings_window.wm_attributes("-transparent", True)
    canvas_set = Canvas(settings_window, width=width, height=height)
    #Закрытие окна настроек
    settings_window.protocol("WM_DELETE_WINDOW", on_closing_settings)


    #Фоновое изображение в настройках
    # background_settings_image = ImageTk.PhotoImage(Image.open("resources/interface/Dark_theme/black-theme-background.jpg"))
    # canvas_set.create_image(0, 0, image=background_settings_image, anchor=NW)
    # canvas_set.pack()
    
    #Текст "Музыка"
    canvas_set.create_text(50, 20,text="Музыка",font = 'Arial 25')
    canvas_set.pack()

    #Ползунок для настройки сохранения
    img_slider = ImageTk.PhotoImage(file="resources/interface/Dark_theme/slider18.png", master= settings_window)
    style=ttk.Style(settings_window)
    global count_slider
    count_slider+=1
    string_slider=str(count_slider)+'.custom.Horizontal.Scale.slider'
    style.element_create(string_slider, 'image', img_slider)
    style.layout('custom.Horizontal.TScale', [('Horizontal.Scale.trough', {'sticky': 'nswe'}),(string_slider,{'side': 'left', 'sticky': ''})])
    volume_background_music = TickScale(settings_window,  orient="horizontal", style='custom.Horizontal.TScale', showvalue=FALSE, length=300, from_=0, to=100, resolution=1, command=background)
    if int(music.background_music.get_volume()*100) == 0:
        volume_background_music.set(int(music.background_music.get_volume()*100))
    else:
        volume_background_music.set(int(music.background_music.get_volume()*100)+1)
    volume_background_music.place(x=0,y=40)

    settings_window.mainloop()



#Активация фоновой музыки
music.background_music.play(loops=-1)


#Настройки для сохранения
config = ConfigParser()

try:
    open("config.ini", "r")
except:
    open("config.ini", "w")
    config.add_section("Volume")
    config["Volume"] = {'background_volume': "50"}
    with open("config.ini", "w") as file:
        config.write(file)

config.read("config.ini")
music.background_music.set_volume(int(config.get('Volume','background_volume'))/100)

#Проверка размер окна, с помощью картинки
(width,height)=(Image.open("resources/Alice/Dark_theme/1.jpg")).size

#Настройки окна
window.eval('tk::PlaceWindow . center')
window.geometry(str(width)+"x"+str(height))
window.resizable(False, False)
window.title("Alice Voice Assistant")
window.wm_attributes("-transparent", True)
window.iconphoto(True, PhotoImage(file=('resources/interface/icon/icon.png')))
canvas = Canvas(window, width=width, height=height)


#Закрытие главного окна
window.protocol("WM_DELETE_WINDOW", on_closing)


#Иконка приложения
if system() == 'Darwin':
    icon = 'resources/interface/icon/icon.icns'
elif system() == 'Windows':
    icon = 'resources/interface/icon/icon.ico'
else:
    icon = 'resources/interface/icon/icon.xbm'
window.iconbitmap(icon)


#Изображение Алисы
alice_image = ImageTk.PhotoImage(file="resources/Alice/Dark_theme/1.jpg")
canvas.create_image(0, 0, image=alice_image, anchor=NW)
canvas.pack()


#Кнопка для активации logic.py
button_image = ImageTk.PhotoImage(file="resources/interface/Dark_theme/button1.png")
button_activate = canvas.create_image(width/2, height-50, image=button_image)
canvas.tag_bind(button_activate, "<Button-1>", button_act)

#Кнопка для активации Настройки
settings_image = ImageTk.PhotoImage(file="resources/interface/Dark_theme/settings.jpg")
settings_activate = canvas.create_image(330, 20, image=settings_image)
canvas.tag_bind(settings_activate, "<Button-1>", settings_act)

window.mainloop()