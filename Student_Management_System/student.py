# Student Management System
import os

class student_details:
    def __init__(self,st_no,name,roll_number,age,course):
        self.st_no=st_no
        self.name=name
        self.roll_number=roll_number
        self.age=age
        self.course=course
        
            
    def write(self):
        if os.path.exists("student_management.txt"):
            with open("student_management.txt","w") as w:
                w.write("_________________________________________________________________________________________________\n")
                w.write(f"name : {self.name} \n")
                w.write(f"roll_number : {self.roll_number} \n")
                w.write(f"age : {self.age} \n")
                w.write(f"course : {self.course} \n")
                
    def append(self):
        if os.path.exists("student_management.txt"):
            with open("student_management.txt","a") as w:
                w.write("_________________________________________________________________________________________________\n")
                w.write(f"st_no {self.st_no} \n")
                w.write(f"name : {self.name} \n")
                w.write(f"roll_number : {self.roll_number} \n")
                w.write(f"age : {self.age} \n")
                w.write(f"course : {self.course} \n")
                
    
print("******************this is student management system********************************")
content=input(" \n write \n append \n you choose any i do it : ").lower()
student1=student_details(input("st_no :"),input("name :"),input("roll_number :"),input("age :"),input("course :"))
if content=="write":
    student1.write()
    
if content=="append":
    student1.append()

    