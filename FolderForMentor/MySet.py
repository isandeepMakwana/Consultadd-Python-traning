class MyCollection:
    def __init__(self):
        self.set = {}
    def MySet(self,x): #using dict in set
        for i in x:
            self.set[i]=0
        x=self.set.keys()
        return list(x)
    def MySet2(self,x): #using list in set
        self.set=[]
        for i in x:
            if i in self.set:
                continue
            else:
                self.set.append(i)
        return self.set








x =[]
for i in range(10):
    x.append(int(i%4+i%5+i/2))
print(x)
print(MyCollection().MySet(x))
print(MyCollection().MySet2(x))

