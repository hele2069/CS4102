# CS4102 Spring 2022 - Unit A Programming 
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: yh9vhg
# Collaborators: None
# Sources: Introduction to Algorithms, Cormen
#################################
import copy
import math


class ClosestPair:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distances
    # and return those values from this method
    #
    # @return the distances between the closest pair and second closest pair
    # with closest at position 0 and second at position 1 
    def compute(self, file_data):
        output = self.convert(file_data)
        n = len(output)
        return self.result(output, n)

    def convert(self, file_data):
        points = []
        for line in file_data:
            points.append(line.split(' '))
        points2 = list(map(lambda sub: list(map(float, sub)), points))
        return points2

    def distance(self, point1, point2):
        return math.sqrt(
            (point1[0] - point2[0]) * (point1[0] - point2[0]) +
            (point1[1] - point2[1]) * (point1[1] - point2[1]))

    def bruteforce(self, points):
        smallest = 50000
        secondsmallest = 50000
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if self.distance(points[i], points[j]) < smallest:
                    secondsmallest = smallest
                    smallest = self.distance(points[i], points[j])
                elif self.distance(points[i], points[j]) < secondsmallest:
                    secondsmallest = self.distance(points[i], points[j])
        return smallest, secondsmallest
    """
    def helper(self, strip, size, n):
        min = n
        for i in range(size):
            j = i + 1
            while j < size and (strip[j][1] - strip[i][1]) < min:
                print(self.distance(strip[i], strip[j]))
                min = self.distance(strip[i], strip[j])
                j += 1
        print(str(min)+"min")
        return min
    """

    def Divcon(self, P, n):
        if n <= 3:
            return self.bruteforce(P)
        m = n // 2
        mPoint = P[m]
        l = P[:m]
        r = P[m:]
        dl = self.Divcon(l, m)
        dr = self.Divcon(r, n - m)

        d = min(min(dl), min(dr))
        d1 = max(min(dl), min(dr))
        stripP = []
        lr = l + r
        for i in range(n):
            if abs(lr[i][0] - mPoint[0]) < d1:
                stripP.append(lr[i])
        stripP.sort(key=lambda point: point[1])
        #print(self.helper(stripP, len(stripP),d))
        #min_a = min(d, self.helper(stripP, len(stripP), d))
        #min_b = min(d1, self.helper(stripP, len(stripP), d1))
        a = self.bruteforce(stripP)
        b = sorted(list(set(a+dl+dr)))
        return b[0],b[1]
        #return min_a, min_b

    def result(self, P, n):
        P.sort(key=lambda point: point[0])
        return self.Divcon(P, n)
