class Test:
    def __init__(self,liste):
        self.value=1
        liste.append(self)




liste=[]

zuppi=Test(liste)

print liste[0].value
        