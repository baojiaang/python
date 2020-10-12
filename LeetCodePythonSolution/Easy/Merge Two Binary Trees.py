# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-two-binary-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        newNode = TreeNode(t1.val+t2.val)
        newNode.left = self.mergeTrees(t1.left,t2.left)
        newNode.right = self.mergeTrees(t1.right,t2.right)

        return newNode

