# Sometimes we want to save the objects, so that we can retrieve them later (Even after Program
# that generated the data has terminated). Or we want to transmit the object to someone or
# something else outside our application.

# Pickle module is used for serializing and deserializing the object.
'''
serializing object (Pickling): Create representation of an object.
deserializing object (Unpickling): Re-load the object from representation.

dump : pickle to file
load : unpickle from file
dumps : returns a pickled representation. We can store it in variable.
loads : unpickle from supplied variable.
'''

import pickle
print("Using dumps and loads to store it in variable ")
list1 =[2,4]
dict1 = {1:list1 , 2:'hello' , 3:list1}
pickle_dict = pickle.dumps(dict1)
print(pickle_dict)

dict2 =pickle.loads(pickle_dict)
print(dict2)

# obj1==obj2 => True
# obj1 is obj2 => False

print(id(dict1.get(1)), id(dict1.get(3)))
print(id(dict2.get(1)), id(dict2.get(3)))
print("*"*100)
print("Using dump and load to store it in File ")
cars =["Audi","BMW","Maruti 800" ,"Maruti Suzuki"]
file_name = "mycar.pkl"
fileobj= open(file_name,'wb')
pickle.dump(cars, fileobj)
fileobj.close();

file_name = "mycar.pkl"
fileobj=open(file_name,'rb')
mycar = pickle.load(fileobj)
print(mycar)
