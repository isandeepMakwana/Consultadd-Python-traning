list_of_dict=[
{"name": "navin", "isIndian": False, "miceCaught": 1,"age": 21},
{"name": "pradeep", "isIndian": True, "miceCaught": 20,"age": 20},
{"name": "nitin", "isIndian": True, "miceCaught": 3,"age": 24},
{"name": "pawan", "isIndian": True, "miceCaught": 20,"age": 25},
{"name": "rishak", "isIndian": True, "miceCaught": 20,"age": 32},
{"name": "anup", "isIndian": False, "miceCaught": 10,"age": 56}
]
print(type(list_of_dict))
# print(list_of_dict)
second_dict=[]
for i in list_of_dict:
    second_dict.append([i["name"],i])
# print(second_dict)
second_dict.sort();
for i in second_dict:
    print(i)