# range function and loop 

# x = range(0,6,1)
# for i in x:
#     print(i)

# list and it's function
'''a = [ i/2 for i in range(0 , 6 , 1)]

a.sort()
print(a)
print(type(a))
a.append(34)
print(a)
b = [i for i in range(19,10,-1)]
a.extend(b)
print(a)
print(a.index(19))
print(max(a))
print(min(a))
b.clear();
print(b)
b.insert(0,20)
print(b)
b.insert(0,30)
print(b)

# printf = print
# printf(a.count(2))
# printf(b.pop())
# print(b)
print(b.pop(0))

c= b.copy()
print(c)

b.append(304)
print(c)
'''
'''
#list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# newlist = [expression for item in iterable if condition == True]
'''

# dictionry
'''

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

# Tuples and Its Functions
Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

Same as a list methods working 
only one difference tuple is immutable or list is mutable

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")#Note: If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)
# If the item to remove does not exist, remove() will raise an error
'''


# try:
#     c=5/0
# except NameError as e:
#     print("error")
# except:
#     print("another error")


# create a Color class
class Color:
	
# constructor method
    def __init__(self):
        # object attributes
        self.name = 'Green'
        self.lg = self.Lightgreen()
        
    def show(self):
        print("Name:", self.name)
        
    # create Lightgreen class
    class Lightgreen:
        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'
        
        def display(self):
            print("Name:", self.name)
            print("Code:", self.code)

# create Color class object
outer = Color()

# method calling
outer.show()

# create a Lightgreen
# inner class object
g = outer.lg

# inner class method calling
g.display()


