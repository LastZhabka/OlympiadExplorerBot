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
			a = message.text
			if (a[:3] == 'add'):
				a = a[4:]
				data = a.split("~")
				DatabaseCommands.add_olympiad(data[0], data[2], data[3], data[1])
			elif (a[:3] == 'dda'):
				a = a[4:]
				data = a.split("~")
				DatabaseCommands.add_olympiad(data[0], data[1], data[2])
			elif(a[:3] == 'del'):
				a = a[4:]
				data = a.split("~")
				DatabaseCommands.del_olympiad(data[0], data[1])
			elif(a[:3] == 'get'):
				DB2 = sql.connect('test.db')
				curs = DB2.cursor()
				curs.execute("SELECT * FROM 'olympiads'")
				olympiads = curs.fetchall()
				response = "Olympiads:\n\n" 
				for olympiad in olympiads:															    	
					response += str(olympiad[0]) + " " + str(olympiad[1]) + " " + str(olympiad[2]) + " " + str(olympiad[3]) + "\n\n"
				bot.send_message(message.chat.id, response)			
			elif(a[:3] == 'teg'):
				DB2 = sql.connect('test.db')
				curs = DB2.cursor()
				curs.execute("SELECT * FROM 'olympiadsinformation'")
				olympiads = curs.fetchall()
				response = "Olympiads:\n\n" 
				for olympiad in olympiads:															    	
					response += str(olympiad[0]) + " " + str(olympiad[1]) + " " + str(olympiad[2]) + "\n\n"
				bot.send_message(message.chat.id, response)			
			elif(a[:3] == 'sta'):
				DB2 = sql.connect('test.db')
				curs = DB2.cursor()
				curs.execute("SELECT * FROM 'users'")
				response = str(len(curs.fetchall()))
				bot.send_message(message.chat.id, response)
			elif(a[:3] == 'tim'):
				now_date = str(datetime.now().day) + "." + str(datetime.now().month) + "." + str(datetime.now().year)
				bot.send_message(message.chat.id, now_date)
			elif(a[:4] == 'send'):
			    mess = a[5:]
			    DB2 = sql.connect('test.db')
			    curs = DB2.cursor()
			    curs.execute("SELECT * FROM 'users'")
			    users = curs.fetchall()
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