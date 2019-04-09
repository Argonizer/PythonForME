import matplotlib.pyplot as plt

x1 = [1,2,3,4]
y1 = [3,6,7,8]


x2 = [4,7,2.8,9]
y2 = [3,5,7,8.7]


plt.plot(x1,y1,label = "line 1")

plt.plot(x2,y2,label = "line 2")

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.legend()
plt.show()

