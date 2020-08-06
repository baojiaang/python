# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 动态规划 此题简单的
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m is 0 or n is 0:
            return 0

        import numpy as np
        res = np.zeros((m,n))
        res[0,:] = [1 for i in range(n)]
        res[:,0] = [1 for i in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return int(res[m-1][n-1])


if __name__=="__main__":
    s = Solution()
    print(s.uniquePaths(3,1))