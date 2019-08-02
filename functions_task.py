from dateutil.relativedelta import *
from datetime import date

print("\nPlease provide your date of birth, as follows: ")

year = int(input(" - Year:  "))
month = int(input(" - Month:  "))
day = int(input(" - Day:  "))

today = date.today()
user_birthdate = date(year, month, day)

def check_birthdate(year, month, day):

	if user_birthdate >= today:
		return False
	else:
		return True
	
def calculate_age(year, month, day):

 	age = relativedelta(today, user_birthdate)

 	print("\nWow! You are "+ str(age.years) + " years, " + str(age.months) + " months and " + str(age.days) + " days old. =O\n")

if check_birthdate(year, month, day) == True:
	calculate_age(year, month, day)
else:
	print("Birthdate is invalid")