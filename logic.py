import os
import time
import random
import pyttsx3
import webbrowser
import subprocess
from platform import system
import speech_recognition as sr
from chatbot import Chat
from googletrans import Translator



class Voice_assistant():

	def __init__(self):
		self.template_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chatbotTemplate", "chatbottemplate.template")
		self.chat = Chat(self.template_file_path)
		self.operation_system = system()
		self.translator = Translator()

	def talk(self, words):
		#print(words)
		os.system("say " + words)

	def command(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			#r.pause_threshold = 1
			r.adjust_for_ambient_noise(source, 2)
			audio = r.listen(source)

		try:
			zadanie = r.recognize_google(audio, language="ru-RU").lower()

		except sr.UnknownValueError:
			print(self.command())
			self.talk("Я вас не поняла")
			zadanie = None

		return zadanie

	def makeSomething(self, zadanie):
		
		if zadanie is None:
			return

		if 'привет' in zadanie or 'здравствуйте' in zadanie or 'доброе утро' in zadanie or 'добрый день' in zadanie or 'добрый вечер' in zadanie:

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

		elif 'как тебя зовут' in zadanie:
			self.talk("Меня зовут Алиса")

		elif 'как дела' in zadanie:
			dela = random.randint(1,2)

			if (dela == 1):
				self.talk("Пока я с вами, у меня всё хорошо")

			elif (dela == 2):
				self.talk("Всё в норме. Спасибо, что интересуетесь.")
			
		elif 'пока' in zadanie or 'досвидания' in zadanie:
			self.talk("Пока")

		elif 'сколько времени' in zadanie or 'время' in zadanie:
			
			self.talk("Время:"+time.strftime('%H'))
			if int(time.strftime('%H'))==1 or int(time.strftime('%H'))==21:
				self.talk(" час")
			elif int(time.strftime('%H'))==2 or int(time.strftime('%H'))==3 or int(time.strftime('%H'))==4 or int(time.strftime('%H'))==22 or int(time.strftime('%H'))==23 or int(time.strftime('%H'))==24:
				self.talk(" часa")
			else:
				self.talk(" часов")
			self.talk(time.strftime('%M')+" минут")
		
		elif 'открой калькулятор' in zadanie:
			
			self.talk("Открываю калькулятор")

			if self.operation_system == 'Darwin':
				os.system(f"open {'/Applications/Calculator.app'}")

			elif self.operation_system == 'Windows':
				os.system('start C:\\Windows\\System32\\calc.exe')

			else:
				subprocess.run("gnome-calculator")

		elif 'открой браузер' in zadanie:

			self.talk("Открываю браузер")

			if self.operation_system == 'Darwin':
				os.system(f"open {'/Applications/Safari.app'}")
			else:
				webbrowser.open("https://yandex.ru/")
		
		elif 'открой календарь' in zadanie:

			self.talk("Открываю календарь")

			if self.operation_system == 'Darwin':
				os.system(f"open {'/Applications/Calendar.app'}")

			else:
				webbrowser.open("https://calendar.yandex.ru/")

		elif 'открой карту' in zadanie:
			self.talk("Открываю карту")

			if self.operation_system == 'Darwin':
				os.system(f"open {'/Applications/Maps.app'}")
			else:
				webbrowser.open("https://map.yandex.ru/")


		elif 'включи диктофон' in zadanie:
			self.talk("Включаю диктофон")

			if self.operation_system == 'Darwin':
				os.system(f"open {'/Applications/VoiceMemos.app'}")
			else:
				self.talk("Данная функция на вашей операционной системе не поддерживается")

		elif 'включи музыку' in zadanie:
			self.talk("Включаю музыку")

			if self.operation_system == 'Darwin':
				os.system(f"open {'/Applications/iTunes.app'}")
			else:
				self.talk("Данная функция на вашей операционной системе не поддерживается")
	
		elif 'найди в интернете' in zadanie:
			self.talk('Что мне найти?')
			r = sr.Recognizer()
			with sr.Microphone() as source:
				# r.pause_threshold = 0
				r.adjust_for_ambient_noise(source, 2)
				audio = r.listen(source)
				url = r.recognize_google(audio, language="ru-RU").lower()
				self.talk('Вот что я смогла найти.')
			weburl="https://yandex.ru/search/?text=" + url
			webbrowser.get().open(weburl)
		else:
			message_trans = (self.translator.translate(text=zadanie, dest='en')).text
			ru_result = (self.translator.translate(text=self.chat.respond(message_trans), dest='ru')).text
			self.talk(ru_result)