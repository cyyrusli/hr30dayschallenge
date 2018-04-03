# Day 12 - Inheritance

# You are given two classes, Person and Student, where Person is the base class and Student
# is the derived class. Completed code for Person and a declaration for Student are provided for
# you in the editor. Observe that Student inherits all the properties of Person.
# Complete the Student class by writing the following:
# A Student class constructor, which has 4 parameters:
# 1. A string, firstName.
# 2. A string, lastName.
# 3. An integer, id.
# 4. An integer array(or vector) of test scores, scores.
# A char calculate() method that calculates a Student object's average and returns the grade
# character representative of their calculated average:
# Letter      Average(a)
#   O         90<=a<=100
#   E         80<=a<=90
#   A         70<=a<=80
#   P         55<=a<=70
#   D         40<=a<=55
#   T           a<40


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
      super().__init__(firstName, lastName, idNumber)
      self.scores = scores

    def calculate(self):
      avgScore = sum(self.scores) / len(self.scores)
      if 90 <= avgScore <= 100:
        return "O"
      elif 80 <= avgScore <= 90:
        return "E"
      elif 70 <= avgScore <= 80:
        return "A"
      elif 55 <= avgScore <= 70:
        return "P"
      elif 40 <= avgScore <= 55:
        return "D"
      elif avgScore < 40:
        return "T"
      else:
        return ""

name = input().split(' ')
firstName = name[0]
lastName = name[1]
idNumber = name[2]
s2avg = int(input())
scores = list(map(int, input().split()))
c = Student(firstName, lastName, idNumber, scores)
c.printPerson()
print("Grade:", c.calculate())