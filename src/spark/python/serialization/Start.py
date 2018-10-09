import pickle
sl = [1,2,3,4,5]
sd = {1:"1",2:"2",3:"3"}

path = "/home/tzablock/IdeaProjects/PythonLearn/repository/"
lf = open(path+"listfile.pickle","wb")
df = open(path+"dictfile.pickle","wb")
pickle.dump(sl,lf)
pickle.dump(sd,df)
lf.close()
df.close()

lrf = open(path+"listfile.pickle","rb")
drf = open(path+"dictfile.pickle","rb")
rsl = pickle.load(lrf)
rsd = pickle.load(drf)
lrf.close()
drf.close()
print(rsl)
print(rsd)
