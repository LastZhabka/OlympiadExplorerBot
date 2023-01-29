# -*- coding: cp1251 -*-
import sys
from pathlib import Path
path = Path(Path.cwd(), "AdditionalApps");
MyPath = str(path)
sys.path.insert(1, MyPath)
import DatabaseCommands
from dateCalculator import distance
from SecretData import APIKey
import sqlite3 as sql
from sqlite3 import Error
import telebot
from telebot import types
from threading import Thread
from time import sleep
from datetime import datetime 
import os
from Welcome import welcome
path = Path(Path.cwd(), "Messages");
MyPath = str(path)
sys.path.insert(1, MyPath)
import BotKeyboards
import phrases

bot = telebot.TeleBot(APIKey(), parse_mode="Markdown")

def query(call):					
	if call.data == "info":
		UserMessage = call.message
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Information"), reply_markup = BotKeyboards.keyboards("InfoMenu", call.from_user.id), disable_web_page_preview=True)
	
	elif call.data == "welcome":
		UserMessage = call.message
		out = phrases.GetPhrase("Welcome") + str("\n") + str("\n")
		z = DatabaseCommands.get_user(call.from_user.id)
		if z[3] == 0:
			out = out + "\n\U0001F515*Уведомления отключены*"
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = out, reply_markup = BotKeyboards.keyboards("Menu", call.from_user.id), disable_web_page_preview=True)
	
	elif call.data == "olympiadsinfo":
		UserMessage = call.message
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("InfoOlympiads"), reply_markup = BotKeyboards.keyboards("InfoOlympiads", call.from_user.id), disable_web_page_preview=True)
	
	elif call.data == "settings":
		UserMessage = call.message
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Settings"), reply_markup = BotKeyboards.keyboards("Settings", call.from_user.id), disable_web_page_preview=True)
	
	elif call.data == "subjects":
		UserMessage = call.message
		z = DatabaseCommands.get_user(call.from_user.id)
		subjectsMask = [0]
		for j in range(1, 15):
			if ((1<<j)&z[2]) > 0:
				subjectsMask.append(1)
			else:
				subjectsMask.append(0)											
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Subjects"), reply_markup = BotKeyboards.keyboards("Subjects", subjectsMask), disable_web_page_preview=True)		
	
	elif call.data == "grades":
		UserMessage = call.message
		z = DatabaseCommands.get_user(call.from_user.id)
		gradesMask = [0]
		for j in range(1, 12):
			if ((1<<j)&z[1]) > 0:
				gradesMask.append(1)
			else:
				gradesMask.append(0)		
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Grades"), reply_markup = BotKeyboards.keyboards("Grades", gradesMask), disable_web_page_preview=True)
	
	elif call.data == "notifications":
		UserMessage = call.message
		z = DatabaseCommands.get_user(call.from_user.id)
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Notifications"), reply_markup = BotKeyboards.keyboards("Notifications", z[3]), disable_web_page_preview=True)
	
	elif call.data == "olympiads":
		UserMessage = call.message
		response = "Ближайшие события:\n\n"
		olympiads = DatabaseCommands.get_all_olympiads(call.from_user.id)
		now_date = str(datetime.now().day) + "." + str(datetime.now().month) + "." + str(datetime.now().year)
		DatesAndOlympiads = []
		for olympiad in olympiads:
			if distance(now_date, olympiad[1]) < 60:
				DatesAndOlympiads.append([distance(now_date, olympiad[1]), olympiad[1] + " " + DatabaseCommands.get_name(olympiad[0]) + "\n\n"])
		if len(DatesAndOlympiads) == 0:
			response = "*В ближайшее время нету событий* \U0001F622"
		DatesAndOlympiads.sort()
		for x in DatesAndOlympiads:
			response += x[1]
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("DatesOlympiads") + "\n\n" + response, reply_markup = BotKeyboards.keyboards("DatesOlympiads", call.from_user.id), disable_web_page_preview=True)
	
	elif call.data.find("activate") != -1:
		que = call.data.split("|")
		UserMessage = call.message
		user = DatabaseCommands.get_user(call.from_user.id)
		if que[1] == '1':		    
			newvalue = user[2] ^ (1<<(int(que[2])))
			DatabaseCommands.upd_user(call.from_user.id, "subjects", newvalue)
			user = DatabaseCommands.get_user(call.from_user.id)
			subjects = [0]
			for j in range(1, 15):
				if ((1<<j)&user[2]) > 0:
					subjects.append(1)
				else:
					subjects.append(0)											
			bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Subjects"), reply_markup = BotKeyboards.keyboards("Subjects", subjects), disable_web_page_preview=True)				
		elif que[1] == '2':
			newvalue = user[1] ^ (1<<(int(que[2])))
			DatabaseCommands.upd_user(call.from_user.id, "grades", newvalue)
			user = DatabaseCommands.get_user(call.from_user.id)
			grades = [0]
			for j in range(1, 12):
				if ((1<<j)&user[1]) > 0:
					grades.append(1)
				else:
					grades.append(0)											
			bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Grades"), reply_markup = BotKeyboards.keyboards("Grades", grades), disable_web_page_preview=True)				
		elif que[1] == '3':
			newvalue = user[3]^1
			DatabaseCommands.upd_user(call.from_user.id, "notify", newvalue)
			bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Notifications"), reply_markup = BotKeyboards.keyboards("Notifications", newvalue), disable_web_page_preview=True)		