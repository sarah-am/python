import datetime

class Employee:
	def __init__(self, name, age, salary, employment_date):
		self.name = str(name)
		self.age = int(age)
		self.salary = int(salary)
		self.employment_date = int(employment_date)

	def get_working_years(self):
		return (datetime.date.today().year - self.employment_date)

	def __str__(self):
		return """\nName: {}, Age: {}, Salary: {}, Working years: {}""".format(self.name, self.age, self.salary, self.get_working_years())

class Manager(Employee):
	def __init__(self, name, age, salary, employment_date, bonus_percentage):
		Employee.__init__(self, name, age, salary, employment_date)
		self.bonus_percentage = int(bonus_percentage)
		
	def get_bonus(self):
		return self.bonus_percentage * self.salary

	def __str__(self):
		return """\nName: {}, Age: {}, Salary: {}, Working years: {}, Bonus: {}""".format(self.name, self.age, self.salary, Employee.get_working_years(self), self.get_bonus())

employees = []
managers = []

def add_employee():
	name = input("Enter name: ")
	age = input("Enter age: ")
	salary = input("Enter salary: ")
	employment_date = input("Date of employment (year): ")
	employee = Employee(name, age, salary, employment_date)

	if employee not in employees:
		employees.append(employee)
	else:
		print("Employee already exists")

	print("Employee added succesfully")

def add_manager():
	name = input("Name: ")
	age = input("Age: ")
	salary = input("Salary: ")
	employment_date = input("Date of employment (year): ")
	bonus_percentage = input("Bonus (%): ")
	manager = Manager(name, age, salary, employment_date, bonus_percentage)

	if manager not in managers:
		managers.append(manager)
	else:
		print("Manager already exists")

	print("Manager added succesfully")

while True:
	print("""\nWelcome to HR Pro 2019 \nChoose an action to do:\n1. Show employees\n2. Show managers\n3. Add an employee\n4. Add a manager\n5. Exit""")

	x = int(input("\nWhat would you like to do?  "))

	if x == 1:
		if len(employees) != 0:
			print("\nEmployees:")
			for employee in employees:
				print(employee.__str__())
		else:
			print("Please add an employee")
	elif x == 2:
		if len(managers) != 0:
			print("\nManagers:")
			for manager in managers:
				print(manager.__str__())
		else:
			print("Please add a manager")
	elif x == 3:
		add_employee()
	elif x == 4:
		add_manager()
	elif x == 5:
		break