import sys
import time
from Supply import Supply, Disjoint_set

# test1
fp = open("/Users/yhe/Desktop/3rd Year - Spring/CS 4102/Code/B-Programming/two_port.txt", 'r')
lines = fp.readlines()
inputLines = []
for line in lines:
    inputLines.append(line.strip())

# test2
fp2 = open("/Users/yhe/Desktop/3rd Year - Spring/CS 4102/Code/B-Programming/complete_graph_9.txt", 'r')
lines2 = fp2.readlines()
inputLines2 = []
for line in lines2:
    inputLines2.append(line.strip())

# test3
fp3 = open("/Users/yhe/Desktop/3rd Year - Spring/CS 4102/Code/B-Programming/complete_graph_14.txt", 'r')
lines3 = fp3.readlines()
inputLines3 = []
for line in lines3:
    inputLines3.append(line.strip())

# Call the compute() function in your class, passing in the
# contents of the file
supply = Supply()

start = time.time()
print(supply.compute(inputLines))
end = time.time()
print("time: "+ str(end-start))

start = time.time()
print(supply.compute(inputLines2))
end = time.time()
print("time: "+ str(end-start))

start = time.time()
print(supply.compute(inputLines3))
end = time.time()
print("time: "+ str(end-start))
