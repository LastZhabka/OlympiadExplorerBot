# -*- coding: cp1251 -*-
import sqlite3 as sql
from sqlite3 import Error

def out_database():
	DB = sql.connect('test.db')
	curs = DB.cursor()
	curs.execute("SELECT * FROM 'olympiads'")
	xxx = curs.fetchall()
	for i in xxx:
		print(i)	

def add_olympiad_to_Database(id, name, info):
	DB = sql.connect('test.db')
	param = str(id) + ",'" + name + "','" + info + "'" 
	DB.cursor().execute("INSERT INTO 'olympiadsinformation' VALUES(" + param + ")")
	DB.commit()

def add_olympiad(id, grade, subject, datentime):
	DB = sql.connect('test.db')
	param = str(id) + ",'" + str(datentime) + "'," + str(grade) + "," + str(subject);
	#print param
	DB.cursor().execute("INSERT INTO 'olympiads' VALUES(" + param + ")")
	DB.commit()
def upd_olympiad(id, param, val):
	DB = sql.connect('test.db')
	DB.cursor().execute("UPDATE 'olympiads' SET '" + param + "'=\"" + str(val) + "\" WHERE olympiad_id = " + str(id))
	DB.commit()
def del_olympiad(id, date):
	DB = sql.connect('test.db')
	DB.cursor().execute("DELETE FROM 'olympiads' WHERE olympiad_id = " + str(id) + " AND " + "DateNTime = '" + date + "'")
	DB.commit()

#	Initialization of all tables in database
def init():
	DB = sql.connect('test.db')
	DB.cursor().execute("CREATE TABLE IF NOT EXISTS 'users' (user_id INTEGER, grades INTEGER, subjects INTEGER, notify INTEGER)")
	DB.cursor().execute("CREATE TABLE IF NOT EXISTS 'olympiads' (olympiad_id INTEGER, DateNTime varchar(256), grades INTEGER, subjects INTEGER)")
	DB.cursor().execute("CREATE TABLE IF NOT EXISTS 'olympiadsinformation' (olympiad_id INTEGER, name varchar(256), information varchar(2048))")
	DB.commit()
	'''
	add_olympiad_to_Database(1, "Международная Жаутыковская олимпиада", "")
	add_olympiad_to_Database(2, "Районный этап Республиканской олимпиады", "")
	add_olympiad_to_Database(3, "Областной этап Республиканской олимпиады", "")
	add_olympiad_to_Database(4, "Олимпиада Высшая Проба", "")
	add_olympiad_to_Database(5, "Олимпиада Фоксфорд", "")
	add_olympiad_to_Database(6, "Beyon Olympiad", "")
	add_olympiad_to_Database(7, "Олимпиада СПБГУ", "")
	add_olympiad_to_Database(8, "Олимпиада Покори Воробьевы Горы", "")
	add_olympiad_to_Database(9, "British Biology Olympiad", "")
	add_olympiad_to_Database(10, "Республиканская олимпиада", "")
	add_olympiad_to_Database(11, "Турнир городов", "")
	add_olympiad_to_Database(12, "Городская Жаутыковская олимпиада", "")
	add_olympiad_to_Database(13, "Олимпиада Эйлера", "")
	add_olympiad_to_Database(14, "Московская Олимпиада Школьников", "")
	add_olympiad_to_Database(15, "Всесибирская олимпиада", "")
	add_olympiad_to_Database(16, "Европейская Физическая Олимпиада", "")
	add_olympiad_to_Database(17, "Туймаада", "")
	add_olympiad_to_Database(18, "Городская Жаутыковская олимпиада", "")
	add_olympiad_to_Database(19, "Республиканская олимпиада", "")
	add_olympiad_to_Database(20, "Олимпиада Шаг в будущее", "")
	add_olympiad_to_Database(21, "Innopolis Open", "")
	add_olympiad_to_Database(22, "Открытая олимпиада школьников по программированию", "")
	add_olympiad_to_Database(23, "Олимпиада Технокубок", "")
	add_olympiad_to_Database(24, "VK cup", "")
	add_olympiad_to_Database(25, "Всероссийская Командная Олимпиада Школьников по Программированию", "")
	add_olympiad_to_Database(26, "Открытое Хорватское Состязание по Информатике", "")
	add_olympiad_to_Database(27, "Республиканская Юниорская Олимпиада", "")
	add_olympiad_to_Database(28, "Азиатско-Тихоокеанская Олимпиада по Информатике", "")
	add_olympiad_to_Database(29, "Европейская Юниорская Олимпиада по Информатике", "")
	add_olympiad_to_Database(30, "Европейская Олимпиада по Информатике для Девушек", "")
	add_olympiad_to_Database(31, "Европейская Олимпиада по Математике для девушек", "")
	add_olympiad_to_Database(32, "AITU Open", "")
	add_olympiad_to_Database(33, "IITU Open", "")
	add_olympiad_to_Database(34, "КБТУ Open", "")
	add_olympiad_to_Database(35, "NU Open", "")
	add_olympiad_to_Database(36, "Областной этап Республиканской Юниорской Олимпиады", "")
	add_olympiad_to_Database(37, "Зимние Республиканские сборы", "")
	add_olympiad_to_Database(38, "Весенние Республиканские сборы", "")
	add_olympiad_to_Database(39, "Международная Олимпиада по Информатике(IOI)", "")
	add_olympiad_to_Database(40, "Международная Физическая Олимпиада(IPhO)", "")
	add_olympiad_to_Database(41, "Международная Математическая Олимпиада(IMO)", "")
	add_olympiad_to_Database(42, "Международная Химическая Олимпиада(IChO)", "")
	add_olympiad_to_Database(43, "Международная Географическая Олимпиада(IGeO)", "")
	add_olympiad_to_Database(44, "Международная Географическая Олимпиада(IBO)", "")
	add_olympiad_to_Database(45, "Азиатская Физическая Олимпиада", "")
	add_olympiad_to_Database(46, "Азиатско-Тихоокеанская математическая олимпиада", "")
	add_olympiad_to_Database(47, "Балканская математическая олимпиада среди юниоров", "")
	add_olympiad_to_Database(48, "Международная Менделеевская Олимпиада по химии", "")
	add_olympiad_to_Database(49, "Европейская олимпиада по географии", "")
	add_olympiad_to_Database(50, "Центрально-Европейская олимпиада по информатике", "")
	add_olympiad_to_Database(51, "Азиатская Олимпиада по Биологии", "")
	'''
#	Function that get information about user with user_id = id
def get_user(id):
	DB = sql.connect('test.db')
	curs = DB.cursor()
	curs.execute("SELECT * FROM 'users' WHERE user_id = " + str(id))
	return (curs.fetchall())[0]
#	Function that checks if the user with user_id = id has been added in table 'users'
def check_user(id):
	DB = sql.connect('test.db')
	curs = DB.cursor()
	curs.execute("SELECT * FROM 'users' WHERE user_id = " + str(id))
	return (len(curs.fetchall()) == 1)
# Function that delete user with user_id = id from table 'users'
def del_user(id):
	DB = sql.connect('test.db')
	DB.cursor().execute("DELETE FROM 'users' WHERE user_id = " + str(id))
	DB.commit()
# Function that add user with user_id = id to table 'users'
def add_user(id):
	DB = sql.connect('test.db')
	DB.cursor().execute("INSERT INTO 'users' VALUES(" + str(id) + ", 0, 0, 0)")
	DB.commit()
# Function that update infomation about user with user_id = id in table 'users' 
def upd_user(id, param, val):
	DB = sql.connect('test.db')
	DB.cursor().execute("UPDATE 'users' SET '" + param + "'=\"" + str(val) + "\" WHERE user_id = " + str(id))
	DB.commit()

def get_name(id):
	DB = sql.connect('test.db')
	curs = DB.cursor()
	curs.execute("SELECT * FROM 'olympiadsinformation' WHERE olympiad_id = " + str(id))
	return (curs.fetchall())[0][1]

def get_all_olympiads(id):
	user = get_user(id)
	DB = sql.connect('test.db')
	curs = DB.cursor()
	xxx = []
	curs.execute("SELECT * FROM 'olympiads'")
	yyy = curs.fetchall()
	for ol in yyy:
		if (ol[2]&user[1]) == ol[2] and (ol[3]&user[2]) == ol[3]:
			xxx.append(ol)		
	return xxx	
#out_database() #aab