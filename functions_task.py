from datetime import date

# input("Please provide your date of birth (yyyy/mm/dd):  ")

print("Please provide your date of birth, as follows: ")

year = int(input("year:  "))
month = int(input("month:  "))
day = int(input("day:  "))

today = date.today()
user_birthdate = date(year, month, day)

def check_birthdate(year, month, day):

	if user_birthdate >= today:
		return False
	else:
		return True
	
def calculate_age(year, month, day):

 	# year = today.year - user_birthdate.year
 	# month = today.month - user_birthdate.month
 	# day = today.day - user_birthdate.day

 	age = today - user_birthdate

 	print("You are "+ str(age.year) + " years " + str(age.month) + " months and " + str(age.day) + " days old")

if check_birthdate(year, month, day) == True:
	calculate_age(year, month, day)
else:
	print("Birthdate is invalid")


# Returns False if the given birthdate is in the future and True if it was in the past.
# Calculates the age of the user.
# # Prints a message to the user with his age in years, months, and days.
# Ask the user for his birthdate (year, month, day)



# class date.date
