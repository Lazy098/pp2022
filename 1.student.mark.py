from datetime import datetime

def getStudentCount ():
    return int (input ("How many students? "))
    
def getStudentDetails ():
    yid = input ("Enter student id: ")
    yname = input ("Enter student name: ")
    while True:
        try:
            sdob = input ("Enter student's date of birth mm/dd/yyyy: ")
            dob = datetime.strptime(sdob, "%m/%d/%Y")
        except ValueError:
            print("that not a date of birth format!")
            continue
        break
    tdob = str(dob.month) + "/" + str(dob.day) + "/" + str(dob.year)
    return yid, yname, tdob

def getCourseCount ():
    return int (input ("how about the number of this courses?: "))
    
def getCourseDetails ():
    idc = input ("how about course id?: ")
    namec = input ("and course name too?: ")
    return idc, namec
    
def getStudentDetails ():
    gid = input ("Enter student id: ")
    gname = input ("Enter student name: ")
    gdob = input ("Enter student's date of birth: ")
    return gid, gname, gdob 
    
def getMarks (sid, cid):
    point = f"I want to know the marks for student {sid} for course {cid}: ".format (sid, cid)
    input (point)
    
cStudents = getStudentCount ()
studentLst = []
for i in range (cStudents):
    id, name, dob = getStudentDetails ()
    studentLst.append ((id, name, dob))

print ("\nListing all students now..")
for s in studentLst:
    print (f"Student id: {s[0]} - Name: {s[1]} - Date of birth: {s[2]}")
    
nStudents = getStudentCount ()
studentLst = []
for i in range (nStudents):
    sid, name, dob = getStudentDetails ()
    studentLst.append ((sid, name, dob))

nCourses = getCourseCount ()
courseLst = []
for i in range (nCourses):
    idc, namec = getCourseDetails ()
    courseLst.append ((idc, namec))
    
d = {}
while True:
  n = int (input ("how many student-course marks do you want to know? "))
  if n < 0 or n > nStudents * nCourses:
      print("can't find student-course marks, ask your teacher again please")
      continue
  break 
  for i in range (n):
      while True:
          yid = input ("Enter student id: ")
          idc = input ("Enter course id: ")
          if yid not in [student [0] for student in studentLst]:
              print ("not a student id")
              continue 
          if idc not in [course [0] for course in courseLst]:
              print ("not a  course id")
              continue 
          break
    
      while True:
          marks = float (input ("Enter marks: "))
          if marks < 0 or marks > 20:
              print("Mark is not available, please try again")
              continue
          break

      if idc in d:
          d [idc].append ((yid, marks))
      else:
          d [idc] = [(yid, marks)]
          print ("\nListing all students now..")
for s in studentLst:
    print (f"Student id: {s[0]} Name: {s[1]} Date of birth: {s[2]}")

print ("\nListing all courses now..")
for c in courseLst:
    print (f"Course id: {c[0]} Name: {c[1]}")
    
cid = input ("\nWhich course do you want to see all student marks for? ")
if cid in d:
    for tups in d [cid]:
        print (f"Student {tups[0]} got {tups [1]} marks")