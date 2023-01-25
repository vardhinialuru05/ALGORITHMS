class fraction:
    @staticmethod
    def __find(num, den):
        minValue = min(num, den)
        i = 2
        while i <= minValue:
            if num % i == 0 and den % i == 0:
                num //= i
                den //= i
            else:
                i +=1 
        return num,den
    def __init__(self,num,den):
        self.num , self.den = self.__find(num,den)
    def  print(self):
        print(self.num,"/",self.den)
    def add(self,f2):
        self.num = self.num * f2.den + f2.num * self.den
        self.den = self.den * f2.den

        self.num , self.den = self.__find(self.num,self.den)
    def mul(self,f2):  
        self.num = self.num * f2.num
        self.den = self.den * f2.den
        self.num , self.den = self.__find(self.num,self.den)
    def __truediv__(self,f2): #operator overloading-
        temp = fraction(self.num,self.den)
        temp.num = self.num * f2.den
        temp.den = self.den * f2.num
        temp.num , temp.den = self.__find(temp.num,temp.den)
        return temp
f1 = fraction(1,3)
f2 = fraction(5,3)
f3 = f1 / f2
f3.print()
