class abc:
    def dis(self, a, b):
        self.a = a
        self.b = b
    def greet(self):
        print("Good Morning")

z = abc()
x = abc()

z.dis(20, 10)
x.dis(50, 70)
varsha = []
varsha.append(x)
varsha.append(z)

print(varsha[0].a)
print(varsha[0].b)
print(varsha[1].a)
print(varsha[1].a)

print(varsha[0].a + varsha[0].b)