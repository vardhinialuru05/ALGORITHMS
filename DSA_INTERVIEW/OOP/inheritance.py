class Vehicle:
    def __init__(self,color,speed):
        self.color = color
        self.__speed = speed 

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, newSpeed):
        self.__speed = newSpeed


class Car(Vehicle):
    def __init__(self,color,speed,noOfGears,isConvertible):
        super().__init__(color,speed)
        self.noOfGears = noOfGears
        self.isConvertible = isConvertible
    
    def setSpeed(self, newSpeed):
        super().setSpeed(newSpeed)


    def print(self):
        print("color =" , self.color)
        print("speed =" , super().getSpeed())
        print("Gears =",self.noOfGears)
        print("isConvertible = " , self.isConvertible)

c = Car("red",180,2,True)
c.setSpeed(1000)
c.print()