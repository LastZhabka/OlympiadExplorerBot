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