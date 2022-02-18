from unicodedata import name


class Outer:
    def __init__(self , name):
        self.name = name
        self.innerObj = self.Inner

    def __str__(self):
        return f"outer class member name = {self.name} and innerclass name "
    
    class Inner:
        def __init__(self , name):
            self.name = name
        # def __str__(self) -> str:f"{self.name} and outerclass name {name}"


'''
# print(Outer("outer_name"))
obj = Outer("outer_name")
a=obj.innerObj("inner_name")
print(a.name)
print(obj)
'''

# Example 2 : 
obj = Outer("outer_name").Inner("inner_take-name")
print(obj.name)
