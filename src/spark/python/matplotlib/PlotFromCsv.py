from matplotlib import pyplot as plt, style as stl
import numpy as np

stl.use("ggplot")

x,y = np.loadtxt("exampleFile.csv",unpack=True,delimiter=",")
print(str(x)+" "+str(y))

plt.plot(x,y, label="label")
plt.legend()

plt.title("Title")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()