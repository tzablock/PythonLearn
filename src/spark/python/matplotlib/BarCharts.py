from matplotlib import pyplot as plt, style as stl
stl.use("ggplot")

x = [1,2,3,4]
y = [4,2,7,8]

x1 = [1,2,5]
y1 = [3,7,2]

plt.bar(x,y, align="center",color="y") # to make bar diagram on canvas
plt.bar(x1,y1,color="g", align="center")

plt.title("some bar")
plt.xlabel("x label")
plt.ylabel("y label")

plt.show()