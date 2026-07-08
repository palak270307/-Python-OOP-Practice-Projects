class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(f"Name:{self.name}")
        print(f"Employee Id:{self.emp_id}")
        print(f"Salary:{self.salary}")


class FullTime(Employee):
    def __init__(self, name, emp_id, salary, bonus):
        super().__init__(name, emp_id, salary)
        self.bonus = bonus

    def total_salary(self):
        return self.salary + self.bonus


class PartTime(Employee):
    def __init__(self, name, emp_id, salary, hours):
        super().__init__(name, emp_id, salary)
        self.hours = hours

    def total_salary(self):
        return self.salary * self.hours


print("---EMPLOYEE SALARY MANAGEMENT SYSTEM---")
name = input("Enter Your Name:")
emp_id = input("Enter your id: ")
salary = int(input("Enter your base salary:"))

print("1.Full Time Employee")
print("2.Part Time Employee")

choice = int(input("Enter Your Choice:"))

if choice == 1:
    bonus = int(input("Enter bonus amount:"))
    emp = FullTime(name, emp_id, salary, bonus)
elif choice == 2:
    hours = int(input("Enter number of hours:"))
    emp = PartTime(name, emp_id, salary, hours)
else:
    print("Invalid choice")
    emp = None

if emp:
    emp.display()
    print("Total Salary:", emp.total_salary())
                 