import sys
import time
from ClosestPair_raw import ClosestPair

fp = open("/Users/yhe/Desktop/3rd Year - Spring/CS 4102/Code/A-Programming/test1.txt", 'r')
fp2 = open("/Users/yhe/Desktop/3rd Year - Spring/CS 4102/Code/A-Programming/test2.txt", 'r')
fp3 = open("/Users/yhe/Desktop/3rd Year - Spring/CS 4102/Code/A-Programming/test3.txt", 'r')

lines = fp.readlines()
lines2 = fp2.readlines()
lines3 = fp3.readlines()

# Call the closest_pair function passing in the
# contents of the file

start = time.time()
cp = ClosestPair()
print(cp.compute(lines))
end = time.time()
print("time: " + str(end - start))

start = time.time()
cp = ClosestPair()
print(cp.compute(lines2))
end = time.time()
print("time: " + str(end - start))


start = time.time()
cp = ClosestPair()
print(cp.compute(lines3))
end = time.time()
print("time: " + str(end - start))
