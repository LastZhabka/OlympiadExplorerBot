# -*- coding: cp1251 -*-
import sys
from pathlib import Path
path = Path(Path.cwd(), "AdditionalApps");
MyPath = str(path)
sys.path.insert(1, MyPath)
import DatabaseCommands
from dateCalculator import distance
from SecretData import APIKey
import SecretData
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

def interact (message):
					
	if message.chat.type == 'private':
		if (message.from_user.id) in SecretData.adminslist:
			text = message.text
			if (text[:3] == 'add'):
				text = text[4:]
				data = text.split("~")
				DatabaseCommands.add_olympiad(data[0], data[2], data[3], data[1])
			elif (text[:3] == 'dda'):
				text = text[4:]
				data = text.split("~")
				DatabaseCommands.add_olympiad(data[0], data[1], data[2])
			elif(text[:3] == 'del'):
				text = text[4:]
				data = text.split("~")
				DatabaseCommands.del_olympiad(data[0], data[1])
			elif(text[:3] == 'get'):
				Database = sql.connect('test.db')
				cursor = Database.cursor()
				cursor.execute("SELECT * FROM 'olympiads'")
				olympiads = cursor.fetchall()
				response = "Olympiads:\n\n" 
				for olympiad in olympiads:															    	
					response += str(olympiad[0]) + " " + str(olympiad[1]) + " " + str(olympiad[2]) + " " + str(olympiad[3]) + "\n\n"
				bot.send_message(message.chat.id, response)			
			elif(text[:3] == 'teg'):
				Database = sql.connect('test.db')
				cursor = Database.cursor()
				cursor.execute("SELECT * FROM 'olympiadsinformation'")
				olympiads = cursor.fetchall()
				response = "Olympiads:\n\n" 
				for olympiad in olympiads:															    	
					response += str(olympiad[0]) + " " + str(olympiad[1]) + " " + str(olympiad[2]) + "\n\n"
				bot.send_message(message.chat.id, response)			
			elif(text[:3] == 'sta'):
				Database = sql.connect('test.db')
				cursor = Database.cursor()
				cursor.execute("SELECT * FROM 'users'")
				response = str(len(curs.fetchall()))
				bot.send_message(message.chat.id, response)
			elif(text[:3] == 'tim'):
				now_date = str(datetime.now().day) + "." + str(datetime.now().month) + "." + str(datetime.now().year)
				bot.send_message(message.chat.id, now_date)
			elif(text[:4] == 'send'):
			    mess = text[5:]
			    Database = sql.connect('test.db')
			    cursor = Database.cursor()
			    cursor.execute("SELECT * FROM 'users'")
			    users = cursor.fetchall()
			    for user in users:
			    	try:
			    		bot.send_message(user[0], mess)
			    	except:
			    		axe = 0
			else:
				welcome(message)
		else:
			welcome(message)
	
#if message.from_user.id == 418299796: