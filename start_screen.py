def start_screen():
	print("WELCOME TO ANDELA LEARNING MAP TRACKER")
	print("======================================")
	print("PLEASE PICK COMPLETED TASKS")
	print("--------------------------------")
	print("1.Version Control")
	print("2.Agile Methodology")
	print("3.Programming Logic")
	print("4.Object Oriented Programming")
	print("5.Test-Driven Development")
	print("6.Databases")
	print("7.HTTP and Web Services")
	print("8.Front-End Development")
	print("9.Growth Mindset")
	print("10.Relationship Building")
	print("11.Asks Questions")
	print("12.Motivation and Commitment")
	print("13.Adaptability")
	print("14.Seeks Feedback")
	print("15.Speaking to be Understood")
	print("16.Writing Professionally")
	print("17.Git \n")
	print("======================================")
	print("PRESS ENTER TO CONTINUE")

	print("	")

#start_screen()
skills = {
        "Skill 1" : "Version Control",
        "Skill 2" : "Agile Methodology",
        "Skill 3" : "Programming Logic",
        "Skill 4" : "Object Oriented Programming",
        "Skill 5" : "Test-Driven Development",
        "Skill 6" : "Databases",
        "Skill 7" : "HTTP and Web Services",
        "Skill 8" : "Front-End Development",
        "Skill 9" : "Growth Mindset",
        "Skill 10" : "Relationship Building",
        "Skill 11" : "Asks Questions",
        "Skill 12" : "Motivation and Commitment",
        "Skill 13" : "Adaptability",
        "Skill 14" : "Seeks Feedback",
        "Skill 15" : "Speaking to be Understood",
        "Skill 16" : "Writing Professionally",
        "Skill 17" : "Git",
}
# start_screen()

def progress_check(skills):
    '''input -> dict
       output -> lists, complete lists and incomplete lists
    '''
    complete = []
    incomplete = []

    if type(skills) != type({}):
        return "invalid input"
    if type(skills) != type(""):
        return "please insert a string"

    for key in skills:
        print("Have you completed" %d.format(skills[key]))
        choice = input()
        choice = choice.upper()

        if choice == "YES":
            complete.append(skills[key])
            return complete
        elif choice == "NO":
            incomplete.append(skills[key])
            return incomplete

#progress_check(skills)
def user_input():
	Choice = int(input("Select your Skills Completed: \n"))
	if (Choice == 1):
		print("Selected as done: Version Control")
	elif (Choice == 2):
		print("Selected as done: Agile Methodology")
	elif (Choice == 3):
		print("Selected as done: Programming Logic")
	elif (Choice == 4):
		print("Selected as done: Object Oriented Programming ")
	elif (Choice == 5):
		print("Selected as done: Test-Driven Development ")
	elif (Choice == 6):
		print("Selected as done: Databases ")
	elif (Choice == 7):
		print("Selected as done: HTTP and Web Services")
	elif (Choice == 8):
		print("Selected as done: Front-End Development")
	elif (Choice == 9):
		print("Selected as done: Growth Mindset")
	elif (Choice == 10):
		print("Selected as done: Relationship Building")
	elif (Choice == 11):
		print("Selected as done: Asks Questions ")
	elif (Choice == 12):
		print("Selected as done: Motivation and Commitment")
	elif (Choice == 13):
		print("Selected as done: Adaptability")
	elif (Choice == 14):
		print("Selected as done: Seeks Feedback")
	elif (Choice == 15):
		print("Selected as done: Speaking to be Understood")
	elif (Choice == 16):
		print("Selected as done: Writing Professionally")
	elif (Choice == 17):
		print("Selected as done: Git")
	else:
		print("Invalid Choice ")

start_screen()
user_input()

	
