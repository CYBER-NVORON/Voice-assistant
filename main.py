from time import sleep
from tkinter import *
from tkinter import ttk
from ttkwidgets import TickScale
from PIL import Image, ImageTk
from platform import system
from music import Music
from logic import Voice_assistant
import webbrowser
import configparser

music = Music()
voice = Voice_assistant()
window = Tk()

count_slider=1

#При закрытии главного окна
def on_closing():
    #Говорит:"Ты уже уходишь? Ну ладно, пока.
    window.destroy()


#При нажатии кнопки button
def button_act():
    music.background_music.pause()
    voice.makeSomething(voice.command())
    music.background_music.unpause()


#При нажатии кнопки settings
def settings_act():

    def background(_=None):
        music.background_music.set_volume(volume_background_music.get()/100)
        
    #При закрытии окна настроек
    def on_closing_settings():
        #Сохранение громкости в файл
        config.set("Volume", "background_volume", str(int(volume_background_music.get())))
        save.close()
        settings_window.destroy()
        




    settings_window = Toplevel(window)
    settings_window.geometry("300x500")
    settings_window.resizable(False, False)
    settings_window.title("Settings")
    settings_window.wm_attributes("-topmost", True)
    settings_window.wm_attributes("-transparent", True)

    #Закрытие окна настроек
    settings_window.protocol("WM_DELETE_WINDOW", on_closing_settings)


    #Фоновое изображение в настройках
    background_settings_image = ImageTk.PhotoImage(Image.open("resources/interface/Dark_theme/black-theme-background.jpg"))
    Label(settings_window, image=background_settings_image).pack()
    
    #Текст "Музыка"
    Label(settings_window, text="Музыка",font = 'Arial 25', fg='white', background='black').place(x=0,y=0)
    
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


    #Кнопка для перехода в группы в ВК

    #vk_image = ImageTk.PhotoImage(file="resources/interface/Dark_theme/vk.jpg")
    #Button(settings_window, image=vk_image, highlightthickness=0, padx=-100, pady=-100,  command = vk_act).place(x=173,y=467)

    #Кнопка для перехода в донат
    #donation_image = ImageTk.PhotoImage(file="resources/interface/Dark_theme/donation.jpg")
    #Button(settings_window, image=donation_image, highlightthickness=0, padx=-100, pady=-100, command = donation_act).place(x=232,y=467)

    #Кнопка для перехода на сайт об разработчиков
    #info_image = ImageTk.PhotoImage(file="resources/interface/Dark_theme/info.jpg")
    #Button(settings_window, image=info_image, highlightthickness=0, padx=-100, pady=-100, command = info_act).place(x=267,y=467)


    settings_window.mainloop()



#Активация фоновой музыки
music.background_music.play(loops=-1)


#Настройки для сохранения
config = configparser.ConfigParser(strict=False)
config.read("config.ini")
music.background_music.set_volume(int(config.get("Volume", "background_volume"))/100)
save = open('config.ini', 'w')

#Загрузка в конфиг значений, в случае, если не будет использовано окно settings_window
config.set("Volume", "background_volume", str(int(music.background_music.get_volume()*100)))
config.write(save)

#Проверка размер окна, с помощью картинки
(width,height)=(Image.open("resources/Alica/Dark_theme/1.jpg")).size

#Настройки окна
window.geometry(str(width)+"x"+str(height))
window.resizable(False, False)
window.title("Alica Voice Assistant")
window.wm_attributes("-transparent", True)


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
alica_image = ImageTk.PhotoImage(file="resources/Alica/Dark_theme/1.jpg")
Label(window, image=alica_image).place(x=-3,y=-3)


#Кнопка для активации main.py
button_image = ImageTk.PhotoImage(file="resources/interface/Dark_theme/button1.jpg")
Button(window, image=button_image, borderwidth=0, highlightthickness=0, padx=-100, pady=-100,  command = button_act,).pack(side= BOTTOM)

#Кнопка для активации Настройки
settings_image = ImageTk.PhotoImage(file="resources/interface/Dark_theme/settings.jpg")
Button(window, image=settings_image, highlightthickness=0, padx=-100, pady=-100, command = settings_act).place(x=310,y=0)

window.mainloop()