#Smart Student Helper

class students:
    def __init__(self,id,name,age,dept,tamil,english,math,science,social_science):
        self.id=id
        self.name=name
        self.age=age
        self.dept=dept
        self.tamil=int(tamil)
        self.english=int(english)
        self.math=int(math)
        self.science=int(science)
        self.social_science=int(social_science)
        
    def dictinory(self):
        student1={"id":self.id,
                  "name":self.name,
                  "age":self.age,
                  "dept":self.dept,
                  "tamil":self.tamil,
                  "english":self.english,
                  "math":self.math,
                  "science":self.science,
                  "scocial science":self.social_science
                  
                  }
            
        with open("students.txt","a") as f:
                    f.write(f"id: {self.id}, name: {self.name}, age: {self.age}, dept: {self.dept}\n")
                    f.write(f"tamil: {self.tamil}\n")
                    f.write(f"english: {self.english}\n")
                    f.write(f"math: {self.math}\n")
                    f.write(f"science: {self.science}\n")
                    f.write(f"social science: {self.social_science}\n\n")
        
    def __str__(self):
        return (f"id :{self.id} name :{self.name} age :{self.age} dept :{self.dept}\n"
                f"tamil :{self.tamil}\n" 
                f"english :{self.english}\n"
                f"math :{self.math}\n"
                f"science :{self.science}\n"
                f"social science :{self.social_science}\n")
        
    def get_marks(self):
        return [self.tamil, self.english, self.math, self.science, self.social_science]

#inserting student values       

while True:
    print("enter the student values :","you want exit say exit")
    id=(input("student id :").lower())
    if id=="exit":
        print("succrsfully exited")
        break
    name=(input("student name :"))
    age=(input("student age :"))
    dept=(input("student dept :"))
    tamil=(input("tamil mark :"))
    english=(input("english marks :"))
    math=(input("math mark :"))
    science=(input("science mark :"))
    social_science=input("social science mark :")
    
    def temp():
        student1=students(id,name,age,dept,tamil,english,math,science,social_science)
        student1.dictinory()
        print("sucessfully student detail saved saved")
    temp()
    