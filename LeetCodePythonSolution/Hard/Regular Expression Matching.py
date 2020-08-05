# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/regular-expression-matching
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 动态规划
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        row, col = len(s), len(p)

        def match(i : int, j : int) -> bool:
            if i == 0:
                return False
            if p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]

        res = [[False] * (col+1) for i in range(row+1)]

        res[0][0] = True

        for i in range(row+1):
            for j in range(1,col+1):
                if p[j-1] == '*':
                    # 不匹配, 直接跳过 这对 a*
                    res[i][j] |= res[i][j-2]  # 只要res[i][j]或res[i][j-2]一个为True
                    if match(i,j-1):
                        # 不匹配， 但是不跳过这对 a*
                        res[i][j] |= res[i-1][j]
                else: # i,j 位置均为字母
                    if match(i,j):
                        res[i][j] |= res[i-1][j-1]
        return res[row][col]