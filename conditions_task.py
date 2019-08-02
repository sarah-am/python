

first_number = input("Enter the first number:  ")
second_number = input("Enter the second number:  ")
operation = raw_input("Pick an operation (+, -, *, /):  ")

answer = ""

if type(first_number and second_number) == (int or float):
	if operation == "+":
		answer = float(first_number + second_number)
		print("The answer is " + str(answer))
	elif operation == "-":
		answer = float(first_number - second_number)
		print("The answer is " + str(answer))
	elif operation == "*":
		answer = float(first_number * second_number)
		print("The answer is " + str(answer))
	elif operation == "/":
		answer = float(first_number) / second_number
		print("The answer is " + str(answer))
	else: 
		print("The operation is not valid")

else:
	print("Numbers are invalid")

