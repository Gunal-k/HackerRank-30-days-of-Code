class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
   
    def calculate(self):
        calc = sum(self.scores) // len(self.scores)
        if calc >= 90 and calc <= 100:
            return "O"
        elif calc >= 80 and calc < 90:
            return "E"
        elif calc >= 70 and calc < 80:
            return "A"
        elif calc >= 55 and calc <= 70:
            return "P"
        elif calc >= 40 and calc <= 55:
            return "D"
        else:
            return "T"
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())