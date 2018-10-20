from matplotlib import style as s,pyplot as plt

s.use("ggplot")  # usage of other style(colors)

x = [1, 2, 3]
y = [5, 4, 3]

x1 = [2,5,3]
y1 = [6,1,4]
plt.plot(x, y,label="line 1", linewidth=10)  # plot variables with set linewidth
plt.plot(x1,y1,label="line 2", linewidth= 5)  # label is shown when .legend() is run

plt.title("Some diagram")  # named title and anxises
plt.xlabel("x")
plt.ylabel("y")

plt.legend()   # to show labels it's needed

plt.grid(True, color="k") # make color of lines in background dark

plt.show()