from matplotlib import pyplot as plt, style as stl
stl.use("ggplot")

x = [1,4,5]
y = [6,2,9]
x1 = [5,9,2]
y1 = [3,2,1]

plt.scatter(x,y,color="r")
plt.scatter(x1,y1,color="b")

plt.title("Title")
plt.xlabel("x label")
plt.ylabel("y label")

plt.show()