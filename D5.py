from choice import Choice as cho
class User():
    def __init__(self) -> None:
        self.List = ["Computer Science","Designing","Development",
        "Annimation","Graphic Designing"]
        self.name=input("Enter Your Name : ")
        self.mobile = input("Enter Your Mobile Number :")
        self.age = input("Enter Your Age")
        print("Subject Available :")
        print(self.List)
        self.course = input("Enter Subject Here :")
    def get(self):
        print("User Details :")
        print("")
        print("Name of User : ",self.name)
        print("Mobile Number : ",self.mobile)
        print("Age : ",self.age) 
        self.obj = cho(self.course)   
        print("Completed")
        print("")
u1=User()
#u2=User("Shub","7389162810","18")
u1.get()
#u2.get()
#obj=u2.Child("computer science")
