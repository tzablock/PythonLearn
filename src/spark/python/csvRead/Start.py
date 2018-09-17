import csv

with open("/home/tzablock/IdeaProjects/PythonLearn/repository/examplecsv.csv") as exampleCSV:
    readCSV = csv.reader(exampleCSV,delimiter = ',')
    ids = []
    strs = []
    for l in readCSV:
        print(l[0])
        print(l[1])
        ids.append(l[0])
        strs.append(l[1])

    print(ids)
    print(strs)
    id = input("Str for what id?")
    indx = ids.index(id)
    print("For ",id," is str ",strs[indx])

f = open("/home/tzablock/IdeaProjects/PythonLearn/repository/examplecsv.csv")
rows = csv.reader(f, delimiter = ",")
for r in rows:
    print(r)