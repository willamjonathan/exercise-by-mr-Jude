class Person:
    def __init__(self,name,address):
        self.name = name
        self.__address = address
        
    def setAddress(self,address):
        self.__address = address
        
    def getAddress(self):
        return self.__address
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return " {}({})".format(self.getName(),self.getAddress())
#testing  
p1 = Person("Will","Sukajadi")
print(p1.__str__())

class Student(Person):
    def __init__(self, name, address,numCourses):
        super().__init__(name, address)
        self.grade = []
        self.numCourses = numCourses
        self.courses = []
    def AddCourse (self,courses):
        self.courses.append(courses)
    def AddGrade(self,grade):
        self.grade.append(grade)
    def getCourse(self):
        return self.courses
    def getGrade(self):
        return self.grade
    def getNumCourses(self):
        return self.numCourses
    #def get average?
    def __str__(self):
        return " Student: {}({}) Grade : {}".format(super().getName(),super().getAddress(),self.grade())


class Teacher(Person):
    def __init__(self,name,address,numCourses,courses):
        super().__init__(name, address)
        self.setNumCourses(numCourses)
        self.setCourses(courses)
