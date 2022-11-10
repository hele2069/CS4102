import time
from TilingDino import TilingDino

fp = open("/Users/yhe/Desktop/3rd Year - Spring/CS 4102/Code/D-Programming/corner2.txt", 'r')
fulllines = fp.readlines()
lines = []
for line in fulllines:
    lines.append(line.strip())

# Call the tiling dino function passing in the
# contents of the file
start = time.time()
td = TilingDino()
result = td.compute(lines)
end = time.time()

#for i in range(len(result)):
#    print(result[i])

print(result)
print("time: "+ str(end-start))
