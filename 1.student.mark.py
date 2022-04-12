#some note that i follow your solve so sthing i don't know can i ask u about it ?
def StudNum():
  snum = int(input("How many students?: "))
  return snum
def Studin4(stud):
  studs = [] 
  for i in range (0, stud):
    names = input("Student's name: ")
    ids = input("Student's id: ")
    dobs = input("Student's date of birth: ")
    s = {
      "name": names,
      "id": ids,
      "dob": dobs,
      "marks": {} #as u say it will be a dict
    }
    studs.append(s)
  return studs
def CouNum():
  cnum = int(input("How many courses?: "))
  return cnum
def Couin4(cou):
  cous = []
  for i in range (0, cou):
    namec = input("Course's name: ")
    idc = input("Course's id: ")
    c = {
      "name": namec,
      "id": idc
    }
    cous.append(c)
  return cous
def CouPicked(cous):
  CouL(cous)
  coid = input('gimme your course id u choose from the previous list: ')
  return coid
def StudMark(coid, studs):
  print(f'give marks in {coid} for him/her: ')
  for std in studs:
    studmk = int(input(Student {std['name']}))
    std["marks"][coid] = Studmk 

def StudL(studs):
  print("\nStudent information list: ")
  for stu in studs:
    print(f'{stu["name"]} | {stu["id"]} | {stu["dob"]}')
def CouL(cous):
  print("\nCourse information list: ")
  for co in cous:
    print(f"{co['name']} | {co['id']}")
def showIn4(coid, studsa):
  print("\nWe have a mark for this course: ")
    for stmrk in studs:
      print(f'{stmrk["name"]} | {stmrk["mark"]}')


studentNumber = StudNum()
studentdetail = Studin4(stud)

courseNumber = CouNum()
coursedetail = Couin4(cou)

cousec = CouPicked()
mark = StudMark(mrk)

StudL(studs)
CouL(cous)

cousec = CouPicked(cous)
showIn4(cousec, studs)




