class Cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a + self.b
    def mul(self):
        return self.a * self.b
    def sub(self):
        return self.a -self.b
    def div(self):
        return self.a /self.b

op=Cal(1,1)
print(op.add())
print(op.mul())
print(op.sub())
print(op.div())


