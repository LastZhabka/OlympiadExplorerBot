# -*- coding: cp1251 -*-
from Interaction import interact
from Welcome import welcome
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
import SecretData
import sqlite3 as sql
from sqlite3 import Error
import telebot
from telebot import types
from threading import Thread
from time import sleep
from datetime import datetime 
import os
path = Path(Path.cwd(), "Messages");
MyPath = str(path)
sys.path.insert(1, MyPath)
import BotKeyboards
import phrases
from Query import query


DatabaseCommands.init()


#DatabaseCommands.add_olympiad_to_Database(1, "Международная Жаутыковская олимпиада", "")
#DatabaseCommands.add_olympiad_to_Database(2, "Районный этап Республиканской олимпиады", "")
#DatabaseCommands.add_olympiad_to_Database(3, "Областной этап Республиканской олимпиады", "")
#DatabaseCommands.add_olympiad_to_Database(4, "Республиканская олимпиада", "")
#DatabaseCommands.add_olympiad(1, 128, 2, "29.01.2023")
#cc
bot = telebot.TeleBot(APIKey(), parse_mode="Markdown")



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	welcome(message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	interact(message)

@bot.callback_query_handler(func = lambda call: True)
def callHandler1(call):
	query(call)

def check_reminders():
	os.system('python3 Reminders.py')	


Reminding = Thread(target=check_reminders)
Reminding.start()


bot.infinity_polling()