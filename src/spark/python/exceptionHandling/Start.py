try:
    list = [7,2,3,4]
    inx = input("Give some index.")
    inex = list.index(int(inx))
    print("Its ", inex)
except Exception as e:
    print("Such index not exist",e)