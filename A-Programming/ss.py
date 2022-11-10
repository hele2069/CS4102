fp = open("/Users/yhe/Desktop/3rd Year - Spring/CS 4102/Code/A-Programming/test1.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.split(' '))
points = list(map(lambda sub: list(map(int, sub)), points))
print(type(points[1][1]))