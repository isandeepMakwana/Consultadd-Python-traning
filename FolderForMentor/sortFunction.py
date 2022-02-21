
from argparse import ArgumentError
class MyCollection:
    def __init__(self):
        self._x=[]
        self._second_list=[]
        self._new_dict={}
    def __check1__(self,a, b,reverse=False):
        if reverse:
            return a>=b
        else:
            return a<=b
    def __check2__(self,a,b,reverse=False):
        if reverse:
            return a<b
        else:
            return b<a

    def __findPartitionPoint__(self,x,lb,ub,reversed):
        e ,f = lb , ub
        pp =0 # partition point
        while(e<f):
            while((e<ub) and self.__check1__(x[e],x[lb],reversed)): e=e+1
            while(self.__check2__(x[f],x[lb],reversed)): f=f-1
            if(e<f):
                tmp = x[e]
                x[e]=x[f]
                x[f] = tmp
            else:
                tmp = x[lb]
                x[lb] = x[f]
                x[f]=tmp
                pp = f
        return pp

    def __sortFun__(self,x,reversed):
        stack =[]
        lowerbond = 0
        upperBond=len(x)-1
        stack.append([lowerbond,upperBond])
        while(len(stack)!=0):
            lb ,ub = stack.pop();
            pp =self.__findPartitionPoint__(x, lb, ub ,reversed)
            if pp+1 <ub: stack.append([pp+1 , ub])
            if pp-1>lb: stack.append([lb, pp-1])
        return x

    def Mysort(self,container_obj, sortBy="key",reversed=False):
        x=self._x
        if type(container_obj)==type([]):
            if(sortBy!="key" and sortBy!="value"):
                lst=self._second_list # i am using list for repited elements
                for i in container_obj:
                    try:
                        lst.append([i[sortBy],i])
                    except KeyError:
                        raise KeyError("please pass correct key : in sortBy=<key>")
                self.__sortFun__(lst,reversed)
                x=[i[1] for i in lst]
                return x
            else:
                x=[i for i in container_obj]
                return self.__sortFun__(x,reversed)
        elif type(container_obj)==type({}):
            if(sortBy=="key"):
                x=[i for i in container_obj.keys()]
            elif sortBy=="value":
                x=[i for i in container_obj.values()]
            else:
                raise ArgumentError("USAGE: sortBy BY SUPPORTS ONLY 'key and value' ")
            self.__sortFun__(x,reversed)
            self._new_dict = {i:container_obj[i] for i in x}
            return self._new_dict

   
'''
test case 1: sort numbers
x =[]
for i in range(10):
    x.append(int(i%4+i%5+i/2))
print(MyCollection().Mysort())
'''   
'''
test case 2: sort names
x=['Jhon', 'Komal', 'Mukesh', 'Navin', 'Sandeep', 'Swagat', 'Vikas', 'Yuvraj']
print(MyCollection().Mysort())
'''

'''
test case 3 : sort in reverse order
print(MyCollection().Mysort() , reversed=True)
'''

'''
test case 4: sort dict
x={}
x["jhon"]=1
x["koman"]=3
x["komal"]=2

print(MyCollection().Mysort())

'''

'''
test case 5: sort dict order by (keys) in reverse order
x={}
x["jhon"]=1
x["koman"]=3
x["komal"]=2
print(MyCollection().Mysort() , reversed=True)
'''

'''
test case 6: sort dict order by values
x={}
x["jhon"]=1
x["koman"]=3
x["komal"]=2

print(MyCollection().Mysort(),sortBy="value")
print(MyCollection().Mysort(),sortBy="value" , reversed=True)

'''

# print(MyCollection().Mysort([int((i%4+i%5+i/2)%10) for i in range(10)],reversed=True))

list_of_dict=[
{"name": "navin", "isIndian": False, "miceCaught": 0,"age": 21},
{"name": "pradeep", "isIndian": True, "miceCaught": 0,"age": 20},
{"name": "nitin", "isIndian": True, "miceCaught": 0,"age": 24},
{"name": "pawan", "isIndian": True, "miceCaught": 0,"age": 25},
{"name": "rishak", "isIndian": True, "miceCaught": 0,"age": 32},
{"name": "anup", "isIndian": False, "miceCaught": 0,"age": 56}
]
print("printing in increasing order")
for i in (MyCollection().Mysort(list_of_dict,sortBy="name")):
    print(i)
print("printing in decreasing order")
_=print
for i in (MyCollection().Mysort(list_of_dict,sortBy="name",reversed=True)):
    _(i)
