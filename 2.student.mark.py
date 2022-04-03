from datetime import datetime
class Student:
	def haveStudnum(stud):
		stud.num = int(input("how many students you wanna enter?: ")) 
		return stud.num 
	def Studin4(stud):
	    stud.id = input("Enter student ID: ")
	    stud.name = input("Enter student name: ")
	    stud.dob = input("Don't forget his/her date of birth: ")
	    return stud.id, stud.name, stud.dob

	def StudentL(stud):
		studL = []
	    for i in range(stud.num):
        stud.in4 = Studin4()
        stud.append((stud.id, stud.name, stud.dob))


class Course:
	def haveCourse(cou):
		cou.many = int(input("How many Courses do you want?: "))
		return cou.many
	def Coursein4(cou):
		cou.id = input("Enter course ID:")
		cou.name = input("Enter course name: ")
	def CourseL(cou):
		coul = []
		for i in range(cou.many):
		cou.in4 = Coursein4()
		cou.append((cou.id ,cou.name))
		

class Stumark:
	def Marks(mk):
		d = {}
		mk.ask = int(input("How many students are there?: "))
		for i in range(mk.ask):
			while True:
				mk.studid = input("Enter student id: ")
				mk.courid = input("Enter course id: ")

			while True: 
				mk.marks = int(input("Enter mark: "))
				if mk.marks <= 20 and mr.marks >= 0:
					break
				else: 
					print("enter right number (0 <= mark <= 20)")
					continue

			if mk.marks in d: 
				d[].append ((mk.studid, mk.marks))
			else:
				d[] = [(mk.studid, mk.marks)]

for sl in StudentL(stud):
	mk.studlist = print(f"Student id: {sl[0]} | Name: {sl[1]} |Date of birth: {sl[2]}")
for cl in CourseL(cou):
    mk.courselist = print(f"Course id: {cl[0]} | Name: {cl[1]}")


afk = Student()
afk.haveStudnum()
afk.Studin4()
afk.StudentL()

pity = Course()
pity.haveCourse()
pity.Coursein4()
pity.CourseL() 

sco = Stumark()
sco.ask()
sco.studid()
sco.courid()
sco,marks()
sco.studlist()
sco.courselist()