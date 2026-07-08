class Student:
    def __init__(self, name, roll_no, subject, marks):
        self.name = name
        self.roll_no = roll_no
        self.subject = subject
        self.marks = marks

    def display(self):
        print(f"Name:{self.name}")
        print(f"Roll_no:{self.roll_no}")
        print(f"Subject:{self.subject}")
        print(f"Marks:{self.marks}")

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter your name:")
        roll_no = int(input("Enter your roll no.:"))
        subject = input("Enter your subject:")
        marks = float(input("Enter your marks: "))

        student = Student(name, roll_no, subject, marks)
        self.students.append(student)
        print("Successfully Added!")

    def view_student(self):
        if len(self.students) == 0:
            print("No student found")
        else:
            for student in self.students:
                print("Details")
                student.display()

    def search_student(self):
        roll_no = int(input("Enter the roll no. of student to search:"))
        for student in self.students:
            if student.roll_no == roll_no:
                student.display()
                return
        print("Student not found")  
        
    def del_student(self):
        roll_no = int(input("Enter roll no. of student to delete:"))
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
        print("Student Deleted")
        
sms = StudentManagement()

while True:
    print("----Student MAnagement System---")
    print("1.Add\n2.View\n3.Search\n4.Delete\n5.Exit")
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        sms.add_student()
        
    if choice == 2:
        sms.view_student()
        
    if choice == 3:
        sms.search_student()
        
    if choice == 4:
        sms.del_student()
        
    if choice == 5:
        sms.exit()
        print("Exiting....")
        break
    
    else:
        print("Invalid choice!")
                   
    
                                        
                    