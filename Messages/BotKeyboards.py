# -*- coding: cp1251 -*-
from telebot import types
import os

def CreateButton(A, B):
	return types.InlineKeyboardButton(A, callback_data=B)

def keyboards(text, activated):
	keyboard = types.InlineKeyboardMarkup()
	if text == "Menu":
		keyboard.add(CreateButton("\U0001F9E0Информация", 'info'))
		keyboard.add(CreateButton("\U000023F1События", 'olympiads'))
		keyboard.add(CreateButton("\U00002699Настройки", 'settings'))
	if text == "InfoMenu":
		keyboard.add(CreateButton("\U0001F324Олимпиады", 'olympiadsinfo'))
		keyboard.add(CreateButton("\U000021A9Назад", 'welcome'))
	if text == "Settings":
		keyboard.add(CreateButton("\U0001F4D3Предметы", 'subjects'))
		keyboard.add(CreateButton("\U0001F3EBКлассы", 'grades'))
		keyboard.add(CreateButton("\U0001F514Уведомления", 'notifications'))
		keyboard.add(CreateButton("\U000021A9Назад", 'welcome'))
	if text == "InfoOlympiads":
		keyboard.add(CreateButton("\U000021A9Назад", 'info'))	
	if text == "Subjects":
		subjects = ["Null", "Математика", "Физика", "Биология", "Химия","Информатика", "География","Английский язык", "История","Казахский язык (Я2)", "Казахский язык и литература","Немецкий язык", "Основы права","Русский язык (Я2)", "Русский язык и литература"]
		emojies = ["\U0000274C", "\U00002705"]
		for j in range(1, 15, 2):
			keyboard.row(CreateButton(emojies[activated[j]] + subjects[j], "activate|1|" + str(j)),CreateButton(emojies[activated[j + 1]] + subjects[j + 1], "activate|1|" + str(j + 1))) 
		keyboard.add(CreateButton("\U000021A9Назад", 'settings'))	
	if text == "Grades":
		emojies = ["\U0000274C", "\U00002705"]
		for j in range(7, 11, 2):
			keyboard.row(CreateButton(emojies[activated[j]] + str(j), "activate|2|" + str(j)),CreateButton(emojies[activated[j + 1]] + str(j + 1), "activate|2|" + str(j + 1))) 
		keyboard.add(CreateButton(emojies[activated[11]] + "11", "activate|2|11"))
		keyboard.add(CreateButton("\U000021A9Назад", 'settings'))	
	if text == "Notifications":
		respon = ["\U0001F515Уведомления выключены", "\U0001F514Уведомления включены"]
		keyboard.add(CreateButton(respon[activated], "activate|3|1"))
		keyboard.add(CreateButton("\U000021A9Назад", 'settings'))	
	elif text == "DatesOlympiads":
		keyboard.add(CreateButton("\U000021A9Назад", 'welcome'))					
	return keyboard
	