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


th = Thread(target=check_reminders)
th.start()


bot.infinity_polling()