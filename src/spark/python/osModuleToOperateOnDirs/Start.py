import os
# get currect working dir
print(os.getcwd())
# make new folder
os.mkdir("newDir")
# to rename dir
os.rename("newDir","renamedDir")
# to remove dir
os.mkdir("toRemove")
os.rmdir("toRemove")