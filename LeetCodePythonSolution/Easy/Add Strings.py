# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j = len(num1) -1 , len(num2) -1
        add = 0
        ans = list()
        while i>= 0 or j>= 0 or add > 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result =  x + y + add
            ans.append(str(result%10))
            add = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])
