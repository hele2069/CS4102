import math
import copy
import random
import time


def distance(point1, point2):
    return math.sqrt(
        (point1[0] - point2[0]) * (point1[0] - point2[0]) +
        (point1[1] - point2[1]) * (point1[1] - point2[1]))


def bruteforce(points):
    minDistance = 10001
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if distance(points[i], points[j]) < minDistance:
                minDistance = distance(points[i], points[j])
    return minDistance


def helper(strip, size, n):
    min = n
    for i in range(size):
        j = i + 1
        while j < size and (strip[j][1] - strip[i][1]) < min:
            min = distance(strip[i], strip[j])
            j += 1
    return min


def Divcon(P, ori, n):
    if n <= 3:
        return bruteforce(P)

    m = n // 2
    mPoint = P[m]
    l = P[:m]
    r = P[m:]
    dl = Divcon(l, ori, m)
    dr = Divcon(r, ori, n - m)
    d = min(dl, dr)
    stripP = []
    stripQ = []
    lr = l + r
    for i in range(n):
        if abs(lr[i][0] - mPoint[0]) < d:
            stripP.append(lr[i])
        if abs(ori[i][0] - mPoint[0]) < d:
            stripQ.append(ori[i])

    stripP.sort(key=lambda point: point[1])
    min_a = min(d, helper(stripP, len(stripP), d))
    min_b = min(d, helper(stripQ, len(stripQ), d))
    return min(min_a, min_b)


def result(P, n):
    P.sort(key=lambda point: point[0])
    ori = copy.deepcopy(P)
    ori.sort(key=lambda point: point[1])
    return Divcon(P, ori, n)


"""
filename = "/Users/apple/Desktop//UVA/CS4102/Week3/test.txt"
P = []
with open(filename, ) as f:
    b = f.readline()
    n = int(b[0])
    for line in f:
        a = line.split(' ')
        if len(a) == 1:
            if int(a[0]) > 0:
                r = result(P, n)
                if r > 10000:
                    print("infinity")
                else:
                    print(round(r, 4))
                n = int(a[0])
                P.clear()
            else:
                r = result(P, n)
                if r > 10000:
                    print("infinity")
                else:
                    print(round(r, 4))
                P.clear()
        if len(a) > 1:
            point = [float(a[0]), float(a[1])]
            P.append(point)
"""
"""
n = int(input())
while n != 0:
    Po = []
    for i in range(n):
        x, y = map(float, input().split())
        p = [x, y]
        Po.append(p)
    a = result(Po, n)
    if a > 10000:
        print("infinity")
    else:
        dist = format(a, '.4f')
        print(dist)
    n = int(input())
"""
# ----First Experiment----#

X = 3000
P = []
for x in range(X):
    a = round(random.uniform(-50000, 50000), 4)
    b = round(random.uniform(-50000, 50000), 4)
    # print(a,b)
    point = [a, b]
    P.append(point)
co = copy.deepcopy(P)

fp = open("/Users/yhe/Desktop/3rd Year - Spring/CS 4102/Code/A-Programming/test1.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.split(' '))
points = list(map(lambda sub: list(map(float, sub)), points))
DIV_start = time.time()
a = result(points, len(points))
DIV_end = time.time()
print("DIV takes: ", (DIV_end - DIV_start), "seconds\n")
print(a)
