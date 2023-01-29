from datetime import datetime

def distance(date1, date2):
	date3 = date1.split(".")
	date4 = date2.split(".")
	first_date = datetime(int(date3[2]), int(date3[1]), int(date3[0]))
	second_date = datetime(int(date4[2]), int(date4[1]), int(date4[0]))
	return (second_date - first_date).days
