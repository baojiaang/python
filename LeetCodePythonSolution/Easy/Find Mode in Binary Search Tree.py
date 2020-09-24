# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
import sys
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        pre_val = -sys.maxsize - 1
        count = 0
        max_count = 0
        def preSearch(node: TreeNode):
            nonlocal ans
            nonlocal pre_val
            nonlocal count
            nonlocal max_count
            if node.left:
                preSearch(node.left)
            if node:
                val = node.val
                if val == pre_val:
                    count += 1
                else:
                    count = 1
                pre_val = val
                if count == max_count:
                    ans.append(val)
                elif count > max_count:
                    ans.clear()
                    ans.append(val)
                    max_count = count
            if node.right:
                preSearch(node.right)
        if(root):
            preSearch(root)
        return ans



