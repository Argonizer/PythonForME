import math

points = [[1,2],[3,7], [5,8], [9,3], [4,2], [0,3], [5,5], [9,9], [7,5]]

shortest_distance = math.sqrt((points[0][0] - points[1][0])**2 + (points[0][1] - points[1][1])**2)
nearest_point1 = points[0]
nearest_point2 = points[1]

for i in range(len(points)):
    for j in range(len(points) - i - 1):
        distance = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
        if distance < shortest_distance:
            shortest_distance = distance
            nearest_point1 = points[i]
            nearest_point1 = points[j]


print("The nearest distance is between points", nearest_point1, "and", nearest_point2, "of", distance)

