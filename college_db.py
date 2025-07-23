class c:
    col = "NMAMIT, NITTE"
    def student(self, name, mark):
        self.name = name
        self.mark = mark
    def passfail(self):
        if(self.mark > 40):
            return "CLEAR"
        else:
            return "FAIL"
    def modify(self, grace):
        self.mark += grace

    def display(self):
        print("Name : {}".format(self.name))
        print("college : {}".format(self.col))
        print("Mark: {}".format(self.mark))
        print("Status : {}".format(self.passfail()))
s1 = c()
s2 = c()

s1.student("Nikitha", 38)
s2.student("Pooja", 70)
print()
s1.display()
print()
s2.display()
print()
s1.modify(3)
s1.display()
print()
