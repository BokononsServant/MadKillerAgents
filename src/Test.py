class Test():
    def __init__(self):
        self.a="sdfg"

lst =[]
for i in range(10):
    lst.append(Test())
    

p=lst[5]
print p
print p in lst