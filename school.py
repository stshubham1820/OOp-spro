from configparser import DuplicateSectionError
import update

class syc:
    def __init__(self) -> None:
        usermode = input("Teacher / Student : ")
        usermode=usermode.lower()
        user = input("Register / Login : ")
        user = user.lower()
        if usermode == "teacher":
            self.teacher(user)
        elif usermode == "student":
            self.student(user)
        else :
            print("Wrong Input Try Again")
    def teacher(self,user):
        import mysql.connector
        try :
            mydb = mysql.connector.connect(host='localhost',user='root',password='1820',database='work')
            pointer = mydb.cursor()
            def techlogin():
                username = input("Enter User Name : ")
                username = username.lower()
                select = "select * from teacher"
                pointer.execute(select)
                data =pointer.fetchall()
                for i in data :
                    if i[0] == username :
                        passw=input("Enter Password : ")
                        if i[2] == passw :
                            print("Login Sucessful")
                            self.acess("teacher",username)
                            break
                        else :
                            print("Password Incorrect : Try Again")
                            break            
                else :
                    print("User is Not Here : Please Register")
                    techregister()
            def techregister():
                try :
                    username = input("Enter User Name : ")
                    username = username.lower()
                    Name = input("Enter Your Name : ")
                    Passw = input("Enter Password : ")
                    Email = input("Enter Email Address : ")
                    tup = (username,Name,Passw,Email)
                    user = "insert into teacher values(%s,%s,%s,%s)"
                    pointer.execute(user,tup)
                    mydb.commit()
                    print("Registeration Sucessful")
                    mydb.close()
                except Exception as err:
                    print("Registeration Unsucessful Due to : ",err)
            if user == "login":
                techlogin()
            elif user == "register":
                techregister()
            else :
                print("Wrong Input")
        except Exception as err:
            print("Connection Failed Due to : ",err)
    def student(self,user):
        import mysql.connector
        try :
            mydb = mysql.connector.connect(host='localhost',user='root',password='1820',database='work')
            pointer = mydb.cursor()
            def studlogin():
                username = input("Enter User Name : ")
                username = username.lower()
                select = "select * from student"
                pointer.execute(select)
                data =pointer.fetchall()
                for i in data :
                    if i[0] == username :
                        passw=input("Enter Password : ")
                        if i[2] == passw :
                            print("Login Sucessful")
                            self.acess("student",username)
                            break
                        else :
                            print("Password Incorrect : Try Again")
                            break            
                else :
                    print("User is Not Here : Please Register")
            def studregister():
                try :
                    username = input("Enter User Name : ")
                    username = username.lower()
                    Name = input("Enter Your Name : ")
                    Passw = input("Enter Password : ")
                    Email = input("Enter Email Address : ")
                    Dob = input("Enter Date Of Birth : ")
                    Father_Name = input("Enter Father Name : ")
                    Mother_Name = input("Enter Mother Name : ")
                    DAdm = input("Date Of Admission : ")
                    tup = (username,Name,Passw,Email,Dob,Father_Name,Mother_Name,DAdm)
                    user = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    pointer.execute(user,tup)
                    mydb.commit()
                    print("Registeration Sucessful")
                    mydb.close()
                except DuplicateSectionError as err:
                    print("Already Registered Please Login")
                except Exception as Err :
                    print("Registeration Unsucessful Due to : ",Err)
            if user == "login":
                studlogin()
            elif user == "register":
                studregister()
            else :
                print("Wrong Input")
        except :
            print("Not Connected")
    def acess(self,user,userid):
        import mysql.connector
        mydb = mysql.connector.connect(host='localhost',user='root',password='1820',database='work')
        pointer=mydb.cursor()
        def techaccess():
            print("Hii "+userid)
            opt=input("Press 1 to See Students Details Press 2 to ADD Students Press 3 For Student Updation : ")
            if opt == "1":
                select = "select username,studentname,email,dob,fathername,mothername,Admdate from student"
                pointer.execute(select)
                data = pointer.fetchall()
                for i in data :
                    print(i)
            elif opt == "2":
                try :
                    username = input("Enter User Name : ")
                    username = username.lower()
                    Name = input("Enter Your Name : ")
                    Passw = input("Enter Password : ")
                    Email = input("Enter Email Address : ")
                    Dob = input("Enter Date Of Birth : ")
                    Father_Name = input("Enter Father Name : ")
                    Mother_Name = input("Enter Mother Name : ")
                    DAdm = input("Date Of Admission : ")
                    tup = (username,Name,Passw,Email,Dob,Father_Name,Mother_Name,DAdm)
                    user = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    pointer.execute(user,tup)
                    mydb.commit()
                    print("Registeration Sucessful")
                    mydb.close()
                except DuplicateSectionError as err:
                    print("Already Registered Please Login")
                except Exception as Err :
                    print("Registeration Unsucessful Due to : ",Err)
            elif opt == "3":
                user = input("Enter Student UserId : ")
                update.supdate(user)
            else :
                print("Sorry Wrong Input")
        def studaccess():
            print("Hii "+userid)
            opt = input("Would You Like to See Your Data : Y/N : ")
            opt=opt.lower()
            try :
                if opt == 'y': 
                    select = "select * from student where username = %s"
                    pointer.execute(select,(userid,))
                    data = pointer.fetchall()
                    print(data)
                else :
                    newopt=input("Would You like to update your Data : Y/N : ")
                    newopt = newopt.lower()
                    try :
                        if newopt == 'y':
                            update.supdate(userid)
                    except Exception as Err :
                        print(Err)
            except Exception as err:
                print(err)
        if user == "teacher":
            techaccess()
        else :
            studaccess()

obj = syc
obj()
