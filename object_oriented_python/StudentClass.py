class Student:
    'Common base class for all students'
    count = 0
    def __init__(self, name, family):
      self.name = name
      self.family = family
      Student.count += 1;
     
    def displayCount(self):
     print("Total Student : ", Student.count)

    def displayStudent(self):
     print("Name : ", self.name,  ", family: ", self.family)

print("Student.__doc__:", Student.__doc__)
print("Student.__name__:", Student.__name__)
print("Student.__module__:", Student.__module__)
print("Student.__bases__:", Student.__bases__)
print("Student.__dict__:", Student.__dict__)
