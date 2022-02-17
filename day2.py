
import csv
def ShowNames(file_name):
    with open(file_name , 'r') as csv_file:
        csv_reader_obj = csv.reader(csv_file)
        # print(csv_reader_obj)
        # print(next(csv_reader_obj))
        # print(next(csv_reader_obj))
        
        next(csv_reader_obj)
        names=set()
        for row in csv_reader_obj:
            # print(row)
            # print(row[0])
            names.add(row[0].title())
        return sorted(list(names))

# lst=ShowNames("DemoData.csv")
# print(lst)

def ShowNames2(filename):
    exampleFile = open(file=filename)
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    # print(exampleData)
    names = list(set(row[0] for row in exampleData))
    return sorted(names)

# print(ShowNames2("DemoData.csv"))

def ShowUniqueNames(file_name):
    try:
        with open(file_name , 'r') as csv_file:
            csv_reader_obj = csv.DictReader(csv_file)
            names=set(row["name"].title() for row in csv_reader_obj)
            return sorted(list(names))
    except:
        return "error to excute file !!!!"
    
print(ShowUniqueNames("DemoData.csv"))