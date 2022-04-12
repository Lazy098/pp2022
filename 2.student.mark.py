from datetime import datetime
class Student:
	def __init__(self, id, name, dob):
		self.id = id
		self.name = name 
		self.dob = dob  

StudL = []
studnum = int(input("Number of student: "))
for i in range(0, studnum):
	studentdetail = (
	input("His/Her student id?: "),
	input("His/Her name?: "),
	datetime.strptime(int(input("Enter his/her date of birth: ")))
	)
	StudL.append(studentdetail)
	
class Course:
	def __init__(self, idcou, namecou):
	    self.idcou = idcou
	    self.namecou = namecou

CouL = []
counum = int(input("Number of course: "))
for i in range(0, counum):
	coursedetail = (
	input("Course id?: "),
	input("Course name?: "),
	)
	CouL.append(coursedetail)

x = {}
num = int(input("How many student in the course?: "))
for i in range(num):
		studid = input("Enter his/her id: ")
		couid = input("Enter course id: ")




#well i remake lab2 because i see that was a mess so lab2 is going to be finish in the short time