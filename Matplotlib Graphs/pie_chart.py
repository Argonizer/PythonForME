import matplotlib.pyplot as plt

slices = [2, 8, 9, 5]
colors = ["red", "blue", "green", "yellow"]

activities = ["eat", "sleep", "work", "play"]

plt.pie(slices, labels = activities, colors = colors, \
        startangle = 90, shadow = True, \
        explode = (0, 0, 0.1, 0), radius = 1.2, autopct = "%1.1f%%")


plt.legend()
plt.show()
