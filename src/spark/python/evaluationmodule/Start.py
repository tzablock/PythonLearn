lString = "[1,2,3,4,5,6]"
l = eval(lString)
l.append(7)
print(l)
print(l[0])
eval("print('ssddd')")

exec("""
def someF():
    print("working!")
""")
someF()