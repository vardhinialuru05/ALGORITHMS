class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def isLegal(self):
        if self.age >= 18:
            return True
        else:
            False
    
    def __str__(self):
        return "age=" + str(self.age)

s1 = Student("vardhini", 19)
# print(s1.isLegal())
print(s1)
#by default py has a class object