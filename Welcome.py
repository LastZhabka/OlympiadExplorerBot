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


def welcome(message):
	if message.chat.type == "private":
		if DatabaseCommands.check_user(message.from_user.id) == 0:
			DatabaseCommands.add_user(message.from_user.id)
		try:
			out = phrases.GetPhrase("Welcome") + str("\n") + str("\n")
			z = DatabaseCommands.get_user(message.from_user.id)
			if z[3] == 0:
				out = out + "\n\U0001F515*Уведомления отключены*"
			bot.send_message(message.chat.id, out, reply_markup=BotKeyboards.keyboards("Menu", message.from_user.id), disable_web_page_preview=True)
		except:
			print("Error")
	elif message.chat.type == "group" or message.chat.type == "supergroup":		
		user = (bot.get_chat_member(message.chat.id, message.from_user.id))
		if user.status != "member":
			if DatabaseCommands.check_user(message.chat.id) == 0:
				DatabaseCommands.add_user(message.chat.id)
			try:
				out = phrases.GetPhrase("Welcome") + str("\n") + str("\n")
				z = DatabaseCommands.get_user(message.chat.id)
				if z[3] == 0:
					out = out + "\n\U0001F515*Уведомления отключены*"
				bot.send_message(message.chat.id, out, reply_markup=BotKeyboards.keyboards("GroupMenu", message.from_user.id), disable_web_page_preview=True)
			except:
				print("Error")