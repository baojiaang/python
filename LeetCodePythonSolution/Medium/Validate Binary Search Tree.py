# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/validate-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 中序遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def midOrderSearch(node, pre=float('-inf'), next = float('inf')):
            if not node:
                return True
            if not midOrderSearch(node.left,pre,node.val):
                return False
            if node.val <= pre or node.val >= next:
                return False
            return midOrderSearch(node.right,node.val,next)
        return midOrderSearch(root)







