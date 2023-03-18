#The Quiz and Question classes define a particular quiz
import datetime
import sys
#TODO: import randommodule to randomize questions
imort random

class Quiz:
	def __init__(self):
		# TODO: defien quiz propeties
		self.name = ""
		self.description = ""
		self.questions = []
		self.score = 0 
		self.correct_count = 0
		self.total_points = 0
		self.completion_time = 0

	def print_header(self):
		print("\n\n********************************************")
		# TODO: print the quiz header
		print(f"QUIZ NAME: {self.name}")
		print(f"DESCRIPTION: {self.description}")
		print(f"QUESTIONS: {len(self.questions)}")
		print(f"TOTAL POINTS: {self.total_points}")
		print("********************************************\n")

	def print_results(self, quiztaker, thefile = sys.stdout):
		print("********************************************", file = thefile, flush = True)
		#TODO: Print the results
		print(f"RESULTS for {quiztaker}", file = thefile, flush = True)
		print(f"Date: {datetime.datetime.today()}", file = thefile, flush = True)
		print(f"ELAPSED TIME: {self.completion_time}", file = thefile, flush = True)
		print(f"QUESTIONS: {self.correct_count} out of {len(self.questions)} correct", file = thefile, flush = True)
		print(f"SCORE: {self.score} points out of possible {self.total_points}", file = thefile, flush = True)
		print("********************************************\n", file = thefile, flush = True)
	
	def take_quiz(self):
		 # TODO: initialize quiz state
		 self.score = 0
		 self.correct_count = 0
		 for q in self.questions:
			 q.is_correct = False

		 # TODO: print the header
		 self.print_header()

		 #TODO: randomize the questions
		 random.shuffle(self.questions)

		 #TODO: record the start time of quiz
		 starttime = datetime.datetime.now()

		 # TODO: execute each question and record the result
		 for q in self.questions:
			 q.ask()
			 if (q.is_correct):
				 self.correct_count += 1
				 self.score += q.points
				 
		 print("-------------------------------------")

		 #TODO: record the end time of quiz
		 endtime = datetime.datetime.now()

		 #TODO: ask user if they want to redo any  incorrect questions
		 if self.correct_count != len(self.questions):
			 response = input("\nIt looks like you missed some questions. Redo the incorrect questions? (y/n)").lower()
			 if response[0] == "y":
				wrong_qs = [q for q in self.questions if q.is_correct = False]
				for q in self.questions:
					q.ask()
					if (q.is_correct):
					self.correct_count += 1
					self.score += q.points
				 
				print("-------------------------------------\n")
				endtime = datetime.datetime.now()


		 self.completion_time = endtime - starttime
		 self.completion_time = datetime.timedelta(seconds = round(self.completion_time.total_seconds()))

		 # TODO: return the results
		 return (self.score, self.correct_count, self.total_points)



class Question:
	def __init__(self):
		# TODO: define the Question fields
		self.points = 0
		self.correct_answer = ""
		self.text = ""
		self.is_correct = False

class QuestionTF(Question):
	def __init__(self):
		super().__init__()

	# TODO: define ask method
	def ask(self):
		while(True):
			print(f"(T)rue or (F)alse: {self.text}")
			response = input("? ")

			# TODO: Check to see if no response was entered
			if len(response) == 0:
				print("Sorry, that is not a valid response. Please try again.")
				continue

			# TODO: Check to see if either T or F was given
			response = response.lower()
			if response[0] != "t" and response[0] != "f":
				print("Sorry, that is not a valid response. Please try again.")
				continue

			#TODO: Mark as correct if answered correctly
			if response[0] == self.correct_answer:
				self.is_correct = True

			break

class QuestionMC(Question):
	def __init__(self):
		super().__init__()
		# TODO: define answers for this question
		self.answers = []

	# TODO: define ask method
	def ask(self):
		while (True):
			# TODO: Present question and possible answers
			print(self.text)
			for a in self.answers:
				print(f"({a.name}) {a.text}")
			
			response = input("? ")

			# TODO: Check to see if o response was entered
			if len(response) == 0:
				print("Sorry, that is not a valid response. Please try again.")
				continue

			# TODO: Mark as correct if answered correctly
			response = response.lower()
			if response[0] == self.correct_answer:
				self.is_correct = True

			break

class Answer:
	def __init__(self):
		# TODO:	define the Answer fields
		self.text = ""
		self.name = ""


if __name__ == "__main__":
	qz = Quiz()
	qz.name = "Sample Quiz"
	qz.description = "This is a sample quiz!"


	q1 = QuestionTF()
	q1.text = "Broccoli is good for you."
	q1.points = 5
	q1.correct_answer = "t"
	#q1.ask()
	qz.questions.append(q1)


	q2 = QuestionMC()
	q2.text = "What is 2+2?"
	q2.points = 10
	q2.correct_answer = "b"
	ans = Answer()
	ans.name = "a"
	ans.text = "3"
	q2.answers.append(ans)
	ans = Answer()
	ans.name = "b"
	ans.text = "4"
	q2.answers.append(ans)
	ans = Answer()
	ans.name = "c"
	ans.text = "5"
	q2.answers.append(ans)
	#q2.ask()
	qz.questions.append(q2)

	qz.total_points = q1.points + q2.points
	result = qz.take_quiz()
	print(result)

	#print(q1.is_correct)
	#print(q2.is_correct)