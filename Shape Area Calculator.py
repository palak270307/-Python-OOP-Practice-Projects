class Shape:
    pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def Area(self):
        return self.length * self.breadth


print("---Shape Calculator---")
print("1.Circle\n2.Rectangle")

choice = int(input("Enter your choice:"))

if choice == 1:
    radius = int(input("Enter the radius: "))
    s = Circle(radius)
    print("Area of Circle is", s.Area())

elif choice == 2:
    length = int(input("Enter the length:"))
    breadth = int(input("Enter the breadth:"))
    s = Rectangle(length, breadth)
    print("Area of Rectangle is", s.Area())

else:
    print("Invalid choice!")