APPID = 'YOUR_APPID_HERE'
import json, requests, sys

def names(url):
    response = requests.get(url)
    # print(response.text)
    jsonDataAsPythonDict = json.loads(response.text)
    data=[]
    for i in jsonDataAsPythonDict:
        data.append(i['emp_name'])
    print(list(set(data)))

url ='http://localhost:9009/emp'
names(url)