# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 动态规划

class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n+1)
        G[0] = 1
        G[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]