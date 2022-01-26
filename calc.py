class calc:
    #Nesting Of Class 
    def __init__(self) -> None:
        sign = (input("Enter Sign : "))
        self.var1 = int(input("Enter Num1 : "))
        self.var2 = int(input("Enter Num2 : "))
        if sign == '+':
            self.add()
        elif sign == '-':
            self.sub()
        elif sign == '*':
            self.mul()
        elif sign == '/':
            self.div()
        else :
            print("Wrong Input")
        newobj = self.mynew
        newobj()
    class mynew:
        def __init__(self) -> None:
            print("New Class")
    def add(self):
        var3 = self.var1 + self.var2
        print(var3)
    def sub(self):
        var3 = self.var1 - self.var2
        print(var3)
    def mul(self):
        var3 = self.var1 * self.var2
        print(var3)
    def div(self):
        var3 = self.var1 / self.var2
        print(var3)
obj=calc
obj()