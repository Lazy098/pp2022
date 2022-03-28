from datetime import datetime

studin4 = {
    "ID": None,
    "Name": None,
    "DoB": None
}

def haveStudentinformation():
  studin4 = {
    "ID": input("show me your ID: "),
    "Name": input("How about your name?: "),
    "DoB": input("don't forget the date of birth: ")
}
  return studin4

def haveCourceinformation():
  idc = input("Enter cource id: ")
  namec = input("Enter cource name please: ")
  return idc, namec

numStudents = int(input("how many students are there?: "))
StudentL = []
for i in range(numStudents):
  studin4 = haveStudentinformation()
  StudentL.append(studin4)

numCourses = int(input("how many courses are there?: "))
CourseL = []
for i in range(numCourses):
  idc, namec = haveCourceinformation()
  CourseL.append((idc, namec))

d = {}
m = int(input("Enter how many student's marks in course do you want to enter? "))
for i in range (m):
    while True:
        sid = input ("Enter student id: ")
        cid = input ("Enter course id: ")
        break
        
    while True:
        try:
          marks = int(input("Enter mark: ")) 
          if marks>=0 and marks<=20:
            break;
          else:
              print("Mark should be >0 and <20")      
        except ValueError:
          print("Provide an integer value")
          continue

    if cid in d:
        d [cid].append ((sid, marks))
    else:
        d [cid] = [(sid, marks)]
        
print("\nWe got the student list")
for t in StudentL:
    print(f"Student id: {t[0]} | Name: {t[1]} |Date of birth: {t[2]}")

print("\nAlso got the course list")
for o in CourseL:
    print(f"Course id: {o[0]} | Name: {o[1]}")
    
cid = input("\nEnter course ID to check student's mark: ") 
if cid in d:
  for tups in d [cid]:
    print (f"Student {tups[0]} got {tups [1]} marks")
