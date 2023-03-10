# -*- coding: cp1251 -*-
from telebot import types
import os

def CreateButton(A, B):
	return types.InlineKeyboardButton(A, callback_data=B)

def keyboards(text, activated):
	keyboard = types.InlineKeyboardMarkup()
	Prefix = ""
	if len(text) >= 5 and text[0:5] == "Group":
		Prefix = (text[0:5])
		text = text[5:]
	if text == "Menu":
		keyboard.add(CreateButton("\U0001F9E0??????????", Prefix + 'info'))
		keyboard.add(CreateButton("\U000023F1???????", Prefix + 'olympiads'))
		keyboard.add(CreateButton("\U00002699?????????", Prefix + 'settings'))
	if text == "InfoMenu":
		keyboard.add(CreateButton("\U0001F324?????????", Prefix + 'olympiadsinfo'))
		keyboard.add(CreateButton("\U000021A9?????", Prefix + 'welcome'))
	if text == "Settings":
		keyboard.add(CreateButton("\U0001F4D3????????", Prefix + 'subjects'))
		keyboard.add(CreateButton("\U0001F3EB??????", Prefix + 'grades'))
		keyboard.add(CreateButton("\U0001F514???????????", Prefix + 'notifications'))
		keyboard.add(CreateButton("\U000021A9?????", Prefix + 'welcome'))
	if text == "InfoOlympiads":
		keyboard.add(CreateButton("\U000021A9?????", Prefix + 'info'))	
	if text == "Subjects":
		subjects = ["Null", "??????????", "??????", "????????", "?????","???????????", "?????????","?????????? ????", "???????","????????? ???? (?2)", "????????? ???? ? ??????????","???????? ????", "?????? ?????","??????? ???? (?2)", "??????? ???? ? ??????????"]
		emojies = ["\U0000274C", "\U00002705"]
		for j in range(1, 15, 2):
			keyboard.row(CreateButton(emojies[activated[j]] + subjects[j], Prefix + "activate|1|" + str(j)),CreateButton(emojies[activated[j + 1]] + subjects[j + 1], Prefix + "activate|1|" + str(j + 1))) 
		keyboard.add(CreateButton("\U000021A9?????", Prefix + 'settings'))	
	if text == "Grades":
		emojies = ["\U0000274C", "\U00002705"]
		for j in range(7, 11, 2):
			keyboard.row(CreateButton(emojies[activated[j]] + str(j), Prefix + "activate|2|" + str(j)),CreateButton(emojies[activated[j + 1]] + str(j + 1), Prefix + "activate|2|" + str(j + 1))) 
		keyboard.add(CreateButton(emojies[activated[11]] + "11", Prefix + "activate|2|11"))
		keyboard.add(CreateButton(emojies[activated[12]] + "??????? ????????????(ACM)", Prefix + "activate|2|12"))
		keyboard.add(CreateButton("\U000021A9?????", Prefix + 'settings'))	
	if text == "Notifications":
		respon = ["\U0001F515??????????? ?????????", "\U0001F514??????????? ????????"]
		keyboard.add(CreateButton(respon[activated], Prefix + "activate|3|1"))
		keyboard.add(CreateButton("\U000021A9?????", Prefix + 'settings'))	
	elif text == "DatesOlympiads":
		keyboard.add(CreateButton("\U000021A9?????", Prefix + 'welcome'))					
	return keyboard