class Student:        
   stuCount = 0
   
   def __init__(self,name,stu_no,class_no,gender):
      self.name=name
      self.stu_no=stu_no
      self.class_no=class_no
      self.gender=gender
      Student.stuCount +=1
 
   def study(self):
       print 'Student can study'
 
   def getStuCount(self):
       return Student.stuCount
    
 
class  primaryStudent(Student):
    primaryStuCount=0
       
    def canRecite(self):
       print "prinary Student can recite"

    def canOral(self):
       print "Primary Student can oral"

class Middlestudent(Student):
    middlestyCount=0
    
    def __init__(self,name,stu_no,class_no,gender):
      self.name=name
      self.stu_no=stu_no
      self.class_no=class_no
      self.gender=gender
      Student.stuCount+=1
      MiddleStudent.middlestuCount +=1
 
    def canChemistry(self):
        print 'middle Student can Chemistry'
      
    def canpyhics(self):
        print 'middle Student can physics'
