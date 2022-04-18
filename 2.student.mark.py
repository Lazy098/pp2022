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
StudMk = []
studetail = (
	input("Enter student's id: "),
	input("Enter course's id: ")
	)
    StudMk.append(studetail)
    if True:
    	stmark = int(input("Enter student's mark: "))
    	if stmark < 0 || stmark >20:
    		print("unvalid mark")
    	else 
    	    print(f"Studen {self.name} has {stmark} point in course {couid}")

#out of idea :(( 


	        





