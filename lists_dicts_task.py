skills = ["python", "sleeping", "c++", "driving", "javascript", "procrastination",]
cv = {}

print("\nWelcome to the special recruitment program! Please fill out the below:\n")
cv["name"] = raw_input("Name:  ")
cv["age"] = input("Age:  ")
cv["experience"] = input("Years of experience:  ")
cv["skills"] = []

skills_cap = [i.capitalize() for i in skills]

print("\nSkills:")

skill_number = 1
for skill in skills:
	print("{}) {}".format(skill_number, skills_cap[(skill_number-1)]))
	skill_number += 1
print("")

# OR ==> print('\n'.join('{}) {}'.format(*i) for i in enumerate(skills_cap, 1)) + '\n')

skill_1 = input("Choose a skill from the above (number):  ")
skill_2 = input("Pick another skill (number): ")

cv["skills"] = [skills[(skill_1 - 1)], skills[(skill_2 - 1)]]

def check_criteria(cv):
	if (cv["age"] >= 22 and cv["age"] <= 45) and (cv["experience"] >= 2) and ("sleeping" in cv["skills"]):
		print("\nCongratulations, {}! You have been accepted.\n".format(cv["name"]))
	else:
		print("\nUnfortunately, {}, you don't fit our criteria.\n".format(cv["name"]))

check_criteria(cv)