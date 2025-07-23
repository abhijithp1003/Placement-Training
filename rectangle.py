class rectangle:
    prop1 = "Sum of angles in ractangle is 360"
    prop2 = "Every angle is 90"
    def get_info(self):
        length = int(input("Enter len of rectangle : "))
        self.length = length
        breadth = int(input("Enter breadth of rectangle : "))
        self.breadth = breadth
    def display(self):
        print("Area of rectangle is {}".format(self.length * self.breadth))
        print("Perimeter is {}".format(2*(self.length + self.breadth)))
    
print("Properties of Rectangles:")
print("----------------------------------------")
print("1. ",rectangle().prop1)
print("2. ",rectangle().prop2)
print("----------------------------------------")

while True:
    a1 = rectangle()
    a2 = rectangle()

    a1.get_info()
    a1.display()
    print("----------------------------------------")
    a2.get_info()
    a2.display()
    print("----------------------------------------")
