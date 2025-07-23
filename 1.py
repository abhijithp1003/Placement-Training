class LC37:
    def student(self, name):
        self.name = name
    def display(self):
        print("The name is {}".format(self.name))
    def nature(self):
        print("{} is a good student".format(self.name))

a1 = LC37()
a2 = LC37()
a1.student("Abhijith")
a2.student("Adarsh")
a1.display()
a2.display()
a1.nature()

