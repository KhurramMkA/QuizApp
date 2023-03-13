#pyquiz.py - Main starting point of the program
from quizmanager import QuizManager

class QuizApp:
	QUIZ_FOLDER = "Quizzes"

	def __init__(self):
		self.username = ""
		self.qm = QuizManager(QuizApp.QUIZ_FOLDER)


	def startup(self):
		#print greeting at startup
		self.greeting()

		# TODO: ask user for thier name
		self.username = input("What is your name? ")
		print(f"Welcome, {self.username}!")


	def greeting(self):
		print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~-~-~")
		print("-~-~-~-~-~-Welcome to PyQuiz!~-~-~~-~-~")
		print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~-~-~")
		print()

	def menu_header(self):
		print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~-~-~")
		print("Please make a selection:")
		print("(M): Repeat this menu")
		print("(L): List quizzes")
		print("(T): Take a quiz")
		print("(E): Exit program")

	def menu_error(self):
		print("That is not a valid selection. Please try again.")

	def goodbye(self):
		print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~-~-~")
		print(f"Thanks for using PyQuiz, {self.username}!")
		print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~-~-~")

	def menu(self):
		self.menu_header()

		#TODO : get users selection and act on it. This loop will
		#run unitl user exits app
		selection = ""
		while(True):
			selection = input("Selection? ")

			if len(selection) == 0:
				self.menu_error()
				continue

			selection = selection.capitalize()

			if selection[0] == 'E':
				self.goodbye()
				break
			elif selection[0] == 'M':
				self.menu_header()
				continue
			elif selection[0] == 'L':
				print("\n Available Quizes Are: ")
				# TODO list the quizzes
				self.qm.list_quizzes()
				print("------------------------------\n")
			elif selection[0] == 'T':
				try:
					quiznum = int(input("Quiz number: "))
					print(f"you have selected Quiz number {quiznum}")

					# TODO start the quiz
					self.qm.take_quiz(quiznum, self.username)
					self.qm.print_results()

					# TODO aks the user if they want to save results
					dosave = input("Save the results? (y/n): ")
					dosave = dosave.capitalize()
					if len(dosave) > 0 and dosave[0] == 'Y':
						self.qm.save_results()

				except:
					self.menu_error()
			else:
				self.menu_error()



	#This is the entry point to the program
	def run(self):
		#Execute startup routine - ask name, print greeting, etc.
		self.startup()
		#Start main program menu and run until user exits
		self.menu()


if __name__ == "__main__":
	app = QuizApp()
	app.run()
