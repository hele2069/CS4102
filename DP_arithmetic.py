


def max_arith(nums, ops, i):
    memo = [[0]*(i+1)]*(i+1)

    return max_recur(nums, ops, 0, i, memo) 

def max_recur(nums, ops, i, j, memo):
    if nums[i] == nums[j]: 
        memo[i][j] = 0
    if ops[i] == '+':
        memo[i,j] = max_recur(nums,ops,i, j-1,memo) + j
    if ops[i] == '-':
        memo[i,j] = max_recur(nums,ops,i,j-1,memo) - j


nums = [1,2,3,4,5,6]
ops = ['+','-','-','-','+']

print(max_arith(nums,ops,5))


class PlacingParentheses:
    def getMaximValue(exp):
        n = exp.length()
        min,max = new int[n][n]
        for i in range(n):
            min[i][i] = exp.charAt(i * 2) - '0'
            max[i][i] = exp.charAt(i * 2) - '0'
        for(int size = 1; size <= n - 1; size++) {
            // fill in right-up half of the matrix through diagonal
            for(int i = 0; i <= n - 1 - size; i++) {
                int j = size + i;  // maintain j - i = size
                int[] res = getMinAndMax(exp, i, j, min, max);
                min[i][j] = res[0];
                max[i][j] = res[1];
            }
        }
        // max of eval(1..n)
        return max[0][n - 1];
    }

    def getMinAndMax(String exp, int i, int j,
            int[][] min,
            int[][] max) {
        int[] res = new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE};
        for(int index = i; index <= j - 1; index++) {
            // Map OPindex to character of exp
            char oper = exp.charAt(index * 2 + 1);
            // Combinations of mm, mM, Mm, MM
            long a = eval(min[i][index], min[index + 1][j], oper),
                    b  = eval(min[i][index], max[index + 1][j], oper),
                    c  = eval(max[i][index], min[index + 1][j], oper),
                    d  = eval(max[i][index], max[index + 1][j], oper);
            res[0] = (int) Math.min(a, Math.min(b,
                    Math.min(c, Math.min(d, res[0]))));
            res[1] = (int) Math.max(a, Math.max(b,
                    Math.max(c, Math.max(d, res[1]))));
        }
        return res;


    def eval(a, b, op):
        if op == '+': 
            return a + b
        elif op == '-':
            return a - b
        return 
