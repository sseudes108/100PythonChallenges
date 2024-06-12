import math

pointA = [-3,4,-5]
pointB = [2,0,-4]

x = 0
y = 1
z = 2

xValue = (math.pow(pointB[x] - pointA[x], 2))
yValue = (math.pow(pointB[y] - pointA[y], 2))
zValue = (math.pow(pointB[z] - pointA[z], 2))

distance = round(math.sqrt(xValue + yValue + zValue), 5)

print(distance)