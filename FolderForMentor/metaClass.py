# Test= type("Test", (), {"x":5})
# t = Test()
# print(t.x)


class MetaC(type):
    def __new__(self , class_name , bases , attrs):
        # print("class name  : ", class_name)
        # print("basess : ", bases)
        # print("attrs : ",attrs)
        # return type(class_name , bases ,attrs)
        print(attrs)
        a={}
        for name, val in attrs.items () :
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a)
        return type(class_name, bases, a)

class Dog(metaclass = MetaC):
    x=5
    y=20
    def hello(self):
        return "call in Dog class "


d = Dog()
print(d.hello()) # it shows error becuse we change the name in meta class
# print(d.HELLO())
# pickling , unpikling