class employee:
    profit = 100000
    tax = 10
    company = "INFOSYS"

    def __init__(self, name, age, sal, per):
        self.name = name
        self.age = age
        self.sal = sal
        self.per = per

    def cal_tax(self):
        return (employee.tax/100)*self.sal
    def cal_share(self):
        return (self.per/100)*employee.profit
    
    def display(self):
        print("1. Name: {}".format(self.name))
        print("2. Age: {}".format(self.age))
        print("3. Salary: {}".format(self.sal))
        print("4. Percentage: {}".format(self.per))
        print("5. Tax: {}".format(self.cal_tax()))
        print("6. Share: {}".format(self.cal_share()))
    
a1 = employee("Sachin", 30, 80000, 5)
a2 = employee("Sehwag", 40, 60000, 2)
a3 = employee("Virat", 35, 70000, 3)

a1.display()
print("------------------------------------")
a2.display()
print("------------------------------------")
a3.display()