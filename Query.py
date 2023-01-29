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
		M = call.message
		bot.edit_message_text(chat_id = M.chat.id, message_id = M.id, text = phrases.GetPhrase("Information"), reply_markup = BotKeyboards.keyboards("InfoMenu", call.from_user.id), disable_web_page_preview=True)
	
	elif call.data == "welcome":
		M = call.message
		out = phrases.GetPhrase("Welcome") + str("\n") + str("\n")
		z = DatabaseCommands.get_user(call.from_user.id)
		if z[3] == 0:
			out = out + "\n\U0001F515*Уведомления отключены*"
		bot.edit_message_text(chat_id = M.chat.id, message_id = M.id, text = out, reply_markup = BotKeyboards.keyboards("Menu", call.from_user.id), disable_web_page_preview=True)
	
	elif call.data == "olympiadsinfo":
		M = call.message
		bot.edit_message_text(chat_id = M.chat.id, message_id = M.id, text = phrases.GetPhrase("InfoOlympiads"), reply_markup = BotKeyboards.keyboards("InfoOlympiads", call.from_user.id), disable_web_page_preview=True)
	
	elif call.data == "settings":
		M = call.message
		bot.edit_message_text(chat_id = M.chat.id, message_id = M.id, text = phrases.GetPhrase("Settings"), reply_markup = BotKeyboards.keyboards("Settings", call.from_user.id), disable_web_page_preview=True)
	
	elif call.data == "subjects":
		M = call.message
		z = DatabaseCommands.get_user(call.from_user.id)
		subs = [0]
		for j in range(1, 15):
			if ((1<<j)&z[2]) > 0:
				subs.append(1)
			else:
				subs.append(0)											
		bot.edit_message_text(chat_id = M.chat.id, message_id = M.id, text = phrases.GetPhrase("Subjects"), reply_markup = BotKeyboards.keyboards("Subjects", subs), disable_web_page_preview=True)		
	
	elif call.data == "grades":
		M = call.message
		z = DatabaseCommands.get_user(call.from_user.id)
		subs = [0]
		for j in range(1, 12):
			if ((1<<j)&z[1]) > 0:
				subs.append(1)
			else:
				subs.append(0)		
		bot.edit_message_text(chat_id = M.chat.id, message_id = M.id, text = phrases.GetPhrase("Grades"), reply_markup = BotKeyboards.keyboards("Grades", subs), disable_web_page_preview=True)
	
	elif call.data == "notifications":
		M = call.message
		z = DatabaseCommands.get_user(call.from_user.id)
		bot.edit_message_text(chat_id = M.chat.id, message_id = M.id, text = phrases.GetPhrase("Notifications"), reply_markup = BotKeyboards.keyboards("Notifications", z[3]), disable_web_page_preview=True)
	
	elif call.data == "olympiads":
		M = call.message
		response = "Ближайшие события:\n\n"
		olympiads = DatabaseCommands.get_all_olympiads(call.from_user.id)
		indexx = 0
		now_date = str(datetime.now().day) + "." + str(datetime.now().month) + "." + str(datetime.now().year)
		tosortarr = []
		for olympiad in olympiads:
			if distance(now_date, olympiad[1]) < 60:
				indexx += 1
				tosortarr.append([distance(now_date, olympiad[1]), olympiad[1] + " " + DatabaseCommands.get_name(olympiad[0]) + "\n\n"])
		if len(tosortarr) == 0:
			response = "*В ближайшее время нету олимпиад* \U0001F622"
		tosortarr.sort()
		for x in tosortarr:
			response += x[1]
		bot.edit_message_text(chat_id = M.chat.id, message_id = M.id, text = phrases.GetPhrase("DatesOlympiads") + "\n\n" + response, reply_markup = BotKeyboards.keyboards("DatesOlympiads", call.from_user.id), disable_web_page_preview=True)
	
	elif call.data.find("activate") != -1:
		que = call.data.split("|")
		M = call.message
		z = DatabaseCommands.get_user(call.from_user.id)
		if que[1] == '1':		    
			newvalue = z[2] ^ (1<<(int(que[2])))
			DatabaseCommands.upd_user(call.from_user.id, "subjects", newvalue)
			z = DatabaseCommands.get_user(call.from_user.id)
			subs = [0]
			for j in range(1, 15):
				if ((1<<j)&z[2]) > 0:
					subs.append(1)
				else:
					subs.append(0)											
			bot.edit_message_text(chat_id = M.chat.id, message_id = M.id, text = phrases.GetPhrase("Subjects"), reply_markup = BotKeyboards.keyboards("Subjects", subs), disable_web_page_preview=True)				
		elif que[1] == '2':
			newvalue = z[1] ^ (1<<(int(que[2])))
			DatabaseCommands.upd_user(call.from_user.id, "grades", newvalue)
			z = DatabaseCommands.get_user(call.from_user.id)
			subs = [0]
			for j in range(1, 12):
				if ((1<<j)&z[1]) > 0:
					subs.append(1)
				else:
					subs.append(0)											
			bot.edit_message_text(chat_id = M.chat.id, message_id = M.id, text = phrases.GetPhrase("Grades"), reply_markup = BotKeyboards.keyboards("Grades", subs), disable_web_page_preview=True)				
		elif que[1] == '3':
			newvalue = z[3]^1
			DatabaseCommands.upd_user(call.from_user.id, "notify", newvalue)
			bot.edit_message_text(chat_id = M.chat.id, message_id = M.id, text = phrases.GetPhrase("Notifications"), reply_markup = BotKeyboards.keyboards("Notifications", newvalue), disable_web_page_preview=True)
