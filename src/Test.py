class Test:
    def __init__(self):
        self.list=[1,2,3]


x=Test()

print x.a
y=x.a
print y
x.a.remove(1)
print x.a
print y
