#QuizManager manages the quiz content
import os.path
import os
import quizparser
import datetime

class QuizManager:
	def __init__(self, quizfolder):
		self.quizfolder = quizfolder

		#TODO: the most recently selected quiz
		self.the_quiz = None

		#TODO: initialize the collection of quizzes
		self.quizzes = dict()
	
		#TODO: stores the results of the most recent quiz
		self.results = None

		#TODO: the name of the person taking  the quiz
		self.quiztaker = ""

		#TODO: make sure that the quiz folder exists
		if (os.path.exists(quizfolder) == False):
			raise FileNotFoundError("the quiz folder does not seem to exist")

		#TODO: build the list of quizzes
		self._build_quiz_list()


	def _build_quiz_list(self):
		dircontents = os.scandir(self.quizfolder)		#builds list of folder contents

		#TODO: parse the XML files in the directory
		for i, f in enumerate(dircontents):
			if f.is_file():
				parser = quizparser.QuizParser()
				self.quizzes[i+1] = parser.parse_quiz(f)

	
	#TODO: print a list of the currently installed quizzes
	def list_quizzes(self):
		for k,v in self.quizzes.items():
			print(f"({k}): {v.name}")



	#start the given quiz for user and return the results
	def take_quiz(self, quizid, username):
		self.quiztaker = username
		self.the_quiz = self.quizzes[quizid]
		self.results = self.the_quiz.take_quiz()	

	
	#prints the results  of the most recently taken quiz
	def print_results(self):
		self.the_quiz.print_results(self.quiztaker)

	
	#save the results of most recent quiz to file
	# the file is named using  current date as QUizResults_YYYY_MM_DD_N (N is incremented until unique)
	def save_results(self):
		#TODO: save the results
		today = datetime.datetime.now()
		filename = f"QuizResults_{today.year}_{today.month}_{today.day}.txt"

		#TODO: if filename already exists then add a digit to end until its unique
		n = 1
		while(os.path.exists(filename)):
			filename = f"QuizResults_{today.year}_{today.month}_{today.day}_{n}.txt"
			n = n+1

		with open(filename, "w") as f:
			self.the_quiz.print_results(self.quiztaker, f)



if __name__ == "__main__":
	qm = QuizManager("Quizzes")
	qm.list_quizzes()



