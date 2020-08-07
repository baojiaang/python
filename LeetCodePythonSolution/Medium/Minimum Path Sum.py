from typing import List
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its pat
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 动态规划 此题简单

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        import numpy as np
        m = len(grid)
        n = len(grid[0])
        if m is 0 or n is 0:
            return 0
        else:
            res = np.zeros((m,n))
            for i in range(m):
                for j in range(n):
                    if i is 0 and j is 0:
                        res[i][j] = grid[i][j]
                    elif i is 0:
                        res[i][j] = res[i][j-1] + grid[i][j]
                    elif j is 0:
                        res[i][j] = res[i-1][j] + grid[i][j]
                    else:
                        res[i][j] = min(res[i-1][j],res[i][j-1]) + grid[i][j]
            return int(res[m-1][n-1])
