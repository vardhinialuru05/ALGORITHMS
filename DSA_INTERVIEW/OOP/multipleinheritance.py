class Father:
    def print(self):
        print("i am the father")

class Mother:
    def print(self):
        print("i am the mother")

class Child(Father,Mother): 
    pass


c1 = Child()
c1.print() #as in child we passed father parameter first it goes to that class and will print
    
