import matplotlib.pyplot as plt

x1 = [1,2,3,4]
y1 = [3,6,7,8]


plt.plot(x1,y1,label = "line 1", color = "green",\
         linestyle = "dashed", marker="o", \
         markerfacecolor="blue", markersize=12)


plt.ylim(1,8)
plt.xlim(1,8)

plt.title("Stylised Line Graph")
plt.legend()
plt.show()
