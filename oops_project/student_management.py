print("************************************Student Management**************************************")

class StudentManagement:
    def __init__(self, name, classes, rollnumber, age,underline):
        self.name = name
        self.classes = classes
        self.rollnumber = rollnumber
        self.age = age
        self.underline=underline
        
    # Method to display student details
    def student_details(self):
        print("Name:", self.name)
        print("Class:", self.classes)
        print("Roll Number:", self.rollnumber)
        print("Age:", self.age)
        print(self.underline)

    # Method to save student details to file
    def save_to_file(self, filename):
        with open(filename, "a") as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Class: {self.classes}\n")
            f.write(f"Roll Number: {self.rollnumber}\n")
            f.write(f"Age: {self.age}\n")
            f.write(f"1{self.underline}")
            
student_count=0

# Create a student object
while True:
    student1 = StudentManagement(input("name :"),input("classes :"),input("rollnumber :"),int(input("age :")),"------------------------------------------------------------------------------------------------------------------------")
    student_count += 1
    student1.student_details()
    student1.save_to_file("student.txt")
    
    print(f"student {student_count} detail added")

# Display details on console
    

# Save details to file
    
