import string as str
class Choice:
    def __init__(self,course) -> None:
        super().__init__()
        self.ran = 5
        if course.lower() == "computer science" :
            List = ["Data Science","Data Analysis","Web Development","Rest Api Development"
            ,"Full Stack Development","BSC","MCA"]
            print(List)
        elif course.lower() == "development" :
            List = ["Web Development","Mobile Application Development"
            ,"Backend Development","Front End Development"]
            print(List)
        elif course.lower() == "designing" :
            List = ["WiX","Figma","Adobe XD"]
            print(List)
        elif course.lower() == "annimation" :
            List = ["Adobe Illustrator","Adobe After Effects"]
            print(List)
        elif course.lower() == "graphic designing" :
            List = ["Adobe Illustrator","Adobe Photoshop","Corel Draw","3Ds MAX"]
            print(List)
        else :
            print("Course Not Available")