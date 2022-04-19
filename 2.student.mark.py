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
    def __init__(self, idstud, idcou, markstud):
    	self.idstud = idstud
    	self.idcou = idcou 
    	self.markstud = markstud
    def studmark(mrk):
y = {}
mrk.ask = int(input("Enter number of student: "))
for i in range(mrk.ask):
	while True:
		mrk.idstud = input("Student id: ")
		mrk.idcou = input("Course id:")
	while True: 
		mrk.mark = int(input("Student's mark: "))
		if mrk.mark < 0 || mrk.mark > 20:
			print("Wrong access deny! please do it again ( 0 <= mark <= 20")
		else:
			break 





#out of idea :(( 


	        





