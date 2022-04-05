from datetime import datetime
class Student:
	def __init__(self, id, name, dob):
		self.id = id
		self.name = name 
		self.dob = dob  

StudL = []
num = int(input("Number of student: "))
for i in range(0, num):
	studentdetail = (
	input("His/Her student id?: "),
	input("His/Her name?: "),
	input("Enter student date of birth: ")
	)
	StudL.append(studentdetail)
	
class Course:
	def __init__(self, idcou, namecou):
	    self.idcou = idcou
	    self.namecou = namecou

CouL = []
num = int(input("Number of course: "))
for i in range(0, num):
	coursedetail = (
	input("Course id?: "),
	input("Course name?: "),
	)
	CoudL.append(coursedetail)