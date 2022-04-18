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
	datetime.strptime(input( "Enter his/her date of birth: "), '%d/%m/%Y'),
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

class Mark:
	def __init__(self, mkstud)
	    self.mkstud = mkstud
	    m = []
	def coursemk:
	    while True:
	        try: 
	        	mkstud = int(input("Enter student's mark: "))
	        if mkstud < 0 || mkstud > 20: 
	        	print("Wrong access deny!")
	        else
	            print(f"Student {name} get {mkstud}")
	        





