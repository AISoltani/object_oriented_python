class calcu:
    def __init__(self,input1,input2):
        self.a=input1
        self.b=input2
    def sum1(self):
        return self.a+self.b

class calcu2(calcu):
    def multi(self):
        return self.a*self.b#+self.sum1()


mycal=calcu(30,5)
print(mycal.sum1())

mycal2=calcu2(30,20)
print(mycal2.sum1())
print(mycal2.multi())
