import random
class rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def set_dim(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b

nums = []
d = int(input("Enter num of rectangles: "))
for i in range(d):
    R = rect(random.randint(1,5), random.randint(5,10))
    # a = int(input("Enter length of ractangle {}: ".format(i+1)))
    # b = int(input("Enter breadth of rectangle {}: ".format(i+1)))

    # R.set_dim(a,b)
    nums.append(R)

index = 1
for i in nums:
    # if i.area()%2 == 0:
    print("length, breadth : ", i.a, ", ", i.b)
    print("Area of rectangle {} is {}".format(index, i.area()))
    index += 1

