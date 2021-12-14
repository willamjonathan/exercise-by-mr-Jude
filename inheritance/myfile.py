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
    def __init__(self, name, address):
        super().__init__(name, address)
        self.grades = []
        self.numCourses = 0
        self.courses = []

    def __str__(self):
        return "Name: {}\nAdress:{}\nNumber of courses: {}\nCourses : {}\nGrades :{} ".format(self.name(),self.getAddress(),self.numCourses(),self.courses(),self.grades())
    def AddCourseGrade (self,courses):
        self.courses.append(courses)
        self.grades.append(grade)
        self.numCourses += 1

    def printGrades(self):
        for i in range(self.numCourses):
            print(f"{self.courses[i]}:{self.grades[i]}\n")

    def getAverageGrades(self):
        total = 0 
        for grade in self.grades:
            total += grade
        return total/self.numCourses
    
    def __str__(self):
        return " Student: {}({}) Grade : {}".format(super().getName(),super().getAddress(),self.grade())


class Teacher(Person):
    def __init__(self,name,address):
        super().__init__(name, address)
        self.numCourses = 0
        self.courses = []

    def addCourses(self,course):
        if course in self.courses:
            print("course already exists")
            return False
        else:
            self.course.append(course)
            self.numCourses +=1
            return True
    def removeCourses(self,course):
        if course not in self.courses:
            print("course doesn't already exist")
            return False
        else:
            self.course.remove(course)
            self.numCourses -=1
            return True

    def __str__(self):
        return f"Name:{self.name}\nAdress: {self.address}\n Number of courses : {self.numCourses}\nCourses : {self.courses}"
    
        
            
        
    
