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
		#I need to do sth in here 


class Course:
	def haveCourse(cou):
		cou.many = int(input("How many Courses do you want?: "))
		return cou.many
	def Coursein4(cou):
		cou.id = input("Enter course ID:")
		cou.name = input("Enter course name: ")
	def CourseL(cou):
		coul = []
		#like studL but need to change a little bit


#need to create another class about student's mark


afk = Student()
afk.haveStudnum()
afk.Studin4()
#afk.studL()

pity = Course()
pity.haveCourse()
pity.Coursein4()
#pity.CourseL() (can use when i do sth in def courseL)


#this code still on going
#it looks like a demo and i also add comment to remind me to finish that