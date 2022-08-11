import os
import time
import random
import pyttsx3
import webbrowser
import subprocess
from platform import system
import speech_recognition as sr

operation_system = system()

class Voice_assistant():

	def __init__(self):
		pass

	def talk(self, words):
		#print(words)
		os.system("say " + words)

	def command(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			#r.pause_threshold = 1
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)

		try:
			zadanie = r.recognize_google(audio, language="ru-RU").lower()

		except sr.UnknownValueError:
			print(self.command())
			self.talk("Я вас не поняла")
			zadanie = self.command()

		return zadanie

	def makeSomething(self, zadanie):
		#Блок разговора с Алисой
		if zadanie == 'привет' or zadanie == 'здравствуйте' or zadanie == 'доброе утро' or zadanie == 'добрый день' or zadanie == 'добрый вечер':

			day_time = int(time.strftime('%H'))
			
			if day_time < 12:
				self.talk('Доброе утро.')

			elif 12 <= day_time < 18:
				self.talk('Добрый день.')

			else:
				self.talk('Добрый вечер.')

			self.talk("Чем я могу помочь?")

		elif zadanie == 'алиса':
			self.talk("Слушаю...")

		elif zadanie == 'как тебя зовут':
			self.talk("Меня зовут Алиса")

		elif zadanie == 'как дела':
			dela = random.randint(1,2)

			if (dela == 1):
				self.talk("Пока я с вами, у меня всё хорошо")

			elif (dela == 2):
				self.talk("Всё в норме. Спасибо, что интересуетесь.")
			
		#Блок выключения асисстента
		elif zadanie == 'пока' or zadanie == 'досвидания':
			self.talk("Пока")

		elif zadanie == 'сколько времени' or zadanie == 'время':
			
			self.talk("Время:"+time.strftime('%H'))
			if int(time.strftime('%H'))==1 or int(time.strftime('%H'))==21:
				self.talk(" час")
			elif int(time.strftime('%H'))==2 or int(time.strftime('%H'))==3 or int(time.strftime('%H'))==4 or int(time.strftime('%H'))==22 or int(time.strftime('%H'))==23 or int(time.strftime('%H'))==24:
				self.talk(" часa")
			else:
				self.talk(" часов")
			self.talk(time.strftime('%M')+" минут")
		
		#Блок открытия/закрытия приложений
		elif 'открой калькулятор' in zadanie:
			
			self.talk("Открываю калькулятор")

			if operation_system == 'Darwin':
				os.system(f"open {'/Applications/Calculator.app'}")

			elif operation_system == 'Windows':
				os.system('start C:\\Windows\\System32\\calc.exe')

			else:
				subprocess.run("gnome-calculator")

		elif 'открой браузер' in zadanie:

			self.talk("Открываю браузер")

			if operation_system == 'Darwin':
				os.system(f"open {'/Applications/Safari.app'}")

			else:
				webbrowser.open("https://yandex.ru/")
		
		elif 'открой календарь' in zadanie:

			self.talk("Открываю календарь")

			if operation_system == 'Darwin':
				os.system(f"open {'/Applications/Calendar.app'}")

			else:
				webbrowser.open("https://calendar.yandex.ru/")

		elif 'открой карту' in zadanie:
			self.talk("Открываю карту")

			if operation_system == 'Darwin':
				os.system(f"open {'/Applications/Maps.app'}")
			else:
				webbrowser.open("https://map.yandex.ru/")


		elif 'включи диктофон' in zadanie:
			self.talk("Включаю диктофон")

			if operation_system == 'Darwin':
				os.system(f"open {'/Applications/VoiceMemos.app'}")
			else:
				self.talk("Данная функция на вашей операционной системе не поддерживается")

		elif 'включи музыку' in zadanie:
			self.talk("Включаю музыку")

			if operation_system == 'Darwin':
				os.system(f"open {'/Applications/iTunes.app'}")
			else:
				self.talk("Данная функция на вашей операционной системе не поддерживается")
	
		#Блок поиска запроса в Google
		elif 'найди в интернете' in zadanie:
			self.talk('Что мне найти?')
			r = sr.Recognizer()
			with sr.Microphone() as source:
				r.pause_threshold = 1
				r.adjust_for_ambient_noise(source, duration=1)
				audio = r.listen(source)
				url = r.recognize_google(audio).lower()
				self.talk('Вот что я смогла найти.')
			weburl="https://yandex.ru/search/?text=" + url
			webbrowser.get().open(weburl)