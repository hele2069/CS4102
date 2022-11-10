
def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b

def MinAndMax(minimum, maximum, i, j, operators):
    min_value = 999999
    max_value = -999999
    for k in range(i, j):
        # four possible max and min 
        a = calc(minimum[i][k], minimum[k+1][j], operators[k])
        b = calc(minimum[i][k], maximum[k+1][j], operators[k])
        c = calc(maximum[i][k], minimum[k+1][j], operators[k])
        d = calc(maximum[i][k], maximum[k+1][j], operators[k])
        # 'current' mean and max depends on the last 'min' and 'max'
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value

def get_maximum_value(nums, ops):
    n = len(nums)
    min = [[0 for x in range(n)] for x in range(n)] # memoization space
    max = [[0 for x in range(n)] for x in range(n)] # memoization space

    for i in range(n):
        min[i][i] = nums[i] # the 'diagonal' entries set to number itself 
        max[i][i] = nums[i] # the 'diagonal' entries set to number itself 

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s 
            # best(1,n), best(2,n).....
            # all the way to best(n,n)
            # squared matrix of 'best' outcome in each cell
            min[i][j], max[i][j] = MinAndMax(min, max, i, j, ops) 

    return max[0][n-1]

def test(): 
    nums = [1,2,3,4,5,6]
    ops = ['+','-','-','-','+']
    print(get_maximum_value(nums, ops))

test()