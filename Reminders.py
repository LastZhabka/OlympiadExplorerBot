# -*- coding: cp1251 -*-
import sys
from pathlib import Path
path = Path(Path.cwd(), "AdditionalApps");
MyPath = str(path)
sys.path.insert(1, MyPath)
import DatabaseCommands
from dateCalculator import distance
path = Path(Path.cwd(), "Messages");
MyPath = str(path)
sys.path.insert(1, MyPath)
import BotKeyboards
import phrases
from SecretData import APIKey
import sqlite3 as sql
from sqlite3 import Error
import telebot
from telebot import types
from threading import Thread
from time import sleep
from datetime import datetime 
import os


bot = telebot.TeleBot(APIKey(), parse_mode="Markdown")

def notify(dist, user, name) :
	try:
		bot.send_message(user[0], phrases.GetPhrase("Notify" + str(dist) + "|«" + name + "»"), disable_web_page_preview=True)
	except:
		print("Error")
		

while 1 == 1 :	
	Database = sql.connect('test.db')
	cursor = Database.cursor()
	cursor.execute("SELECT * FROM 'olympiads'")
	olympiads = cursor.fetchall()
	cursor.execute("SELECT * FROM 'users'")
	users = cursor.fetchall()
	for olympiad in olympiads:
		now_date = str(datetime.now().day) + "." + str(datetime.now().month) + "." + str(datetime.now().year)
		name = DatabaseCommands.get_name(olympiad[0])
		dist = distance(now_date, olympiad[1])
		if dist <= -1:
			del_olympiad(olympiad[0], olympiad[1])
		elif dist == 1 or dist == 3 or dist == 7 or dist == 14 or dist == 30:
			for user in users:
				if (olympiad[2]&user[1]) != olympiad[2]	or (olympiad[3]&user[2]) != olympiad[3] or user[3] == 0:
					continue	
				notify(dist, user, name)	
	sleep(86400)