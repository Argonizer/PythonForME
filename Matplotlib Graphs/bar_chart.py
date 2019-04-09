import matplotlib.pyplot as plt

left = [1, 2,3,4,5]
height = [10, 20, 25, 40, 20]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label = tick_label, width=0.8, color = ["red", "green"])

plt.xlabel("Months")
plt.ylabel("Sales during each month")

plt.title("Sales Graph - Bar Chart")

plt.show()
