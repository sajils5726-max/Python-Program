class Student:
 "Common base class for all students"

def getData(self,rollno,name,course) :
   self.rollno=rollno
   self.name= name
   self.course = course
def displayStudent (self):
   print("Roll Number:",self.rollno)
   print("Name:",self.name)
   print("Course:",self.coures)

#Inheritance
class Test(Student):
  def getMarks(self,marks):
    self.marks=marks
  def displayMarkrs(self):
    print ("Total Marks:", self. marks)
class Sports:
  def getSportsMarks(self,spmarks):
    self.spmarks=spmarks
  def displaySportsMarks(self) :
    print("Sports Marks:",self.spmarks)

#Multiple Inheritance
class Result (Test,Sports):
  def calculateGrade(self) :
      m=self.marks+self.spmarks 
      if m>480: self.grade="Distinction"
      elif m>360: self.grade="First Class"
      elif m>240: self.grade="Second Class"
      else: self.grade="Failed"
      print ("Result:", self.grade)

#Main Program
r = int (input("Enter Roll Number:"))
n = input("Enter Name:")
c= input("Enter Course Name:")
m = int(input("Enter Marks:"))
s = int(input("Enter Sports marks:"))

#creating the object
print ("Result")
studl=Result() #instance of child
studl.getData(r,n,c)
studl.getMarks(m)
studl.getSportsMarks(s)
studl.displayStudent ()
studl.displayMarks()
studl.displaySportsMarks()
stud1.calculateGrade()
