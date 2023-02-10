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
	group = False
	Prefix = ""
	text = call.data
	userID = call.from_user.id
	if text.find("Group") != -1:
		text = text[5:]
		Prefix = "Group"
		group = True
		userID = call.message.chat.id
	if group == True and bot.get_chat_member(call.message.chat.id, call.from_user.id).status == 'member':
		bot.answer_callback_query(call.id, "Только админы могут изменять настройки в группе.", show_alert=True)
		return
	if text == "info":
		UserMessage = call.message
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Information"), reply_markup = BotKeyboards.keyboards(Prefix + "InfoMenu", userID), disable_web_page_preview=True)
	
	elif text == "welcome":
		UserMessage = call.message
		out = phrases.GetPhrase("Welcome") + str("\n") + str("\n")
		z = DatabaseCommands.get_user(userID)
		if z[3] == 0:
			out = out + "\n\U0001F515*Уведомления отключены*"
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = out, reply_markup = BotKeyboards.keyboards(Prefix + "Menu", userID), disable_web_page_preview=True)
	
	elif text == "olympiadsinfo":
		UserMessage = call.message
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("InfoOlympiads"), reply_markup = BotKeyboards.keyboards(Prefix + "InfoOlympiads", userID), disable_web_page_preview=True)
	
	elif text == "settings":
		UserMessage = call.message
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Settings"), reply_markup = BotKeyboards.keyboards(Prefix + "Settings", userID), disable_web_page_preview=True)
	
	elif text == "subjects":
		UserMessage = call.message
		z = DatabaseCommands.get_user(userID)
		subjectsMask = [0]
		for j in range(1, 15):
			if ((1<<j)&z[2]) > 0:
				subjectsMask.append(1)
			else:
				subjectsMask.append(0)											
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Subjects"), reply_markup = BotKeyboards.keyboards(Prefix + "Subjects", subjectsMask), disable_web_page_preview=True)		
	
	elif text == "grades":
		UserMessage = call.message
		z = DatabaseCommands.get_user(userID)
		gradesMask = [0]
		for j in range(1, 12):
			if ((1<<j)&z[1]) > 0:
				gradesMask.append(1)
			else:
				gradesMask.append(0)		
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Grades"), reply_markup = BotKeyboards.keyboards(Prefix + "Grades", gradesMask), disable_web_page_preview=True)
	
	elif text == "notifications":
		UserMessage = call.message
		z = DatabaseCommands.get_user(userID)
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Notifications"), reply_markup = BotKeyboards.keyboards(Prefix + "Notifications", z[3]), disable_web_page_preview=True)
	
	elif text == "olympiads":
		UserMessage = call.message
		response = "Ближайшие события:\n\n"
		olympiads = DatabaseCommands.get_all_olympiads(userID)
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
		bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("DatesOlympiads") + "\n\n" + response, reply_markup = BotKeyboards.keyboards(Prefix + "DatesOlympiads", userID), disable_web_page_preview=True)
	
	elif text.find("activate") != -1:
		que = text.split("|")
		UserMessage = call.message
		user = DatabaseCommands.get_user(userID)
		if que[1] == '1':		    
			newvalue = user[2] ^ (1<<(int(que[2])))
			DatabaseCommands.upd_user(userID, "subjects", newvalue)
			user = DatabaseCommands.get_user(userID)
			subjects = [0]
			for j in range(1, 15):
				if ((1<<j)&user[2]) > 0:
					subjects.append(1)
				else:
					subjects.append(0)											
			bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Subjects"), reply_markup = BotKeyboards.keyboards(Prefix + "Subjects", subjects), disable_web_page_preview=True)				
		elif que[1] == '2':
			newvalue = user[1] ^ (1<<(int(que[2])))
			DatabaseCommands.upd_user(userID, "grades", newvalue)
			user = DatabaseCommands.get_user(userID)
			grades = [0]
			for j in range(1, 12):
				if ((1<<j)&user[1]) > 0:
					grades.append(1)
				else:
					grades.append(0)											
			bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Grades"), reply_markup = BotKeyboards.keyboards(Prefix + "Grades", grades), disable_web_page_preview=True)				
		elif que[1] == '3':
			newvalue = user[3]^1
			DatabaseCommands.upd_user(userID, "notify", newvalue)
			bot.edit_message_text(chat_id = UserMessage.chat.id, message_id = UserMessage.id, text = phrases.GetPhrase("Notifications"), reply_markup = BotKeyboards.keyboards(Prefix + "Notifications", newvalue), disable_web_page_preview=True)		