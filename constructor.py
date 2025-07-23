class India:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("{} is a legend".format(self.name))

a1 = India("Sachin")
a1.display()
a1 = India("Dravid")
a1.display()
a1.display()