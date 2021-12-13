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
    def __init__(self, name, address,grade,numCourses,courses):
        super().__init__(name, address)
        self.grade = 0.0
        self.setCourses(courses)
        self.setNumCourses(numCourses)
        
    def setgrade(self,grade):
        if grade >60 :
            self.grade = grade
            return grade
        else:
            self.grade = "void"

    def __str__(self):
        return " Student: {}({}) Grade : {}".format(super().getName(),super().getAddress(),self.grade())
    
class Teacher(Person):
    def __init__(self,name,address,numCourses,courses):
        super().__init__(name, address)
        self.setNumCourses(numCourses)
        self.setCourses(courses)
